#!/usr/bin/env python3
"""
Simple setup and run script for Tristone Partners Dashboard
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def main():
    print("=" * 60)
    print("TRISTONE PARTNERS DASHBOARD")
    print("=" * 60)
    print("Setting up authentication system with OTP verification...")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("ERROR: Python 3.7 or higher is required")
        sys.exit(1)
    print(f"OK: Python {sys.version.split()[0]} detected")
    
    # Install Python dependencies
    print("\nInstalling Python dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True)
        print("OK: Python dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to install Python dependencies: {e}")
        sys.exit(1)
    
    # Create .env file if needed
    env_file = Path('.env')
    if not env_file.exists():
        print("\nCreating .env configuration file...")
        env_content = """SECRET_KEY=tristone-partners-secret-key-2024
FLASK_ENV=development
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@tristone-partners.com
"""
        env_file.write_text(env_content)
        print("OK: .env file created")
    
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print("\nIMPORTANT: Update email settings in .env file for OTP functionality")
    print("\nFor Gmail:")
    print("1. Enable 2-factor authentication")
    print("2. Generate App Password in Google Account settings")
    print("3. Update SMTP_USERNAME and SMTP_PASSWORD in .env")
    print("\nStarting backend server...")
    
    # Start backend
    try:
        subprocess.run([sys.executable, 'backend_app.py'])
    except KeyboardInterrupt:
        print("\nShutting down...")

if __name__ == '__main__':
    main()
