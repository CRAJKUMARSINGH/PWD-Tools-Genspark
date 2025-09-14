import express, { type Request, Response, NextFunction } from "express";
import { registerRoutes } from "./routes";
import fs from "fs";
import path from "path";
import { setupVite, serveStatic, log } from "./vite";
import cors from "cors";
import compression from "compression";
import { LRUCache } from "lru-cache";
import { nanoid } from "nanoid";
import { createServer } from "http";
import { WebSocketServer } from "ws";

const app = express();
const server = createServer(app);

// Enhanced WebSocket server for real-time ClaimMaster.ai features
const wss = new WebSocketServer({ server });

// Initialize enhanced memory cache for ClaimMaster.ai performance optimization
const cache = new LRUCache({
  max: parseInt(process.env.CACHE_MAX_SIZE || '1000'),
  ttl: parseInt(process.env.CACHE_TTL || '900000'), // 15 minutes
  allowStale: false,
  updateAgeOnGet: true,
  updateAgeOnHas: true
});

// Quantum computation cache for financial calculations
const quantumCache = new LRUCache({
  max: 500,
  ttl: 1000 * 60 * 60, // 1 hour for complex calculations
  allowStale: false
});

// AI session management
const aiSessions = new Map();

// Enhanced compression for ClaimMaster.ai-level performance
app.use(compression({
  level: process.env.NODE_ENV === 'production' ? 9 : 6,
  threshold: 1024,
  filter: (req, res) => {
    if (req.headers['x-no-compression']) {
      return false;
    }
    // Special handling for large claim documents
    if (req.path.includes('/api/documents') || req.path.includes('/api/quantum')) {
      return true;
    }
    return compression.filter(req, res);
  }
}));

// Enhanced body parsing for ClaimMaster.ai document processing
app.use(express.json({ 
  limit: process.env.MAX_FILE_SIZE ? `${process.env.MAX_FILE_SIZE}mb` : '50mb',
  type: ['application/json', 'text/plain']
}));

app.use(express.urlencoded({ 
  extended: true, 
  limit: process.env.MAX_FILE_SIZE ? `${process.env.MAX_FILE_SIZE}mb` : '50mb',
  parameterLimit: 1000
}));

// Advanced rate limiting with AI-aware throttling
const requestCounts = new Map();
const RATE_LIMIT = parseInt(process.env.RATE_LIMIT_REQUESTS || '100');
const RATE_WINDOW = parseInt(process.env.RATE_LIMIT_WINDOW_MS || '60000');

app.use((req, res, next) => {
  const clientIP = req.ip || req.connection.remoteAddress || 'unknown';
  const now = Date.now();
  const sessionId = req.headers['x-session-id'] || nanoid();
  
  // Enhanced rate limiting for AI endpoints
  const isAIEndpoint = req.path.includes('/api/ai') || req.path.includes('/api/quantum');
  const currentLimit = isAIEndpoint ? Math.floor(RATE_LIMIT * 0.3) : RATE_LIMIT;
  
  if (!requestCounts.has(clientIP)) {
    requestCounts.set(clientIP, { 
      count: 1, 
      resetTime: now + RATE_WINDOW,
      aiRequests: isAIEndpoint ? 1 : 0
    });
  } else {
    const clientData = requestCounts.get(clientIP);
    if (now > clientData.resetTime) {
      clientData.count = 1;
      clientData.aiRequests = isAIEndpoint ? 1 : 0;
      clientData.resetTime = now + RATE_WINDOW;
    } else {
      clientData.count++;
      if (isAIEndpoint) clientData.aiRequests++;
      
      const checkLimit = isAIEndpoint ? clientData.aiRequests : clientData.count;
      if (checkLimit > currentLimit) {
        return res.status(429).json({ 
          message: `Rate limit exceeded for ${isAIEndpoint ? 'AI' : 'general'} requests. Please try again later.`,
          retryAfter: Math.ceil((clientData.resetTime - now) / 1000),
          type: isAIEndpoint ? 'ai_throttle' : 'general_throttle'
        });
      }
    }
  }
  
  // Add session tracking for AI continuity
  res.setHeader('X-Session-ID', sessionId);
  if (req.url.startsWith('/api/')) {
    res.setHeader('X-Powered-By', 'ClaimEvaluator-Synergy-Suite-v3.0');
    res.setHeader('X-AI-Capabilities', 'grok,openai,gemini,quantum');
  }
  
  next();
});

// CORS configuration for ClaimMaster.ai multi-platform support
const corsOrigins = process.env.NODE_ENV === 'production' 
  ? (process.env.CORS_ORIGIN || 'https://your-app.repl.co').split(',')
  : ['http://localhost:5003', 'http://localhost:3000', 'http://localhost:5000', 'https://*.repl.co'];

app.use(cors({ 
  origin: corsOrigins,
  credentials: true,
  optionsSuccessStatus: 200,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Session-ID', 'X-AI-Provider', 'X-Quantum-Mode']
}));

// Enhanced cache control with ClaimMaster.ai optimization
app.use((req, res, next) => {
  // Static assets - aggressive caching
  if (req.url.match(/\.(css|js|png|jpg|jpeg|gif|svg|ico|woff|woff2|ttf|eot)$/)) {
    res.setHeader('Cache-Control', 'public, max-age=31536000, immutable'); // 1 year
    res.setHeader('Vary', 'Accept-Encoding');
  } 
  // HTML files - moderate caching
  else if (req.url.match(/\.(html|htm)$/)) {
    res.setHeader('Cache-Control', 'public, max-age=3600'); // 1 hour
  }
  // API responses - conditional caching
  else if (req.url.startsWith('/api/')) {
    if (req.url.includes('/analysis') || req.url.includes('/quantum')) {
      res.setHeader('Cache-Control', 'private, max-age=300'); // 5 minutes for AI results
    } else {
      res.setHeader('Cache-Control', 'no-cache');
    }
  }
  next();
});

// Enhanced performance monitoring with ClaimMaster.ai metrics
app.use((req, res, next) => {
  const start = Date.now();
  const path = req.path;
  const method = req.method;
  const sessionId = req.headers['x-session-id'];
  let capturedJsonResponse: Record<string, any> | undefined = undefined;

  const originalResJson = res.json;
  res.json = function (bodyJson, ...args) {
    capturedJsonResponse = bodyJson;
    return originalResJson.apply(res, [bodyJson, ...args]);
  };

  res.on("finish", () => {
    const duration = Date.now() - start;
    
    // Enhanced logging for ClaimMaster.ai features
    if (path.startsWith("/api")) {
      let logLine = `${method} ${path} ${res.statusCode} in ${duration}ms`;
      
      // Add AI provider info if available
      const aiProvider = req.headers['x-ai-provider'];
      if (aiProvider) {
        logLine += ` [AI: ${aiProvider}]`;
      }
      
      // Add quantum mode info
      const quantumMode = req.headers['x-quantum-mode'];
      if (quantumMode) {
        logLine += ` [Quantum: ${quantumMode}]`;
      }
      
      // Add session info
      if (sessionId) {
        logLine += ` [Session: ${sessionId.slice(0, 8)}...]`;
      }

      if (capturedJsonResponse) {
        // Log key metrics for performance monitoring
        if (capturedJsonResponse.processingTime) {
          logLine += ` [Processing: ${capturedJsonResponse.processingTime}ms]`;
        }
        if (capturedJsonResponse.aiTokensUsed) {
          logLine += ` [Tokens: ${capturedJsonResponse.aiTokensUsed}]`;
        }
      }

      // Truncate long log lines
      if (logLine.length > 120) {
        logLine = logLine.slice(0, 119) + "…";
      }

      // Performance warning for slow requests
      if (duration > 5000) {
        log(`⚠️  SLOW: ${logLine}`);
      } else {
        log(logLine);
      }
      
      // Store performance metrics
      if (process.env.ENABLE_PERFORMANCE_LOGS === 'true') {
        const perfMetric = {
          timestamp: new Date().toISOString(),
          method,
          path,
          duration,
          statusCode: res.statusCode,
          aiProvider,
          quantumMode,
          sessionId: sessionId?.slice(0, 8)
        };
        
        // Store in cache for performance analysis
        const perfKey = `perf:${Date.now()}`;
        cache.set(perfKey, perfMetric);
      }
    }
  });

  next();
});

// WebSocket connection handler for real-time ClaimMaster.ai features
wss.on('connection', (ws, req) => {
  const sessionId = nanoid();
  ws.sessionId = sessionId;
  
  log(`WebSocket connected: ${sessionId}`);
  
  ws.on('message', async (message) => {
    try {
      const data = JSON.parse(message.toString());
      
      // Handle real-time quantum calculations
      if (data.type === 'quantum_calculate') {
        ws.send(JSON.stringify({
          type: 'quantum_progress',
          sessionId,
          progress: 0,
          message: 'Starting quantum calculations...'
        }));
        
        // Simulate progressive quantum calculation updates
        for (let i = 1; i <= 100; i += 10) {
          setTimeout(() => {
            ws.send(JSON.stringify({
              type: 'quantum_progress',
              sessionId,
              progress: i,
              message: `Calculating financial impact: ${i}%`
            }));
          }, i * 100);
        }
      }
      
      // Handle AI drafting progress
      if (data.type === 'ai_draft') {
        ws.send(JSON.stringify({
          type: 'ai_draft_progress',
          sessionId,
          stage: 'analysis',
          message: 'Analyzing claim documents...'
        }));
      }
      
    } catch (error) {
      log(`WebSocket error: ${error.message}`);
      ws.send(JSON.stringify({
        type: 'error',
        message: 'Invalid message format'
      }));
    }
  });
  
  ws.on('close', () => {
    log(`WebSocket disconnected: ${sessionId}`);
  });
});

// Memory management for ClaimMaster.ai performance
const gcInterval = parseInt(process.env.GC_INTERVAL_MS || '300000');
setInterval(() => {
  if (global.gc) {
    global.gc();
    log('Garbage collection completed');
  }
  
  // Clean up old AI sessions
  const now = Date.now();
  for (const [sessionId, sessionData] of aiSessions.entries()) {
    if (now - sessionData.lastActivity > 1800000) { // 30 minutes
      aiSessions.delete(sessionId);
    }
  }
  
  // Log memory usage
  const memUsage = process.memoryUsage();
  log(`Memory: RSS=${Math.round(memUsage.rss/1024/1024)}MB, Heap=${Math.round(memUsage.heapUsed/1024/1024)}MB`);
  
}, gcInterval);

// Export instances for use in other modules
export const appInstance = app;
export const serverInstance = server;
export const memoryCache = cache;
export const quantumMemoryCache = quantumCache;
export const webSocketServer = wss;
export const aiSessionManager = aiSessions;

// Initialize ClaimMaster.ai Synergy Suite
(async () => {
  const routesServer = await registerRoutes(app);

  // Enhanced error handling for ClaimMaster.ai features
  app.use((err: any, _req: Request, res: Response, _next: NextFunction) => {
    const status = err.status || err.statusCode || 500;
    const message = err.message || "Internal Server Error";
    
    // Enhanced error logging
    log(`Error ${status}: ${message} - Stack: ${err.stack?.slice(0, 200)}...`);
    
    // Specific error responses for AI failures
    if (err.code === 'AI_PROVIDER_ERROR') {
      res.status(503).json({ 
        message: 'AI service temporarily unavailable. Please try again.',
        type: 'ai_service_error',
        retryAfter: 30
      });
    } else if (err.code === 'QUANTUM_CALCULATION_ERROR') {
      res.status(422).json({ 
        message: 'Quantum calculation failed. Please check input parameters.',
        type: 'quantum_error',
        details: err.details
      });
    } else {
      res.status(status).json({ 
        message,
        type: 'general_error',
        ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
      });
    }
    
    throw err;
  });

  // Vite setup with ClaimMaster.ai optimizations
  const distPath = path.resolve(import.meta.dirname, "public");
  const isProduction = process.env.NODE_ENV === "production";
  
  if (!isProduction || !fs.existsSync(distPath)) {
    await setupVite(app, server);
  } else {
    serveStatic(app);
  }

  // Start ClaimMaster.ai Synergy Suite server
  const port = parseInt(process.env.PORT || '5003', 10);
  const host = process.env.NODE_ENV === 'development' ? 'localhost' : '0.0.0.0';
  
  server.listen(port, host, () => {
    log(`🚀 ClaimEvaluator Synergy Suite v3.0 running on http://${host}:${port}`);
    log(`🤖 AI Providers: Grok${process.env.OPENAI_API_KEY ? ', OpenAI' : ''}${process.env.GEMINI_API_KEY ? ', Gemini' : ''}`);
    log(`🧮 Quantum Calculations: Enabled`);
    log(`📊 Real-time WebSocket: Enabled on port ${port}`);
    log(`🎯 ClaimMaster.ai-level capabilities: Active`);
  });
})();
