import { sql } from "drizzle-orm";
import { pgTable, text, varchar, jsonb, timestamp, real, integer } from "drizzle-orm/pg-core";
import { createInsertSchema } from "drizzle-zod";
import { z } from "zod";

// Re-export types for easier imports
export * from './types';

export const users = pgTable("users", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  username: text("username").notNull().unique(),
  password: text("password").notNull(),
});

export const documents = pgTable("documents", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  filename: text("filename").notNull(),
  originalName: text("original_name").notNull(),
  mimetype: text("mimetype").notNull(),
  size: integer("size").notNull(),
  uploadedAt: timestamp("uploaded_at").defaultNow(),
  content: text("content"),
  parseStatus: text("parse_status").notNull().default('pending'), // pending, success, failed
  parseError: text("parse_error"),
});

export const claimsAnalysis = pgTable("claims_analysis", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  documentIds: jsonb("document_ids").$type<string[]>().notNull(),
  currentClaims: jsonb("current_claims").$type<ClaimItem[]>().notNull(),
  enhancedClaims: jsonb("enhanced_claims").$type<ClaimItem[]>(),
  inconsistencies: jsonb("inconsistencies").$type<Inconsistency[]>().notNull(),
  recommendations: jsonb("recommendations").$type<Recommendation[]>(),
  totalCurrentValue: real("total_current_value").notNull(),
  totalEnhancedValue: real("total_enhanced_value"),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export const calculations = pgTable("calculations", {
  id: varchar("id").primaryKey().default(sql`gen_random_uuid()`),
  analysisId: varchar("analysis_id").references(() => claimsAnalysis.id),
  methodology: text("methodology").notNull(), // fidic-traditional, fidic-green, nhai-ham
  contractValue: real("contract_value").notNull(),
  originalDuration: integer("original_duration").notNull(),
  extendedDuration: integer("extended_duration").notNull(),
  completionPercentage: real("completion_percentage").notNull(),
  calculationResults: jsonb("calculation_results").$type<CalculationResult[]>().notNull(),
  createdAt: timestamp("created_at").defaultNow(),
});

// Types for JSON fields
export type ClaimItem = {
  id: string;
  category: string;
  description: string;
  amount: number;
  status: 'complete' | 'review' | 'incomplete' | 'missing' | 'new';
  annexure?: string;
  evidence?: string[];
  legalBasis?: string;
  methodology?: string;
};

export type Inconsistency = {
  id: string;
  type: 'timeline' | 'missing_data' | 'unclear_reference' | 'calculation_error';
  severity: 'high' | 'medium' | 'low';
  description: string;
  location: string;
  suggestion: string;
};

export type Recommendation = {
  id: string;
  type: 'new_claim' | 'enhancement' | 'evidence' | 'legal_language';
  priority: 'critical' | 'high' | 'medium' | 'low';
  title: string;
  description: string;
  potentialValue?: number;
  evidence: string[];
  legalBasis: string;
  implementation: string;
};

export type CalculationResult = {
  id: string;
  category: string;
  methodology: string;
  inputs: Record<string, any>;
  calculations: Record<string, any>;
  result: number;
  breakdown?: Record<string, number>;
};

export type AnalysisResult = {
  currentClaims: ClaimItem[];
  enhancedClaims?: ClaimItem[];
  inconsistencies: Inconsistency[];
  recommendations: Recommendation[];
  totalCurrentValue: number;
  totalEnhancedValue?: number;
  calculationResults?: CalculationResult[];
  metadata?: {
    generatedAt: string;
    methodology?: string;
    projectName?: string;
    contractNumber?: string;
  };
};

export const insertDocumentSchema = createInsertSchema(documents).omit({
  id: true,
  uploadedAt: true,
});

export const insertClaimsAnalysisSchema = createInsertSchema(claimsAnalysis).omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

export const insertCalculationSchema = createInsertSchema(calculations).omit({
  id: true,
  createdAt: true,
});

export const insertUserSchema = createInsertSchema(users).pick({
  username: true,
  password: true,
});

export type InsertUser = z.infer<typeof insertUserSchema>;
export type User = typeof users.$inferSelect;
export type Document = typeof documents.$inferSelect;
export type InsertDocument = z.infer<typeof insertDocumentSchema>;
export type ClaimsAnalysisType = typeof claimsAnalysis.$inferSelect;
export type InsertClaimsAnalysis = z.infer<typeof insertClaimsAnalysisSchema>;
export type Calculation = typeof calculations.$inferSelect;
export type InsertCalculation = z.infer<typeof insertCalculationSchema>;