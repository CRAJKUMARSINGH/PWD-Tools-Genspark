// ClaimEvaluator22 Home Page with latest files preview
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

interface ProcessingState {
  stage: string;
  isLoading: boolean;
  documents: any[];
  analysis: any;
  error: string;
}

interface FileInfo {
  filename: string;
  sizeFormatted: string;
  modifiedTime: string;
  extension: string;
  isSupported: boolean;
}

export default function Home() {
  const [state, setState] = useState<ProcessingState>({
    stage: 'ready',
    isLoading: false,
    documents: [],
    analysis: null,
    error: ''
  });

  const [latestFiles, setLatestFiles] = useState<FileInfo[]>([]);
  const [fileStats, setFileStats] = useState({ totalFiles: 0, supportedFiles: 0 });

  // Fetch latest files on component mount
  useEffect(() => {
    fetchLatestFiles();
  }, []);

  const fetchLatestFiles = async () => {
    try {
      const response = await fetch('/api/files/latest');
      if (response.ok) {
        const data = await response.json();
        setLatestFiles(data.files.slice(0, 5)); // Show only first 5 files
        setFileStats({ totalFiles: data.totalFiles, supportedFiles: data.supportedFiles });
      }
    } catch (error) {
      console.error('Failed to fetch latest files:', error);
    }
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString('en-IN', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getFileIcon = (extension: string) => {
    switch (extension.toLowerCase()) {
      case '.pdf': return '📄';
      case '.doc':
      case '.docx': return '📝';
      case '.xlsx':
      case '.xls': return '📊';
      case '.txt': return '📋';
      case '.tex': return '📜';
      default: return '📁';
    }
  };

  const loadDocuments = async () => {
    setState(prev => ({ ...prev, isLoading: true, stage: 'loading', error: '' }));
    
    try {
      const response = await fetch('/api/documents/load-sample-batch', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'Failed to load documents');
      }
      
      setState(prev => ({
        ...prev,
        documents: data.documents,
        stage: 'documents-loaded',
        isLoading: false
      }));
    } catch (error) {
      setState(prev => ({
        ...prev,
        error: error instanceof Error ? error.message : 'Unknown error',
        isLoading: false,
        stage: 'error'
      }));
    }
  };

  const runAnalysis = async () => {
    setState(prev => ({ ...prev, isLoading: true, stage: 'analyzing', error: '' }));
    
    try {
      const response = await fetch('/api/analysis/batch-analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'Failed to analyze documents');
      }
      
      setState(prev => ({
        ...prev,
        analysis: data,
        stage: 'complete',
        isLoading: false
      }));
    } catch (error) {
      setState(prev => ({
        ...prev,
        error: error instanceof Error ? error.message : 'Unknown error',
        isLoading: false,
        stage: 'error'
      }));
    }
  };

  const quickTest = async () => {
    setState(prev => ({ ...prev, isLoading: true, stage: 'quick-test', error: '' }));
    
    try {
      const response = await fetch('/api/quick-analysis', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
      });
      
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'Failed to run quick analysis');
      }
      
      setState(prev => ({
        ...prev,
        analysis: data,
        stage: 'quick-complete',
        isLoading: false
      }));
    } catch (error) {
      setState(prev => ({
        ...prev,
        error: error instanceof Error ? error.message : 'Unknown error',
        isLoading: false,
        stage: 'error'
      }));
    }
  };

  const runFullPipeline = async () => {
    await loadDocuments();
    setTimeout(async () => {
      await runAnalysis();
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation Header */}
      <nav className="bg-white shadow-sm border-b">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <h1 className="text-2xl font-bold text-gray-900">ClaimEvaluator22</h1>
            <div className="space-x-4">
              <Link 
                to="/dashboard" 
                className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
              >
                Dashboard
              </Link>
              <Link 
                to="/templates" 
                className="px-4 py-2 text-blue-600 border border-blue-600 rounded hover:bg-blue-50 transition-colors"
              >
                Templates
              </Link>
            </div>
          </div>
        </div>
      </nav>

      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Processing Section */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-bold mb-4">Batch Processing</h2>
              <p className="text-gray-600 mb-6">Process all documents from your sample documents folder</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <button 
                  onClick={quickTest}
                  disabled={state.isLoading}
                  className="px-6 py-3 bg-red-600 text-white rounded-lg hover:bg-red-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                >
                  {state.isLoading ? 'Processing...' : '🚀 Quick Test (5 docs)'}
                </button>
                
                <button 
                  onClick={runFullPipeline}
                  disabled={state.isLoading}
                  className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                >
                  {state.isLoading ? 'Processing...' : 'Full Pipeline (All docs)'}
                </button>
                
                <button 
                  onClick={loadDocuments}
                  disabled={state.isLoading}
                  className="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                >
                  Load Documents Only
                </button>
                
                <button 
                  onClick={runAnalysis}
                  disabled={state.isLoading || state.documents.length === 0}
                  className="px-6 py-3 bg-yellow-600 text-white rounded-lg hover:bg-yellow-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                >
                  Analyze Documents
                </button>
              </div>

              <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <h3 className="font-semibold mb-2">Status: {state.stage}</h3>
                {state.isLoading && <p className="text-blue-600">⏳ Processing...</p>}
                {state.error && <p className="text-red-600">❌ Error: {state.error}</p>}
              </div>

              {state.documents.length > 0 && (
                <div className="mb-6">
                  <h3 className="font-semibold mb-3">📄 Documents Loaded ({state.documents.length})</h3>
                  <div className="max-h-48 overflow-y-auto border rounded-lg p-3 bg-gray-50">
                    {state.documents.map((doc, index) => (
                      <div key={index} className="py-2 border-b border-gray-200 last:border-b-0">
                        <div className="font-medium">{doc.originalName}</div>
                        <div className="text-sm text-gray-600">
                          {doc.parseStatus} • {doc.mimetype} • {(doc.size / 1024).toFixed(1)} KB
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {state.analysis && (
                <div>
                  <h3 className="font-semibold mb-3">📊 Analysis Results</h3>
                  <div className="bg-blue-50 rounded-lg p-4 space-y-2">
                    <p><strong>Documents Analyzed:</strong> {state.analysis.documentsAnalyzed}</p>
                    <p><strong>Current Claims:</strong> {state.analysis.results.currentClaims?.length || 0}</p>
                    <p><strong>Total Current Value:</strong> ₹{state.analysis.results.totalCurrentValue?.toLocaleString() || 0}</p>
                    <p><strong>Enhanced Value:</strong> ₹{state.analysis.results.totalEnhancedValue?.toLocaleString() || 0}</p>
                    <p><strong>Inconsistencies Found:</strong> {state.analysis.results.inconsistencies?.length || 0}</p>
                    <p><strong>Recommendations:</strong> {state.analysis.results.recommendations?.length || 0}</p>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Latest Files Preview */}
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-semibold">Latest Files Preview</h3>
              <Link 
                to="/dashboard" 
                className="text-blue-600 hover:text-blue-800 text-sm"
              >
                View All →
              </Link>
            </div>
            
            <div className="text-sm text-gray-600 mb-4">
              <p>Total: {fileStats.totalFiles} files</p>
              <p>Supported: {fileStats.supportedFiles} files</p>
            </div>

            {latestFiles.length > 0 ? (
              <div className="space-y-3">
                {latestFiles.map((file, index) => (
                  <div key={index} className="flex items-start space-x-3 p-2 rounded border">
                    <span className="text-lg">{getFileIcon(file.extension)}</span>
                    <div className="flex-1 min-w-0">
                      <p className="font-medium text-sm truncate">{file.filename}</p>
                      <div className="text-xs text-gray-500">
                        <p>{file.sizeFormatted} • {formatDate(file.modifiedTime)}</p>
                      </div>
                    </div>
                    <span className={`px-1 py-0.5 rounded text-xs ${
                      file.isSupported ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'
                    }`}>
                      {file.extension.toUpperCase()}
                    </span>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-gray-500 text-center py-4">No files found</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}