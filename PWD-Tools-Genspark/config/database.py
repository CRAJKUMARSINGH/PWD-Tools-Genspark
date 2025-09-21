"""
Database Manager for PWD Tools Desktop Application
Handles SQLite database operations and data management
"""

import sqlite3
import os
from pathlib import Path
from datetime import datetime
import json

class DatabaseManager:
    def __init__(self, db_path=None):
        """Initialize database manager"""
        if db_path is None:
            self.db_path = Path(__file__).parent.parent / "data" / "pwd_tools.db"
        else:
            self.db_path = Path(db_path)
        
        # Ensure data directory exists
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Initialize database
        self.init_database()
    
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(str(self.db_path))
    
    def init_database(self):
        """Initialize database with required tables"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Create bills table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS bills (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        bill_number TEXT UNIQUE NOT NULL,
                        contractor_name TEXT NOT NULL,
                        work_description TEXT NOT NULL,
                        bill_amount REAL NOT NULL,
                        date_created TEXT NOT NULL,
                        status TEXT DEFAULT 'Active',
                        remarks TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create EMD records table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS emd_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tender_number TEXT NOT NULL,
                        contractor_name TEXT NOT NULL,
                        emd_amount REAL NOT NULL,
                        bank_name TEXT,
                        guarantee_number TEXT,
                        validity_date TEXT,
                        refund_status TEXT DEFAULT 'Pending',
                        refund_amount REAL,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create delay calculations table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS delay_calculations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        work_name TEXT NOT NULL,
                        start_date TEXT NOT NULL,
                        completion_date TEXT NOT NULL,
                        total_days INTEGER NOT NULL,
                        delay_days INTEGER NOT NULL,
                        penalty_amount REAL,
                        status TEXT NOT NULL,
                        remarks TEXT,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create deductions table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS deductions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        bill_number TEXT NOT NULL,
                        contractor_name TEXT NOT NULL,
                        gross_amount REAL NOT NULL,
                        tds_amount REAL NOT NULL,
                        security_deduction REAL NOT NULL,
                        other_deductions REAL DEFAULT 0,
                        net_amount REAL NOT NULL,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create financial progress table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS financial_progress (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        project_name TEXT NOT NULL,
                        total_contract_value REAL NOT NULL,
                        work_completed_percentage REAL NOT NULL,
                        amount_released REAL NOT NULL,
                        balance_amount REAL NOT NULL,
                        liquidity_damages REAL DEFAULT 0,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create security refunds table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS security_refunds (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        contractor_name TEXT NOT NULL,
                        work_description TEXT NOT NULL,
                        security_amount REAL NOT NULL,
                        retention_period_days INTEGER NOT NULL,
                        refund_eligibility TEXT NOT NULL,
                        refund_amount REAL,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create stamp duty calculations table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS stamp_duty_calculations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        work_order_number TEXT NOT NULL,
                        contractor_name TEXT NOT NULL,
                        work_description TEXT NOT NULL,
                        contract_value REAL NOT NULL,
                        stamp_duty_rate REAL NOT NULL,
                        stamp_duty_amount REAL NOT NULL,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create tender processing table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tender_processing (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tender_number TEXT NOT NULL,
                        tender_title TEXT NOT NULL,
                        contractor_name TEXT NOT NULL,
                        tender_amount REAL NOT NULL,
                        emd_amount REAL NOT NULL,
                        processing_status TEXT DEFAULT 'Under Review',
                        remarks TEXT,
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                # Create bill deviations table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS bill_deviations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        bill_number TEXT NOT NULL,
                        contractor_name TEXT NOT NULL,
                        original_amount REAL NOT NULL,
                        revised_amount REAL NOT NULL,
                        deviation_amount REAL NOT NULL,
                        deviation_percentage REAL NOT NULL,
                        reason TEXT NOT NULL,
                        approval_status TEXT DEFAULT 'Pending',
                        date_created TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                
                conn.commit()
                print("Database initialized successfully")
                
        except Exception as e:
            print(f"Error initializing database: {e}")
    
    def execute_query(self, query, params=None):
        """Execute a query and return success status"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error executing query: {e}")
            return False
    
    def fetch_one(self, query, params=None):
        """Fetch one record from database"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchone()
        except Exception as e:
            print(f"Error fetching one record: {e}")
            return None
    
    def fetch_all(self, query, params=None):
        """Fetch all records from database"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all records: {e}")
            return []
    
    def backup_database(self):
        """Create a backup of the database"""
        try:
            backup_path = self.db_path.parent / f"pwd_tools_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
            
            # Copy database file
            import shutil
            shutil.copy2(self.db_path, backup_path)
            
            print(f"Database backed up to: {backup_path}")
            return True
        except Exception as e:
            print(f"Error creating backup: {e}")
            return False
    
    def get_table_info(self, table_name):
        """Get information about a table"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(f"PRAGMA table_info({table_name})")
                return cursor.fetchall()
        except Exception as e:
            print(f"Error getting table info: {e}")
            return []
    
    def get_table_count(self, table_name):
        """Get record count for a table"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                return cursor.fetchone()[0]
        except Exception as e:
            print(f"Error getting table count: {e}")
            return 0