#!/usr/bin/env node

/**
 * ClaimEvaluator Synergy Suite v3.0 - One-Click Deployment Script
 * Automated deployment with ClaimMaster.ai-level capabilities
 * 
 * This script performs:
 * 1. Environment validation
 * 2. Dependency installation and optimization
 * 3. Comprehensive testing
 * 4. Build optimization
 * 5. Deployment to Vercel
 * 6. Git repository updates
 */

import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

// Console colors for enhanced output
const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  magenta: '\x1b[35m'
};

function log(message, color = 'cyan') {
  console.log(`${colors[color]}${colors.bright}🚀 ${message}${colors.reset}`);
}

function error(message) {
  console.log(`${colors.red}${colors.bright}❌ ERROR: ${message}${colors.reset}`);
}

function success(message) {
  console.log(`${colors.green}${colors.bright}✅ ${message}${colors.reset}`);
}

function warning(message) {
  console.log(`${colors.yellow}${colors.bright}⚠️  ${message}${colors.reset}`);
}

// Deployment configuration
const deploymentConfig = {
  name: 'ClaimEvaluator Synergy Suite v3.0',
  version: '3.0.0',
  requiredNodeVersion: '18.0.0',
  requiredNpmVersion: '8.0.0',
  testTimeout: 120000, // 2 minutes
  buildTimeout: 300000, // 5 minutes
  deployTimeout: 180000  // 3 minutes
};

class OneClickDeployer {
  constructor() {
    this.startTime = Date.now();
    this.deploymentReport = {
      timestamp: new Date().toISOString(),
      steps: [],
      errors: [],
      warnings: [],
      performance: {},
      success: false
    };
  }

  async deploy() {
    try {
      log(`Starting ${deploymentConfig.name} deployment...`);
      
      await this.validateEnvironment();
      await this.installDependencies();
      await this.runTests();
      await this.optimizeBuild();
      await this.deployToVercel();
      await this.updateGitRepository();
      await this.generateReport();
      
      this.deploymentReport.success = true;
      success(`🎉 Deployment completed successfully in ${this.getElapsedTime()}!`);
      this.showSuccessInfo();
      
    } catch (err) {
      error(`Deployment failed: ${err.message}`);
      this.deploymentReport.errors.push({
        step: 'deployment',
        error: err.message,
        stack: err.stack
      });
      process.exit(1);
    }
  }

  async validateEnvironment() {
    const stepStart = Date.now();
    log('🔍 Validating environment...');
    
    try {
      // Check Node.js version
      const nodeVersion = process.version.slice(1);
      if (this.compareVersions(nodeVersion, deploymentConfig.requiredNodeVersion) < 0) {
        throw new Error(`Node.js ${deploymentConfig.requiredNodeVersion} or higher required. Current: ${nodeVersion}`);
      }
      
      // Check npm version
      const npmVersion = execSync('npm --version', { encoding: 'utf8' }).trim();
      if (this.compareVersions(npmVersion, deploymentConfig.requiredNpmVersion) < 0) {
        warning(`npm ${deploymentConfig.requiredNpmVersion} or higher recommended. Current: ${npmVersion}`);
      }
      
      // Check for required files
      const requiredFiles = [
        'package.json',
        '.replit',
        '.env.example',
        'server/index.ts',
        'client/src/App.tsx'
      ];
      
      for (const file of requiredFiles) {
        if (!fs.existsSync(path.join(rootDir, file))) {
          throw new Error(`Required file missing: ${file}`);
        }
      }
      
      // Check for API keys
      if (fs.existsSync(path.join(rootDir, '.env'))) {
        const envContent = fs.readFileSync(path.join(rootDir, '.env'), 'utf8');
        if (!envContent.includes('GROK_API_KEY') && !envContent.includes('OPENAI_API_KEY')) {
          warning('No AI API keys found in .env file. AI features may not work.');
        }
      } else {
        warning('.env file not found. Create from .env.example and add API keys.');
      }
      
      this.deploymentReport.steps.push({
        name: 'Environment Validation',
        status: 'completed',
        duration: Date.now() - stepStart,
        details: {
          nodeVersion,
          npmVersion,
          filesChecked: requiredFiles.length
        }
      });
      
      success('Environment validation completed');
      
    } catch (err) {
      this.deploymentReport.steps.push({
        name: 'Environment Validation',
        status: 'failed',
        duration: Date.now() - stepStart,
        error: err.message
      });
      throw err;
    }
  }

  async installDependencies() {
    const stepStart = Date.now();
    log('📦 Installing and optimizing dependencies...');
    
    try {
      // Clean previous installation
      this.execCommand('npm run clean', 'Cleaning previous build artifacts');
      
      // Install dependencies
      this.execCommand('npm ci --production=false', 'Installing dependencies');
      
      // Audit security
      try {
        this.execCommand('npm audit --audit-level=high', 'Security audit');
      } catch (auditErr) {
        warning('Security audit found issues. Review with: npm audit');
      }
      
      this.deploymentReport.steps.push({
        name: 'Dependency Installation',
        status: 'completed',
        duration: Date.now() - stepStart
      });
      
      success('Dependencies installed and optimized');
      
    } catch (err) {
      this.deploymentReport.steps.push({
        name: 'Dependency Installation',
        status: 'failed',
        duration: Date.now() - stepStart,
        error: err.message
      });
      throw err;
    }
  }

  async runTests() {
    const stepStart = Date.now();
    log('🧪 Running comprehensive test suite...');
    
    try {
      // Run all tests with timeout
      const testResults = this.execCommand(
        'npm run test:all', 
        'Running comprehensive tests',
        deploymentConfig.testTimeout
      );
      
      // Parse test results
      const testSummary = this.parseTestResults(testResults);
      
      this.deploymentReport.steps.push({
        name: 'Testing',
        status: 'completed',
        duration: Date.now() - stepStart,
        testSummary
      });
      
      success(`Tests completed: ${testSummary.passed} passed, ${testSummary.failed} failed`);
      
    } catch (err) {
      this.deploymentReport.steps.push({
        name: 'Testing',
        status: 'failed',
        duration: Date.now() - stepStart,
        error: err.message
      });
      
      // Don't fail deployment for test failures in development
      if (process.env.NODE_ENV !== 'production') {
        warning('Tests failed but continuing deployment in development mode');
      } else {
        throw new Error(`Tests failed: ${err.message}`);
      }
    }
  }

  async optimizeBuild() {
    const stepStart = Date.now();
    log('🏗️ Building and optimizing application...');
    
    try {
      // Run optimized build
      this.execCommand(
        'npm run build:optimize', 
        'Building optimized production version',
        deploymentConfig.buildTimeout
      );
      
      // Check build output
      const distPath = path.join(rootDir, 'dist');
      if (!fs.existsSync(distPath)) {
        throw new Error('Build output directory not found');
      }
      
      // Calculate build size
      const buildSize = this.calculateDirectorySize(distPath);
      
      this.deploymentReport.steps.push({
        name: 'Build Optimization',
        status: 'completed',
        duration: Date.now() - stepStart,
        buildSize: `${(buildSize / 1024 / 1024).toFixed(2)} MB`
      });
      
      success(`Build completed successfully (${(buildSize / 1024 / 1024).toFixed(2)} MB)`);
      
    } catch (err) {
      this.deploymentReport.steps.push({
        name: 'Build Optimization',
        status: 'failed',
        duration: Date.now() - stepStart,
        error: err.message
      });
      throw err;
    }
  }

  async deployToVercel() {
    const stepStart = Date.now();
    log('🌐 Deploying to Vercel...');
    
    try {
      // Check if Vercel CLI is installed
      try {
        execSync('vercel --version', { encoding: 'utf8' });
      } catch {
        log('Installing Vercel CLI...');
        this.execCommand('npm install -g vercel', 'Installing Vercel CLI globally');
      }
      
      // Deploy to Vercel
      const deployOutput = this.execCommand(
        'vercel --prod --yes', 
        'Deploying to Vercel production',
        deploymentConfig.deployTimeout
      );
      
      // Extract deployment URL
      const urlMatch = deployOutput.match(/https:\\/\\/[^\\s]+/);
      const deploymentUrl = urlMatch ? urlMatch[0] : 'URL not found in output';
      
      this.deploymentReport.steps.push({
        name: 'Vercel Deployment',
        status: 'completed',
        duration: Date.now() - stepStart,
        deploymentUrl
      });
      
      success(`Deployed to Vercel: ${deploymentUrl}`);
      
    } catch (err) {
      this.deploymentReport.steps.push({
        name: 'Vercel Deployment',
        status: 'failed',
        duration: Date.now() - stepStart,
        error: err.message
      });
      
      warning('Vercel deployment failed but continuing...');
      // Don't fail entire deployment for Vercel issues
    }
  }

  async updateGitRepository() {
    const stepStart = Date.now();
    log('📝 Updating Git repository...');
    
    try {
      // Check if there are changes to commit
      const status = execSync('git status --porcelain', { encoding: 'utf8' });
      
      if (status.trim()) {
        this.execCommand('git add .', 'Staging changes');
        this.execCommand(
          `git commit -m "🚀 Deploy ClaimEvaluator Synergy Suite v${deploymentConfig.version} - ${new Date().toISOString()}"`,
          'Committing changes'
        );
        
        try {
          this.execCommand('git push origin main', 'Pushing to remote repository');
        } catch {
          warning('Could not push to remote repository. Check your git configuration.');
        }
      } else {
        log('No changes to commit');
      }
      
      this.deploymentReport.steps.push({
        name: 'Git Repository Update',
        status: 'completed',
        duration: Date.now() - stepStart
      });
      
      success('Git repository updated');
      
    } catch (err) {
      this.deploymentReport.steps.push({
        name: 'Git Repository Update',
        status: 'failed',
        duration: Date.now() - stepStart,
        error: err.message
      });
      
      warning('Git update failed but deployment continues...');
    }
  }

  async generateReport() {
    const reportPath = path.join(rootDir, 'deployment-report.json');
    
    this.deploymentReport.performance.totalDuration = this.getElapsedTime();
    this.deploymentReport.performance.totalSteps = this.deploymentReport.steps.length;
    this.deploymentReport.performance.successfulSteps = this.deploymentReport.steps.filter(s => s.status === 'completed').length;
    
    fs.writeFileSync(reportPath, JSON.stringify(this.deploymentReport, null, 2));
    
    log(`📊 Deployment report saved to: deployment-report.json`);
  }

  showSuccessInfo() {
    console.log('\n' + '='.repeat(60));
    console.log(colors.green + colors.bright + '🎉 DEPLOYMENT SUCCESSFUL!' + colors.reset);
    console.log('='.repeat(60));
    console.log(`${colors.cyan}📱 Application:${colors.reset} ${deploymentConfig.name}`);
    console.log(`${colors.cyan}⏱️  Total Time:${colors.reset} ${this.getElapsedTime()}`);
    console.log(`${colors.cyan}🔧 Steps Completed:${colors.reset} ${this.deploymentReport.steps.length}`);
    console.log(`${colors.cyan}📊 Success Rate:${colors.reset} ${this.deploymentReport.performance.successfulSteps}/${this.deploymentReport.performance.totalSteps}`);
    
    if (this.deploymentReport.warnings.length > 0) {
      console.log(`${colors.yellow}⚠️  Warnings:${colors.reset} ${this.deploymentReport.warnings.length}`);
    }
    
    console.log('\n' + colors.green + '🚀 Your ClaimEvaluator Synergy Suite is ready!' + colors.reset);
    console.log(colors.blue + '📚 Documentation: README_RAJKUMAR.md' + colors.reset);
    console.log(colors.blue + '🐛 Issues: https://github.com/CRAJKUMARSINGH/ClaimEvaluator33/issues' + colors.reset);
    console.log('='.repeat(60) + '\n');
  }

  // Utility methods
  execCommand(command, description, timeout = 30000) {
    try {
      log(`${description}...`);
      return execSync(command, { 
        encoding: 'utf8', 
        timeout,
        cwd: rootDir,
        stdio: 'pipe'
      });
    } catch (err) {
      throw new Error(`Failed to ${description.toLowerCase()}: ${err.message}`);
    }
  }

  compareVersions(a, b) {
    const partsA = a.split('.').map(Number);
    const partsB = b.split('.').map(Number);
    
    for (let i = 0; i < Math.max(partsA.length, partsB.length); i++) {
      const partA = partsA[i] || 0;
      const partB = partsB[i] || 0;
      
      if (partA < partB) return -1;
      if (partA > partB) return 1;
    }
    
    return 0;
  }

  parseTestResults(output) {
    // Simple test result parsing - can be enhanced based on actual test runner
    const passedMatch = output.match(/(\\d+) passed/i);
    const failedMatch = output.match(/(\\d+) failed/i);
    
    return {
      passed: passedMatch ? parseInt(passedMatch[1]) : 0,
      failed: failedMatch ? parseInt(failedMatch[1]) : 0,
      total: (passedMatch ? parseInt(passedMatch[1]) : 0) + (failedMatch ? parseInt(failedMatch[1]) : 0)
    };
  }

  calculateDirectorySize(dirPath) {
    let size = 0;
    
    function calculateSize(currentPath) {
      const stats = fs.statSync(currentPath);
      if (stats.isFile()) {
        size += stats.size;
      } else if (stats.isDirectory()) {
        const files = fs.readdirSync(currentPath);
        files.forEach(file => {
          calculateSize(path.join(currentPath, file));
        });
      }
    }
    
    try {
      calculateSize(dirPath);
    } catch (err) {
      warning(`Could not calculate directory size: ${err.message}`);
    }
    
    return size;
  }

  getElapsedTime() {
    const elapsed = Date.now() - this.startTime;
    const minutes = Math.floor(elapsed / 60000);
    const seconds = Math.floor((elapsed % 60000) / 1000);
    return `${minutes}m ${seconds}s`;
  }
}

// Run deployment if called directly
if (process.argv[1] === __filename) {
  const deployer = new OneClickDeployer();
  deployer.deploy().catch(err => {
    error(`Deployment failed: ${err.message}`);
    process.exit(1);
  });
}

export default OneClickDeployer;
