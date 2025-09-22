"""
Application Settings Manager for PWD Tools Desktop
Handles configuration and user preferences
"""

import json
import os
from pathlib import Path
from datetime import datetime

class AppSettings:
    def __init__(self, config_file=None):
        """Initialize settings manager"""
        if config_file is None:
            self.config_file = Path(__file__).parent.parent / "data" / "settings.json"
        else:
            self.config_file = Path(config_file)
        
        self.settings = self.load_settings()
    
    def load_settings(self):
        """Load settings from file or create defaults"""
        default_settings = {
            "app_info": {
                "name": "PWD Tools Desktop",
                "version": "1.0.0",
                "author": "Mrs. Premlata Jain, AAO, PWD Udaipur"
            },
            "ui_settings": {
                "theme": "light",
                "color_scheme": "blue",
                "window_width": 1200,
                "window_height": 800,
                "font_size": 12
            },
            "department_info": {
                "name": "Public Works Department",
                "office": "PWD Office, Udaipur",
                "state": "Rajasthan",
                "contact": ""
            },
            "calculation_defaults": {
                "deduction_rate": 2.0,
                "stamp_duty_rate": 0.1,
                "penalty_rate": 0.5,
                "tax_rate": 18.0
            },
            "export_settings": {
                "default_export_path": "exports",
                "pdf_quality": "high",
                "excel_format": "xlsx",
                "auto_backup": True
            },
            "last_updated": datetime.now().isoformat()
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                return {**default_settings, **loaded_settings}
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading settings: {e}. Using defaults.")
                return default_settings
        else:
            # Create config file with defaults
            self.save_settings(default_settings)
            return default_settings
    
    def save_settings(self, settings=None):
        """Save settings to file"""
        if settings is None:
            settings = self.settings
        
        settings["last_updated"] = datetime.now().isoformat()
        
        # Ensure directory exists
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
            self.settings = settings
            return True
        except IOError as e:
            print(f"Error saving settings: {e}")
            return False
    
    def get(self, key_path, default=None):
        """Get setting value using dot notation (e.g., 'ui_settings.theme')"""
        keys = key_path.split('.')
        value = self.settings
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path, value):
        """Set setting value using dot notation"""
        keys = key_path.split('.')
        setting_dict = self.settings
        
        # Navigate to the parent dictionary
        for key in keys[:-1]:
            if key not in setting_dict:
                setting_dict[key] = {}
            setting_dict = setting_dict[key]
        
        # Set the value
        setting_dict[keys[-1]] = value
        
        # Save to file
        return self.save_settings()
    
    def get_department_info(self):
        """Get department information"""
        return self.get('department_info', {})
    
    def get_ui_settings(self):
        """Get UI settings"""
        return self.get('ui_settings', {})
    
    def get_calculation_defaults(self):
        """Get calculation default values"""
        return self.get('calculation_defaults', {})
    
    def update_department_info(self, **kwargs):
        """Update department information"""
        dept_info = self.get('department_info', {})
        dept_info.update(kwargs)
        return self.set('department_info', dept_info)
    
    def reset_to_defaults(self):
        """Reset all settings to defaults"""
        self.settings = {}
        self.settings = self.load_settings()
        return self.save_settings()
