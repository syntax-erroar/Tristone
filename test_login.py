#!/usr/bin/env python3
"""
Test login for existing user
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_login():
    """Test user login"""
    print("Testing user login...")
    
    data = {
        "email": "nishit.wadhwani@tristone-partners.com",
        "password": "TestPassword123!"
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/login', json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json().get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 50)
    print("TRISTONE PARTNERS LOGIN TEST")
    print("=" * 50)
    
    if test_login():
        print("OK: Login successful!")
    else:
        print("INFO: Login failed - user may need to verify email first")
        print("Please check your email for OTP verification")

if __name__ == '__main__':
    main()
