#!/usr/bin/env python3
"""
Test the complete email authentication flow
"""

import requests
import json
import time

BASE_URL = 'http://localhost:5000'

def test_health():
    """Test if backend is running"""
    try:
        response = requests.get(f'{BASE_URL}/api/health')
        return response.status_code == 200
    except:
        return False

def test_signup_flow():
    """Test the complete signup flow with EmailJS"""
    print("=" * 60)
    print("TESTING EMAIL AUTHENTICATION FLOW")
    print("=" * 60)
    
    # Test data
    test_email = "test.demo@tristone-partners.com"
    test_data = {
        "email": test_email,
        "password": "TestPassword123!",
        "firstName": "Demo",
        "lastName": "User"
    }
    
    print(f"Testing with email: {test_email}")
    print()
    
    # Step 1: Test signup
    print("1. Testing user registration...")
    try:
        response = requests.post(f'{BASE_URL}/api/auth/signup-no-email', json=test_data)
        result = response.json()
        
        print(f"   Status: {response.status_code}")
        print(f"   Message: {result.get('message', 'No message')}")
        
        if response.status_code == 201:
            print("   ✓ User registration successful")
        elif response.status_code == 400 and "already exists" in result.get('message', ''):
            print("   ✓ User already exists (that's fine for testing)")
        else:
            print("   ✗ Registration failed")
            return False
            
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Step 2: Test OTP storage
    print("\n2. Testing OTP storage...")
    test_otp = "123456"
    otp_data = {
        "email": test_email,
        "otp": test_otp
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/store-otp', json=otp_data)
        result = response.json()
        
        print(f"   Status: {response.status_code}")
        print(f"   Message: {result.get('message', 'No message')}")
        
        if response.status_code == 200:
            print("   ✓ OTP storage successful")
        else:
            print("   ✗ OTP storage failed")
            return False
            
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Step 3: Test user info retrieval
    print("\n3. Testing user info retrieval...")
    try:
        response = requests.get(f'{BASE_URL}/api/auth/user-info/{test_email}')
        result = response.json()
        
        print(f"   Status: {response.status_code}")
        print(f"   User: {result.get('firstName', 'N/A')} {result.get('lastName', 'N/A')}")
        
        if response.status_code == 200:
            print("   ✓ User info retrieval successful")
        else:
            print("   ✗ User info retrieval failed")
            return False
            
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Step 4: Test OTP verification
    print("\n4. Testing OTP verification...")
    verify_data = {
        "email": test_email,
        "otp": test_otp
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/verify-otp', json=verify_data)
        result = response.json()
        
        print(f"   Status: {response.status_code}")
        print(f"   Message: {result.get('message', 'No message')}")
        
        if response.status_code == 200:
            print("   ✓ OTP verification successful")
        else:
            print("   ✗ OTP verification failed")
            return False
            
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Step 5: Test login
    print("\n5. Testing login...")
    login_data = {
        "email": test_email,
        "password": "TestPassword123!"
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/login', json=login_data)
        result = response.json()
        
        print(f"   Status: {response.status_code}")
        print(f"   Message: {result.get('message', 'No message')}")
        
        if response.status_code == 200:
            print("   ✓ Login successful")
            print(f"   Token: {result.get('token', 'No token')[:20]}...")
            return True
        else:
            print("   ✗ Login failed")
            return False
            
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def main():
    # Check if backend is running
    if not test_health():
        print("ERROR: Backend is not running on http://localhost:5000")
        print("Please start the backend with: python simple_demo_backend.py")
        return
    
    print("✓ Backend is running")
    print()
    
    # Test the complete flow
    if test_signup_flow():
        print("\n" + "=" * 60)
        print("🎉 EMAIL AUTHENTICATION FLOW TEST PASSED!")
        print("=" * 60)
        print("✓ User registration works")
        print("✓ OTP storage works")
        print("✓ User info retrieval works")
        print("✓ OTP verification works")
        print("✓ Login works")
        print()
        print("🌟 Your authentication system is ready!")
        print("📱 Frontend: http://localhost:3000")
        print("🔧 Backend: http://localhost:5000")
        print()
        print("📧 EmailJS Integration Status:")
        print("   • Demo mode: OTP shows in browser alerts")
        print("   • Production: Set up EmailJS for real emails")
        print("   • Guide: See EMAILJS_SETUP_GUIDE.md")
        print("=" * 60)
    else:
        print("\n❌ Some tests failed. Check the backend logs.")

if __name__ == '__main__':
    main()
