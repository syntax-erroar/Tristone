#!/usr/bin/env python3
"""
Test resending OTP for email verification
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_resend_otp():
    """Test resending OTP"""
    print("Testing OTP resend...")
    
    data = {
        "email": "nishit.wadhwani@tristone-partners.com"
    }
    
    try:
        response = requests.post(f'{BASE_URL}/api/auth/resend-otp', json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json().get('success', False)
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("=" * 50)
    print("TRISTONE PARTNERS OTP RESEND TEST")
    print("=" * 50)
    
    if test_resend_otp():
        print("OK: OTP sent successfully!")
        print("Check your email: nishit.wadhwani@tristone-partners.com")
    else:
        print("ERROR: Failed to send OTP")

if __name__ == '__main__':
    main()
