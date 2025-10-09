#!/usr/bin/env python3
"""
Test script for Tristone Partners authentication system
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_signup():
    """Test user registration"""
    print("Testing user registration...")
    
    data = {
        "email": "nishit.wadhwani@tristone-partners.com",
        "password": "TestPassword123!",
        "firstName": "Nishit",
        "lastName": "Wadhwani"
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/signup', json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json().get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_health():
    """Test API health"""
    print("Testing API health...")
    
    try:
        response = requests.get(f'{BASE_URL}/api/health')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 50)
    print("TRISTONE PARTNERS AUTH SYSTEM TEST")
    print("=" * 50)
    
    # Test health first
    if not test_health():
        print("ERROR: Backend is not running or not responding")
        return
    
    print("OK: Backend is running")
    print()
    
    # Test signup
    if test_signup():
        print("OK: Registration successful! Check your email for OTP.")
    else:
        print("ERROR: Registration failed")

if __name__ == '__main__':
    main()
