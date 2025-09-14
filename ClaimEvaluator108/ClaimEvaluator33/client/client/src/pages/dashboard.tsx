import { useState, useEffect } from 'react';

interface FileDetail {
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
  files: FileDetail[];
  totalFiles: number;
  supportedFiles: number;
  lastScanned: string;
}

export default function Dashboard() {
  const [files, setFiles] = useState<FileDetail[]>([]);
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
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLatestFiles();
    // Auto-refresh every 30 seconds
    const interval = setInterval(fetchLatestFiles, 30000);
    return () => clearInterval(interval);
  }, []);

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString();
  };

  const getFileIcon = (extension: string) => {
    switch (extension.toLowerCase()) {
      case '.pdf': return '📄';
      case '.doc': case '.docx': return '📝';
      case '.xlsx': case '.xls': return '📊';
      case '.txt': return '📄';
      case '.tex': return '📋';
      default: return '📁';
    }
  };

  const getFileTypeColor = (extension: string, isSupported: boolean) => {
    if (!isSupported) return 'text-gray-400';
    switch (extension.toLowerCase()) {
      case '.pdf': return 'text-red-600';
      case '.doc': case '.docx': return 'text-blue-600';
      case '.xlsx': case '.xls': return 'text-green-600';
      case '.txt': case '.tex': return 'text-purple-600';
      default: return 'text-gray-600';
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Claims Evaluator Dashboard</h1>
          <p className="text-gray-600">Monitor and manage your latest files for claims analysis</p>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-blue-500 rounded-md flex items-center justify-center">
                  <span className="text-white text-sm font-medium">📁</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-500">Total Files</p>
                <p className="text-2xl font-bold text-gray-900">{stats.totalFiles}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-green-500 rounded-md flex items-center justify-center">
                  <span className="text-white text-sm font-medium">✅</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-500">Supported Files</p>
                <p className="text-2xl font-bold text-gray-900">{stats.supportedFiles}</p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="w-8 h-8 bg-purple-500 rounded-md flex items-center justify-center">
                  <span className="text-white text-sm font-medium">🔄</span>
                </div>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-500">Last Scanned</p>
                <p className="text-xs font-medium text-gray-900">
                  {lastScanned ? formatDate(lastScanned) : 'Never'}
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <button
                  onClick={fetchLatestFiles}
                  disabled={loading}
                  className="w-8 h-8 bg-indigo-500 hover:bg-indigo-600 disabled:bg-gray-400 rounded-md flex items-center justify-center transition-colors"
                >
                  <span className="text-white text-sm font-medium">{loading ? '⏳' : '🔄'}</span>
                </button>
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-500">Refresh Files</p>
                <p className="text-xs text-gray-600">Click to update</p>
              </div>
            </div>
          </div>
        </div>

        {/* Error Message */}
        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 rounded-md p-4">
            <div className="flex">
              <div className="ml-3">
                <h3 className="text-sm font-medium text-red-800">Error loading files</h3>
                <p className="mt-1 text-sm text-red-700">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Files Table */}
        <div className="bg-white shadow rounded-lg">
          <div className="px-6 py-4 border-b border-gray-200">
            <h3 className="text-lg font-medium text-gray-900">Latest Files from Your PC</h3>
            <p className="mt-1 text-sm text-gray-500">
              Showing recent files from your documents folder, sorted by modification date
            </p>
          </div>

          {loading ? (
            <div className="p-8 text-center">
              <div className="inline-flex items-center px-4 py-2 font-semibold leading-6 text-sm shadow rounded-md text-gray-500 bg-white transition ease-in-out duration-150">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-gray-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Loading files...
              </div>
            </div>
          ) : files.length === 0 ? (
            <div className="p-8 text-center text-gray-500">
              <div className="text-6xl mb-4">📁</div>
              <h3 className="text-lg font-medium mb-2">No files found</h3>
              <p className="text-sm">No supported files found in the documents folder</p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      File
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Size
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Modified
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Type
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Status
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {files.map((file, index) => (
                    <tr key={index} className={`hover:bg-gray-50 ${!file.isSupported ? 'opacity-60' : ''}`}>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="flex items-center">
                          <span className="text-2xl mr-3">{getFileIcon(file.extension)}</span>
                          <div className="text-sm font-medium text-gray-900 truncate max-w-xs" title={file.filename}>
                            {file.filename}
                          </div>
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {file.sizeFormatted}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {formatDate(file.modifiedTime)}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`text-sm font-medium ${getFileTypeColor(file.extension, file.isSupported)}`}>
                          {file.extension.toUpperCase().substring(1)}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        {file.isSupported ? (
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                            ✓ Supported
                          </span>
                        ) : (
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                            ⚠ Unsupported
                          </span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="mt-8 text-center text-sm text-gray-500">
          <p>Files are automatically refreshed every 30 seconds • ClaimEvaluator22 v2.0</p>
        </div>
      </div>
    </div>
  );
}