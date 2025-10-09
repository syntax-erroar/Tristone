#!/usr/bin/env python3
"""
Tristone Partners Dashboard Startup Script
This script helps set up and run the complete application
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_banner():
    """Print application banner"""
    print("=" * 60)
    print("TRISTONE PARTNERS DASHBOARD")
    print("=" * 60)
    print("Modern SEC Tools with Authentication & OTP Verification")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("ERROR: Python 3.7 or higher is required")
        sys.exit(1)
    print(f"OK: Python {sys.version.split()[0]} detected")

def check_node_installed():
    """Check if Node.js is installed"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"OK: Node.js {result.stdout.strip()} detected")
            return True
    except FileNotFoundError:
        pass
    
    print("ERROR: Node.js not found. Please install Node.js from https://nodejs.org/")
    return False

def install_python_dependencies():
    """Install Python dependencies"""
    print("\nInstalling Python dependencies...")
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("OK: Python dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to install Python dependencies: {e}")
        return False

def install_node_dependencies():
    """Install Node.js dependencies"""
    print("\n📦 Installing Node.js dependencies...")
    try:
        subprocess.run(['npm', 'install'], check=True, capture_output=True)
        print("✅ Node.js dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Node.js dependencies: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path('.env')
    if not env_file.exists():
        print("\n⚙️  Creating .env file...")
        env_content = """# Tristone Partners Dashboard Configuration
SECRET_KEY=tristone-partners-secret-key-2024-change-in-production
FLASK_ENV=development

# Email Configuration (Required for OTP functionality)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=noreply@tristone-partners.com

# Database
DATABASE=tristone_auth.db
"""
        env_file.write_text(env_content)
        print("✅ .env file created")
        print("⚠️  Please update the email settings in .env file for OTP functionality")
    else:
        print("✅ .env file already exists")

def run_backend():
    """Start the Flask backend server"""
    print("\n🚀 Starting Flask backend server...")
    try:
        # Run backend in background
        process = subprocess.Popen([sys.executable, 'backend_app.py'])
        print("✅ Backend server started on http://localhost:5000")
        return process
    except Exception as e:
        print(f"❌ Failed to start backend server: {e}")
        return None

def run_frontend():
    """Start the React frontend server"""
    print("\n🚀 Starting React frontend server...")
    try:
        # This will run in foreground
        subprocess.run(['npm', 'start'], check=True)
    except KeyboardInterrupt:
        print("\n👋 Shutting down frontend server...")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start frontend server: {e}")

def main():
    """Main setup and run function"""
    print_banner()
    
    # Check system requirements
    check_python_version()
    if not check_node_installed():
        sys.exit(1)
    
    # Install dependencies
    if not install_python_dependencies():
        sys.exit(1)
    
    if not install_node_dependencies():
        sys.exit(1)
    
    # Create configuration
    create_env_file()
    
    print("\n" + "=" * 60)
    print("🎉 SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("📋 NEXT STEPS:")
    print("1. Update email settings in .env file for OTP functionality")
    print("2. The application will start automatically")
    print("3. Backend API: http://localhost:5000")
    print("4. Frontend App: http://localhost:3000")
    print()
    print("📧 EMAIL SETUP GUIDE:")
    print("For Gmail:")
    print("- Enable 2-factor authentication")
    print("- Generate App Password in Google Account settings")
    print("- Use the app password in SMTP_PASSWORD")
    print()
    print("🔐 TEST ACCOUNTS:")
    print("- Use any email ending with @tristone-partners.com")
    print("- Example: john.doe@tristone-partners.com")
    print()
    
    input("Press Enter to start the servers...")
    
    # Start backend
    backend_process = run_backend()
    if not backend_process:
        sys.exit(1)
    
    # Wait a moment for backend to start
    time.sleep(3)
    
    try:
        # Start frontend (this will block)
        run_frontend()
    finally:
        # Clean up backend process
        if backend_process:
            print("\n🛑 Stopping backend server...")
            backend_process.terminate()
            backend_process.wait()
    
    print("\n👋 Application stopped. Thank you for using Tristone Partners Dashboard!")

if __name__ == '__main__':
    main()
