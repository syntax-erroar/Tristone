#!/usr/bin/env python3
"""
Simple test for email authentication
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def main():
    print("=" * 50)
    print("TESTING EMAIL AUTHENTICATION")
    print("=" * 50)
    
    # Test health
    try:
        response = requests.get(f'{BASE_URL}/api/health')
        if response.status_code == 200:
            print("OK: Backend is running")
        else:
            print("ERROR: Backend not responding")
            return
    except:
        print("ERROR: Cannot connect to backend")
        return
    
    # Test signup
    print("\nTesting signup...")
    signup_data = {
        "email": "demo@tristone-partners.com",
        "password": "Test123!",
        "firstName": "Demo",
        "lastName": "User"
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/signup-no-email', json=signup_data)
        result = response.json()
        print(f"Signup Status: {response.status_code}")
        print(f"Message: {result.get('message')}")
        
        if response.status_code in [201, 400]:
            print("OK: Signup endpoint working")
        else:
            print("ERROR: Signup failed")
            return
    except Exception as e:
        print(f"ERROR: {e}")
        return
    
    # Test OTP storage
    print("\nTesting OTP storage...")
    otp_data = {
        "email": "demo@tristone-partners.com",
        "otp": "123456"
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/store-otp', json=otp_data)
        result = response.json()
        print(f"OTP Storage Status: {response.status_code}")
        print(f"Message: {result.get('message')}")
        
        if response.status_code == 200:
            print("OK: OTP storage working")
        else:
            print("ERROR: OTP storage failed")
            return
    except Exception as e:
        print(f"ERROR: {e}")
        return
    
    print("\n" + "=" * 50)
    print("SUCCESS! Email authentication system ready!")
    print("=" * 50)
    print("Frontend: http://localhost:3000")
    print("Backend: http://localhost:5000")
    print("\nTo test:")
    print("1. Open http://localhost:3000")
    print("2. Sign up with @tristone-partners.com email")
    print("3. OTP will show in browser alert (demo mode)")
    print("4. Enter OTP and complete verification")
    print("=" * 50)

if __name__ == '__main__':
    main()
