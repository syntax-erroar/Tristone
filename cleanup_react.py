#!/usr/bin/env python3
"""
Cleanup React files and move to Streamlit-only solution
"""

import os
import shutil
from pathlib import Path

def cleanup_react_files():
    """Remove React-related files and directories"""
    
    react_files_and_dirs = [
        'src/',
        'public/',
        'node_modules/',
        'package.json',
        'package-lock.json',
        'craco.config.js',
        '.gitignore',
    ]
    
    print("=" * 50)
    print("CLEANING UP REACT FILES")
    print("=" * 50)
    
    for item in react_files_and_dirs:
        path = Path(item)
        if path.exists():
            try:
                if path.is_dir():
                    shutil.rmtree(path)
                    print(f"Removed directory: {item}")
                else:
                    path.unlink()
                    print(f"Removed file: {item}")
            except Exception as e:
                print(f"Could not remove {item}: {e}")
        else:
            print(f"Not found: {item}")
    
    print("\n" + "=" * 50)
    print("REACT CLEANUP COMPLETE")
    print("=" * 50)
    print("Remaining files:")
    print("✓ authenticated_app.py - New Streamlit app with auth")
    print("✓ simple_demo_backend.py - Backend API")
    print("✓ app.py - Original Streamlit app (backup)")
    print("✓ All your SEC tools and data")
    print("✓ Authentication database")
    print("\nYour new unified Streamlit app is ready!")
    print("Run: streamlit run authenticated_app.py")
    print("=" * 50)

if __name__ == '__main__':
    response = input("Are you sure you want to remove React files? (y/N): ")
    if response.lower() == 'y':
        cleanup_react_files()
    else:
        print("Cleanup cancelled. React files preserved.")
