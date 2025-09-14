import { useState, useEffect } from 'react';

interface FileInfo {
  filename: string;
  size: number;
  sizeFormatted: string;
  modifiedTime: string;
  createdTime: string;
  extension: string;
  isSupported: boolean;
  fullPath: string;
}

interface FilesResponse {
  files: FileInfo[];
  totalFiles: number;
  supportedFiles: number;
  lastScanned: string;
}

const LatestFiles = () => {
  const [files, setFiles] = useState<FileInfo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastScanned, setLastScanned] = useState<string>('');
  const [stats, setStats] = useState({ totalFiles: 0, supportedFiles: 0 });

  const fetchLatestFiles = async () => {
    try {
      setLoading(true);
      const response = await fetch('/api/files/latest');
      if (!response.ok) {
        throw new Error('Failed to fetch files');
      }
      const data: FilesResponse = await response.json();
      setFiles(data.files);
      setStats({ totalFiles: data.totalFiles, supportedFiles: data.supportedFiles });
      setLastScanned(data.lastScanned);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load files');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLatestFiles();
    const interval = setInterval(fetchLatestFiles, 30000);
    return () => clearInterval(interval);
  }, []);

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString('en-IN', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
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

  const getFileTypeColor = (extension: string, isSupported: boolean) => {
    if (!isSupported) return 'text-gray-400';
    switch (extension.toLowerCase()) {
      case '.pdf': return 'text-red-600';
      case '.doc':
      case '.docx': return 'text-blue-600';
      case '.xlsx':
      case '.xls': return 'text-green-600';
      case '.txt': return 'text-gray-600';
      case '.tex': return 'text-purple-600';
      default: return 'text-gray-500';
    }
  };

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-bold mb-4">Latest Files from PC</h2>
        <div className="flex items-center justify-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
          <span className="ml-3">Loading latest files...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-xl font-bold mb-4">Latest Files from PC</h2>
        <div className="text-red-600 text-center py-4">
          <p>Error: {error}</p>
          <button 
            onClick={fetchLatestFiles}
            className="mt-2 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-bold">Latest Files from PC</h2>
        <button 
          onClick={fetchLatestFiles}
          className="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Refresh
        </button>
      </div>
      
      <div className="text-sm text-gray-600 mb-4">
        <p>Total: {stats.totalFiles} files | Supported: {stats.supportedFiles} files</p>
        <p>Last scanned: {lastScanned ? formatDate(lastScanned) : 'Never'}</p>
      </div>

      {files.length === 0 ? (
        <p className="text-center text-gray-500 py-4">No files found</p>
      ) : (
        <div className="space-y-2 max-h-96 overflow-y-auto">
          {files.map((file, index) => (
            <div 
              key={index}
              className={`flex items-center justify-between p-3 rounded-lg border ${
                file.isSupported 
                  ? 'border-green-200 bg-green-50 hover:bg-green-100' 
                  : 'border-gray-200 bg-gray-50 hover:bg-gray-100'
              }`}
            >
              <div className="flex items-center space-x-3 flex-1 min-w-0">
                <span className="text-2xl">{getFileIcon(file.extension)}</span>
                <div className="min-w-0 flex-1">
                  <p className={`font-medium truncate ${getFileTypeColor(file.extension, file.isSupported)}`}>
                    {file.filename}
                  </p>
                  <div className="text-xs text-gray-500 space-y-1">
                    <p>Size: {file.sizeFormatted}</p>
                    <p>Modified: {formatDate(file.modifiedTime)}</p>
                  </div>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <span className={`px-2 py-1 rounded-full text-xs ${
                  file.isSupported 
                    ? 'bg-green-100 text-green-800' 
                    : 'bg-gray-100 text-gray-600'
                }`}>
                  {file.isSupported ? 'Supported' : 'Unsupported'}
                </span>
                <span className="text-xs text-gray-400">
                  {file.extension.toUpperCase()}
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default LatestFiles;