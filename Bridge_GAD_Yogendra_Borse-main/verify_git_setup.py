#!/usr/bin/env python3
"""
Verification script for Git setup.
"""

import os
import subprocess
import sys

def check_git_availability():
    """Check if Git is available."""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True, check=True)
        print(f"✅ Git is available: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not available. Please install Git and add it to your PATH.")
        return False

def check_git_repository():
    """Check if current directory is a Git repository."""
    try:
        result = subprocess.run(['git', 'rev-parse', '--git-dir'], capture_output=True, text=True, check=True)
        print(f"✅ Current directory is a Git repository")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Current directory is not a Git repository")
        return False

def check_git_status():
    """Check Git repository status."""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, check=True)
        if result.stdout.strip():
            print("⚠️  Repository has uncommitted changes:")
            print(result.stdout)
            return False
        else:
            print("✅ Repository is clean (no uncommitted changes)")
            return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Unable to check repository status")
        return False

def check_remote_origin():
    """Check if remote origin is configured."""
    try:
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True, check=True)
        print(f"✅ Remote origin is configured: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Remote origin is not configured")
        return False

def extract_version():
    """Extract version from __init__.py."""
    init_path = os.path.join(os.path.dirname(__file__), 'src', 'bridge_gad', '__init__.py')
    if os.path.exists(init_path):
        with open(init_path, 'r') as f:
            content = f.read()
            if '__version__' in content:
                version_line = [line for line in content.split('\n') if '__version__' in line][0]
                version = version_line.split('=')[1].strip().strip('"')
                print(f"✅ Package version: {version}")
                return version
    print("❌ Unable to extract version from __init__.py")
    return None

def main():
    print("Verifying Git setup for Bridge_GAD...")
    print("=" * 40)
    
    checks = [
        check_git_availability,
        check_git_repository,
        check_git_status,
        check_remote_origin,
        extract_version
    ]
    
    results = []
    for check in checks:
        results.append(check())
        print()
    
    print("=" * 40)
    if all(results[:-1]):  # All checks except version extraction
        version = results[-1]  # Version extraction result
        if version:
            print(f"✅ Git setup is ready for tagging v{version}")
            print("You can now run create_git_tag.bat to create and push the tag")
        else:
            print("❌ Git setup is ready but version could not be extracted")
    else:
        print("❌ Git setup is not ready for tagging")
        print("Please address the issues listed above")
    
    return all(results[:-1]) and results[-1]

if __name__ == "__main__":
    main()