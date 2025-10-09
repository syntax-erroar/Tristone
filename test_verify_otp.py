#!/usr/bin/env python3
"""
Test OTP verification with manual input
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_verify_otp(otp_code):
    """Test OTP verification"""
    print(f"Testing OTP verification with code: {otp_code}")
    
    data = {
        "email": "nishit.wadhwani@tristone-partners.com",
        "otp": otp_code
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/verify-otp', json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json().get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 50)
    print("TRISTONE PARTNERS OTP VERIFICATION TEST")
    print("=" * 50)
    
    # For testing purposes, let's try a sample OTP
    # In real usage, you'd get this from your email
    test_otp = input("Enter the 6-digit OTP code (or press Enter to skip): ").strip()
    
    if test_otp and len(test_otp) == 6:
        if test_verify_otp(test_otp):
            print("OK: Email verified successfully!")
            print("You can now log in to the system.")
        else:
            print("ERROR: OTP verification failed")
            print("The code may be invalid or expired.")
    else:
        print("INFO: Skipping OTP verification test")
        print("To verify your email, you'll need the 6-digit code sent to your email.")

if __name__ == '__main__':
    main()
