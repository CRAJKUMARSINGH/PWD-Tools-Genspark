import type { Express, Request, Response } from "express";
import { createServer, type Server } from "http";
import { WebSocketServer } from "ws";
import multer from "multer";
import path from "path";
import fs from "fs";
import { storage } from "./storage";
import { DocumentParser } from "./services/documentParser";
import { AIAnalysisService } from "./services/aiAnalysis";
import { insertDocumentSchema, insertClaimsAnalysisSchema } from "../shared/schema";

const upload = multer({ 
  dest: 'uploads/',
  limits: { fileSize: 50 * 1024 * 1024 }, // 50MB limit
  fileFilter: (req, file, cb) => {
    const allowedTypes = [
      'application/pdf',
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      'application/msword',
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      'application/vnd.ms-excel',
      'text/plain'
    ];
    
    if (allowedTypes.includes(file.mimetype)) {
      cb(null, true);
    } else {
      cb(new Error(`Unsupported file type: ${file.mimetype}. Please upload PDF, Word, Excel, or text files only.`));
    }
  }
});

const documentParser = new DocumentParser();
const aiService = new AIAnalysisService();

export async function registerRoutes(app: Express): Promise<Server> {
  const httpServer = createServer(app);
  
  // Health check
  app.get('/api/health', (_req, res) => {
    res.json({ message: 'ClaimEvaluator-Integrated API is running' });
  });

  // Set up WebSocket server for real-time progress updates
  const wss = new WebSocketServer({ server: httpServer, path: '/ws/analysis-progress' });
  
  wss.on('connection', (ws) => {
    console.log('Client connected to progress WebSocket');
    
    ws.on('close', () => {
      console.log('Client disconnected from progress WebSocket');
    });
  });
  
  // Function to broadcast progress to all connected clients
  const broadcastProgress = (progress: any) => {
    wss.clients.forEach((client) => {
      if (client.readyState === 1) { // WebSocket.OPEN
        client.send(JSON.stringify({ type: 'progress', data: progress }));
      }
    });
  };
  
  // Document upload endpoint
  app.post("/api/documents/upload", upload.array('files'), (err: any, req: Request, res: any, next: any) => {
    if (err) {
      if (err.code === 'LIMIT_FILE_SIZE') {
        return res.status(400).json({ message: 'File too large. Maximum size is 50MB.' });
      }
      if (err.message && err.message.includes('Unsupported file type')) {
        return res.status(400).json({ message: err.message });
      }
      return res.status(400).json({ message: 'File upload error: ' + err.message });
    }
    next();
  }, async (req: Request, res: Response) => {
    try {
      if (!req.files || !Array.isArray(req.files)) {
        return res.status(400).json({ message: "No files uploaded" });
      }

      if (req.files.length === 0) {
        return res.status(400).json({ message: "No files uploaded" });
      }

      const uploadedDocs = [];

      for (const file of req.files) {
        const docData = {
          filename: file.filename,
          originalName: file.originalname,
          mimetype: file.mimetype,
          size: file.size
        };

        const validatedData = insertDocumentSchema.parse(docData);
        const document = await storage.createDocument(validatedData);
        
        // Parse document content
        try {
          const parsed = await documentParser.parseDocument(file.path, file.mimetype);
          await storage.updateDocumentContent(document.id, parsed.content, 'success');
        } catch (parseError) {
          await storage.updateDocumentContent(document.id, '', 'failed', parseError instanceof Error ? parseError.message : 'Parse failed');
        }

        uploadedDocs.push(document);
      }

      res.json({ documents: uploadedDocs });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Get all documents
  app.get("/api/documents", async (_req, res) => {
    try {
      const documents = await storage.getDocuments();
      res.json({ documents });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Claims analysis endpoint
  app.post("/api/analysis/create", async (req, res) => {
    try {
      const { documentIds } = req.body;
      
      if (!documentIds || !Array.isArray(documentIds)) {
        return res.status(400).json({ message: "Document IDs are required" });
      }

      // Get documents from storage
      const documents = await storage.getDocumentsByIds(documentIds);
      
      if (documents.length === 0) {
        return res.status(404).json({ message: "No documents found" });
      }

      // Set up progress callback
      aiService.setProgressCallback(broadcastProgress);

      // Perform AI analysis
      const analysisResult = await aiService.analyzeClaimsDocuments(
        documents.map(doc => ({ filename: doc.originalName, content: doc.content || '' }))
      );

      // Save analysis results
      const analysisData = {
        documentIds,
        currentClaims: analysisResult.currentClaims,
        enhancedClaims: analysisResult.enhancedClaims,
        inconsistencies: analysisResult.inconsistencies,
        recommendations: analysisResult.recommendations,
        totalCurrentValue: analysisResult.totalCurrentValue,
        totalEnhancedValue: analysisResult.totalEnhancedValue
      };

      const validatedAnalysis = insertClaimsAnalysisSchema.parse(analysisData);
      const analysis = await storage.createClaimsAnalysis(validatedAnalysis);

      res.json({ analysis, results: analysisResult });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Load and process all documents from sample folder
  app.post("/api/documents/load-sample-batch", async (_req, res) => {
    try {
      const sampleDir = path.join(process.cwd(), 'sample_input_documnets_of_a_project');
      
      if (!fs.existsSync(sampleDir)) {
        return res.status(404).json({ message: 'Sample documents folder not found' });
      }

      const files = fs.readdirSync(sampleDir);
      const validFiles = files.filter(file => {
        const ext = path.extname(file).toLowerCase();
        return ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex'].includes(ext) && !file.startsWith('~$');
      });

      const uploadedDocs = [];
      const processedCount = { success: 0, failed: 0 };
      
      for (const filename of validFiles) {
        try {
          const filePath = path.join(sampleDir, filename);
          const stats = fs.statSync(filePath);
          
          // Determine mimetype
          const ext = path.extname(filename).toLowerCase();
          const mimetypeMap: Record<string, string> = {
            '.pdf': 'application/pdf',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.doc': 'application/msword',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.xls': 'application/vnd.ms-excel',
            '.txt': 'text/plain',
            '.tex': 'text/plain'
          };
          
          const mimetype = mimetypeMap[ext] || 'application/octet-stream';
          
          const docData = {
            filename: filename.replace(/[^a-zA-Z0-9.-]/g, '_'),
            originalName: filename,
            mimetype,
            size: stats.size
          };

          const validatedData = insertDocumentSchema.parse(docData);
          const document = await storage.createDocument(validatedData);
          
          // Parse document content
          try {
            const parsed = await documentParser.parseDocument(filePath, mimetype);
            await storage.updateDocumentContent(document.id, parsed.content, 'success');
            processedCount.success++;
          } catch (parseError) {
            await storage.updateDocumentContent(document.id, '', 'failed', parseError instanceof Error ? parseError.message : 'Parse failed');
            processedCount.failed++;
          }

          uploadedDocs.push(document);
        } catch (error) {
          console.error(`Error processing file ${filename}:`, error);
          processedCount.failed++;
        }
      }

      res.json({ 
        documents: uploadedDocs, 
        message: `Loaded ${uploadedDocs.length} documents from sample folder`,
        processed: processedCount,
        totalFiles: validFiles.length
      });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Batch analyze all documents in database
  app.post("/api/analysis/batch-analyze", async (_req, res) => {
    try {
      // Get all successfully parsed documents
      const documents = await storage.getDocuments();
      const validDocs = documents.filter(doc => doc.parseStatus === 'success' && doc.content);
      
      if (validDocs.length === 0) {
        return res.status(400).json({ message: 'No valid documents found for analysis. Please upload documents first.' });
      }

      // Set up progress callback
      aiService.setProgressCallback(broadcastProgress);

      // Perform AI analysis on all documents
      const analysisResult = await aiService.analyzeClaimsDocuments(
        validDocs.map(doc => ({ filename: doc.originalName, content: doc.content || '' }))
      );

      // Save analysis results
      const analysisData = {
        documentIds: validDocs.map(doc => doc.id),
        currentClaims: analysisResult.currentClaims,
        enhancedClaims: analysisResult.enhancedClaims,
        inconsistencies: analysisResult.inconsistencies,
        recommendations: analysisResult.recommendations,
        totalCurrentValue: analysisResult.totalCurrentValue,
        totalEnhancedValue: analysisResult.totalEnhancedValue
      };

      const validatedAnalysis = insertClaimsAnalysisSchema.parse(analysisData);
      const analysis = await storage.createClaimsAnalysis(validatedAnalysis);

      res.json({ 
        analysis, 
        results: analysisResult,
        documentsAnalyzed: validDocs.length,
        message: `Successfully analyzed ${validDocs.length} documents`
      });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Get latest analysis
  app.get("/api/analysis/latest", async (_req, res) => {
    try {
      const analysis = await storage.getLatestAnalysis();
      res.json({ analysis });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Quick test endpoint for immediate analysis
  app.post("/api/quick-analysis", async (_req, res) => {
    try {
      const sampleDir = path.join(process.cwd(), 'sample_input_documnets_of_a_project');
      
      if (!fs.existsSync(sampleDir)) {
        return res.status(404).json({ message: 'Sample documents folder not found' });
      }

      // Process ALL documents in the folder (not just first 5)
      const allFiles = fs.readdirSync(sampleDir);
      const validFiles = allFiles.filter(file => {
        const ext = path.extname(file).toLowerCase();
        return ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex'].includes(ext) && !file.startsWith('~$');
      });
      
      console.log(`📁 Found ${allFiles.length} total files, ${validFiles.length} valid documents to process`);
      
      const documents = [];
      
      for (const filename of validFiles) {
        try {
          const filePath = path.join(sampleDir, filename);
          const stats = fs.statSync(filePath);
          const ext = path.extname(filename).toLowerCase();
          
          if (['.pdf', '.doc', '.docx', '.xlsx', '.txt', '.tex'].includes(ext)) {
            const parsed = await documentParser.parseDocument(filePath, 'application/octet-stream');
            documents.push({ filename, content: parsed.content });
          }
        } catch (error) {
          console.error(`Error processing ${filename}:`, error);
        }
      }

      // Run immediate analysis
      const analysisResult = await aiService.analyzeClaimsDocuments(documents);

      res.json({ 
        success: true,
        documentsProcessed: documents.length,
        results: analysisResult,
        message: `Comprehensive analysis completed on ${documents.length} documents (all documents in folder processed)`
      });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Comprehensive analysis endpoint for ALL 26 documents
  app.post("/api/comprehensive-analysis", async (_req, res) => {
    try {
      const sampleDir = path.join(process.cwd(), 'sample_input_documnets_of_a_project');
      
      if (!fs.existsSync(sampleDir)) {
        return res.status(404).json({ message: 'Sample documents folder not found' });
      }

      // Process ALL 26 documents in the folder
      const allFiles = fs.readdirSync(sampleDir);
      const validFiles = allFiles.filter(file => {
        const ext = path.extname(file).toLowerCase();
        return ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex'].includes(ext) && !file.startsWith('~$');
      });
      
      console.log(`📁 COMPREHENSIVE ANALYSIS: Processing ${validFiles.length} documents out of ${allFiles.length} total files`);
      
      const documents = [];
      let processedCount = 0;
      let failedCount = 0;
      
      for (const filename of validFiles) {
        try {
          const filePath = path.join(sampleDir, filename);
          const stats = fs.statSync(filePath);
          const ext = path.extname(filename).toLowerCase();
          
          if (['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex'].includes(ext)) {
            const parsed = await documentParser.parseDocument(filePath, 'application/octet-stream');
            documents.push({ filename, content: parsed.content });
            processedCount++;
            console.log(`✓ Processed: ${filename} (${(stats.size/1024).toFixed(1)}KB)`);
          }
        } catch (error) {
          console.error(`✗ Failed to process ${filename}:`, error);
          failedCount++;
        }
      }

      console.log(`📊 Analysis Summary: ${processedCount} processed, ${failedCount} failed`);

      // Run comprehensive analysis on ALL documents
      const analysisResult = await aiService.analyzeClaimsDocuments(documents);

      res.json({ 
        success: true,
        totalFilesFound: allFiles.length,
        validFiles: validFiles.length,
        documentsProcessed: processedCount,
        failedDocuments: failedCount,
        results: analysisResult,
        message: `Comprehensive analysis completed: ${processedCount} documents processed out of ${validFiles.length} valid files`
      });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Get latest files from PC
  app.get("/api/files/latest", async (_req, res) => {
    try {
      const sampleDir = path.join(process.cwd(), 'sample_input_documnets_of_a_project');
      
      if (!fs.existsSync(sampleDir)) {
        return res.status(404).json({ message: 'Documents folder not found' });
      }

      const files = fs.readdirSync(sampleDir);
      const fileDetails = [];
      
      for (const filename of files) {
        try {
          const filePath = path.join(sampleDir, filename);
          const stats = fs.statSync(filePath);
          
          // Skip system files and temporary files
          if (filename.startsWith('~$') || filename.startsWith('.')) {
            continue;
          }
          
          const ext = path.extname(filename).toLowerCase();
          const isSupported = ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex'].includes(ext);
          
          fileDetails.push({
            filename,
            size: stats.size,
            sizeFormatted: formatFileSize(stats.size),
            modifiedTime: stats.mtime,
            createdTime: stats.ctime,
            extension: ext,
            isSupported,
            fullPath: filePath
          });
        } catch (error) {
          console.error(`Error reading file stats for ${filename}:`, error);
        }
      }
      
      // Sort by modification time (newest first)
      fileDetails.sort((a, b) => new Date(b.modifiedTime).getTime() - new Date(a.modifiedTime).getTime());
      
      res.json({ 
        files: fileDetails,
        totalFiles: fileDetails.length,
        supportedFiles: fileDetails.filter(f => f.isSupported).length,
        lastScanned: new Date().toISOString()
      });
    } catch (error) {
      res.status(500).json({ message: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  // Enhanced API endpoint to scan PC directories
  app.get("/api/files/pc-scan", async (req, res) => {
    try {
      const { directories, limit = 100, fileTypes } = req.query;
      
      // Default directories to scan
      const defaultDirs = [
        path.join(process.env.USERPROFILE || 'C:\\Users\\Default', 'Documents'),
        path.join(process.env.USERPROFILE || 'C:\\Users\\Default', 'Desktop'),
        path.join(process.env.USERPROFILE || 'C:\\Users\\Default', 'Downloads'),
        process.cwd(), // Current project directory
        path.join(process.cwd(), 'sample_input_documnets_of_a_project')
      ];
      
      const customDirs = directories ? (directories as string).split(',').map(d => d.trim()) : [];
      const searchDirs = [...defaultDirs, ...customDirs];
      
      const allowedExtensions = fileTypes ? 
        (fileTypes as string).split(',').map(ext => ext.trim().toLowerCase()) : 
        ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex', '.md', '.json'];
      
      const recentFiles: Array<{
        name: string;
        path: string;
        size: number;
        sizeFormatted: string;
        modified: Date;
        extension: string;
        directory: string;
        isSupported: boolean;
      }> = [];
      
      const scannedDirs: string[] = [];
      
      // Scan directories for recent files
      for (const dir of searchDirs) {
        try {
          if (!fs.existsSync(dir)) continue;
          
          scannedDirs.push(dir);
          const files = fs.readdirSync(dir, { withFileTypes: true });
          
          for (const file of files) {
            if (file.isFile()) {
              const filePath = path.join(dir, file.name);
              const ext = path.extname(file.name).toLowerCase();
              
              if (allowedExtensions.includes(ext)) {
                try {
                  const stats = fs.statSync(filePath);
                  const isSupported = ['.pdf', '.doc', '.docx', '.xlsx', '.xls', '.txt', '.tex'].includes(ext);
                  
                  recentFiles.push({
                    name: file.name,
                    path: filePath,
                    size: stats.size,
                    sizeFormatted: formatFileSize(stats.size),
                    modified: stats.mtime,
                    extension: ext,
                    directory: dir,
                    isSupported
                  });
                } catch (statError) {
                  // Skip files that can't be accessed
                  continue;
                }
              }
            }
          }
        } catch (dirError) {
          // Skip directories that can't be accessed
          continue;
        }
      }
      
      // Sort by modification time (newest first) and limit results
      const sortedFiles = recentFiles
        .sort((a, b) => b.modified.getTime() - a.modified.getTime())
        .slice(0, parseInt(limit as string));
      
      res.json({
        files: sortedFiles,
        totalFound: recentFiles.length,
        directoriesScanned: scannedDirs,
        supportedFiles: sortedFiles.filter(f => f.isSupported).length,
        lastScanned: new Date().toISOString(),
        message: `Found ${sortedFiles.length} recent files from ${scannedDirs.length} directories`
      });
    } catch (error) {
      res.status(500).json({ 
        message: error instanceof Error ? error.message : 'Unknown error',
        error: 'Failed to scan PC directories'
      });
    }
  });

  // Helper function to format file sizes
  function formatFileSize(bytes: number): string {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  }

  // Test endpoint for ₹451.47 Crores analysis
  app.post("/api/test-451-analysis", async (_req, res) => {
    try {
      const testDocument = {
        filename: "TOTAL_CLAIM_SUMMARY.txt",
        content: `CONSTRUCTION CLAIM SUMMARY
Project: Infrastructure Development Project
TOTAL CLAIM AMOUNT: ₹451.47 CRORES
This represents the comprehensive claim for all project variations and delays.
Total Claim Value: 451.47 Crores
Amount in Rupees: ₹45,147,000,000
Legal Basis: FIDIC Contract Clauses
Status: Under Review`
      };

      const analysisResult = await aiService.analyzeClaimsDocuments([testDocument]);
      
      res.json({
        success: true,
        message: "₹451.47 Crores analysis completed",
        results: analysisResult
      });
    } catch (error) {
      console.error('Error in 451 analysis:', error);
      res.status(500).json({ error: 'Analysis failed', details: error instanceof Error ? error.message : 'Unknown error' });
    }
  });

  return httpServer;
}