#!/usr/bin/env python3
"""
Script to clean up redundant files from the repository
"""

import os
import shutil
import glob
from pathlib import Path

def remove_pycache_dirs():
    """Remove all __pycache__ directories"""
    print("Removing __pycache__ directories...")
    removed_count = 0
    
    for root, dirs, files in os.walk("."):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"  Removed: {pycache_path}")
                removed_count += 1
            except Exception as e:
                print(f"  Error removing {pycache_path}: {e}")
    
    print(f"Removed {removed_count} __pycache__ directories")
    return removed_count

def remove_pyc_files():
    """Remove all .pyc files"""
    print("\nRemoving .pyc files...")
    removed_count = 0
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(root, file)
                try:
                    os.remove(pyc_path)
                    print(f"  Removed: {pyc_path}")
                    removed_count += 1
                except Exception as e:
                    print(f"  Error removing {pyc_path}: {e}")
    
    print(f"Removed {removed_count} .pyc files")
    return removed_count

def remove_build_artifacts():
    """Remove build artifacts and executables"""
    print("\nRemoving build artifacts...")
    removed_count = 0
    
    # Remove dist directory
    dist_path = "dist"
    if os.path.exists(dist_path):
        try:
            shutil.rmtree(dist_path)
            print(f"  Removed: {dist_path}/")
            removed_count += 1
        except Exception as e:
            print(f"  Error removing {dist_path}: {e}")
    
    # Remove build directory
    build_path = "build"
    if os.path.exists(build_path):
        try:
            shutil.rmtree(build_path)
            print(f"  Removed: {build_path}/")
            removed_count += 1
        except Exception as e:
            print(f"  Error removing {build_path}: {e}")
    
    # Remove .exe files in root directory
    exe_files = glob.glob("*.exe")
    for exe_file in exe_files:
        try:
            os.remove(exe_file)
            print(f"  Removed: {exe_file}")
            removed_count += 1
        except Exception as e:
            print(f"  Error removing {exe_file}: {e}")
    
    # Remove .pkg files in root directory
    pkg_files = glob.glob("*.pkg")
    for pkg_file in pkg_files:
        try:
            os.remove(pkg_file)
            print(f"  Removed: {pkg_file}")
            removed_count += 1
        except Exception as e:
            print(f"  Error removing {pkg_file}: {e}")
    
    print(f"Removed {removed_count} build artifacts")
    return removed_count

def remove_temp_files():
    """Remove temporary files"""
    print("\nRemoving temporary files...")
    removed_count = 0
    
    # Patterns to remove
    temp_patterns = [
        "*.tmp",
        "*.bak",
        "*.log",
        "*.old",
        "*.temp"
    ]
    
    for pattern in temp_patterns:
        files = glob.glob(pattern, recursive=True)
        for file in files:
            try:
                os.remove(file)
                print(f"  Removed: {file}")
                removed_count += 1
            except Exception as e:
                print(f"  Error removing {file}: {e}")
    
    print(f"Removed {removed_count} temporary files")
    return removed_count

def preserve_essential_files():
    """List files that should be preserved"""
    print("\nEssential files preserved:")
    print("  - Attached_Folder/ (if exists)")
    print("  - Test_Files/ (if exists)")
    print("  - README.md and similar instructional files")
    print("  - Core application files")
    print("  - Configuration files")
    print("  - Requirements files")

def main():
    """Main cleanup function"""
    print("PWD Tools Repository Cleanup")
    print("=" * 40)
    
    # Confirm with user
    response = input("This will remove redundant files. Continue? (y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("Cleanup cancelled.")
        return
    
    # Perform cleanup
    total_removed = 0
    total_removed += remove_pycache_dirs()
    total_removed += remove_pyc_files()
    total_removed += remove_build_artifacts()
    total_removed += remove_temp_files()
    
    # Show preserved files
    preserve_essential_files()
    
    print(f"\nCleanup completed. Total files/directories removed: {total_removed}")
    print("Run 'git status' to see remaining files.")

if __name__ == "__main__":
    main()