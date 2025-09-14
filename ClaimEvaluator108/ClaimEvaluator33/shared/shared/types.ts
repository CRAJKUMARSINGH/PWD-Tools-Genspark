// Base types that don't depend on schema
export type PDFGenerationOptions = {
  includeCharts?: boolean;
  includeAppendices?: boolean;
  customStyles?: Record<string, string>;
};

export type PDFResult = {
  success: boolean;
  filePath?: string;
  downloadUrl?: string;
  error?: string;
  sizeInBytes?: number;
  generatedAt?: string;
};

// These will be re-exported from schema.ts to avoid circular dependencies
export type { 
  ClaimItem,
  Inconsistency, 
  Recommendation, 
  CalculationResult,
  AnalysisResult 
} from './schema';