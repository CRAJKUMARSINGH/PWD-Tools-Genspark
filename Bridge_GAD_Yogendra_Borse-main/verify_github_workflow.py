#!/usr/bin/env python3
"""
Verification script for GitHub workflow.
"""

import os
import yaml

def check_workflow_file():
    """Check if the GitHub workflow file exists and is valid."""
    workflow_path = os.path.join(os.path.dirname(__file__), '.github', 'workflows', 'release.yml')
    
    if not os.path.exists(workflow_path):
        print("❌ GitHub workflow file not found")
        return False
    
    try:
        with open(workflow_path, 'r') as f:
            workflow_content = yaml.safe_load(f)
        
        # Check for required keys
        required_keys = ['name', 'on', 'jobs']
        missing_keys = [key for key in required_keys if key not in workflow_content]
        
        if missing_keys:
            print(f"❌ Missing required keys in workflow: {missing_keys}")
            return False
        
        # Check for tag trigger
        if 'push' not in workflow_content['on'] or 'tags' not in workflow_content['on']['push']:
            print("❌ Workflow does not trigger on tag pushes")
            return False
        
        # Check for build job
        if 'build' not in workflow_content['jobs']:
            print("❌ Build job not found in workflow")
            return False
        
        print("✅ GitHub workflow file verified successfully")
        return True
        
    except yaml.YAMLError as e:
        print(f"❌ Error parsing workflow YAML: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading workflow file: {e}")
        return False

def check_required_files():
    """Check if required files for the workflow exist."""
    required_files = [
        ('requirements.txt', 'Runtime dependencies'),
        ('requirements-dev.txt', 'Development dependencies'),
        ('src/bridge_gad/cli.py', 'CLI entry point'),
        ('src/bridge_gad/gui.py', 'GUI entry point'),
        ('Bridge_GAD_Installer.iss', 'Inno Setup installer script')
    ]
    
    missing_files = []
    for filename, description in required_files:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(filepath):
            missing_files.append((filename, description))
    
    if missing_files:
        print("❌ Missing required files for workflow:")
        for filename, description in missing_files:
            print(f"   - {filename}: {description}")
        return False
    
    print("✅ All required files for workflow are present")
    return True

def main():
    print("Verifying GitHub release workflow...")
    print("=" * 40)
    
    checks = [
        check_workflow_file,
        check_required_files
    ]
    
    results = []
    for check in checks:
        results.append(check())
        print()
    
    print("=" * 40)
    if all(results):
        print("✅ GitHub release workflow is ready!")
        print("You can now push a tag to trigger an automatic release.")
        print("\nTo create and push a tag:")
        print("  git tag v1.1.0")
        print("  git push origin v1.1.0")
    else:
        print("❌ GitHub release workflow has issues.")
        print("Please address the issues listed above.")
    
    return all(results)

if __name__ == "__main__":
    main()