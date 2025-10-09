#!/usr/bin/env python3
"""
Test script to verify Phone.Email button is visible and working
"""

import requests
import time

def test_phone_email_button():
    """Test if Phone.Email button is visible in the app"""
    print("Testing Phone.Email button visibility...")
    
    try:
        # Test the main page
        response = requests.get('http://localhost:8501', timeout=10)
        
        if response.status_code == 200:
            content = response.text
            
            # Check for Phone.Email elements
            phone_email_checks = [
                "Sign in with Email",
                "pe_verify_email",
                "phone.email/verify_email_v1.js",
                "data-client-id",
                "phoneEmailReceiver"
            ]
            
            found_elements = []
            for check in phone_email_checks:
                if check in content:
                    found_elements.append(check)
                    print(f"✓ Found: {check}")
                else:
                    print(f"✗ Missing: {check}")
            
            if len(found_elements) >= 3:
                print("\n✅ Phone.Email button should be visible!")
                print("Open http://localhost:8501 in your browser to see it.")
            else:
                print("\n❌ Phone.Email button elements not found")
                
        else:
            print(f"❌ App not responding: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error testing app: {e}")

if __name__ == "__main__":
    test_phone_email_button()
