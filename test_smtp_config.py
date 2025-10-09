#!/usr/bin/env python3
"""
Test different SMTP configurations for company email
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_smtp_config(server, port, username, password, test_email):
    """Test SMTP configuration"""
    print(f"Testing SMTP: {server}:{port}")
    
    try:
        # Create test message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = test_email
        msg['Subject'] = "Tristone Partners - SMTP Test"
        
        body = "This is a test email from Tristone Partners authentication system."
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to server
        server_obj = smtplib.SMTP(server, port)
        server_obj.starttls()  # Enable encryption
        server_obj.login(username, password)
        
        # Send test email
        text = msg.as_string()
        server_obj.sendmail(username, test_email, text)
        server_obj.quit()
        
        print(f"✅ SUCCESS: {server}:{port} works!")
        return True
        
    except Exception as e:
        print(f"❌ FAILED: {server}:{port} - {str(e)}")
        return False

def main():
    print("=" * 60)
    print("TRISTONE PARTNERS SMTP CONFIGURATION TEST")
    print("=" * 60)
    
    username = "nishit.wadhwani@tristone-partners.com"
    password = "Wad84025"
    test_email = username  # Send test email to yourself
    
    # List of common SMTP configurations to try
    smtp_configs = [
        ("smtp.office365.com", 587),  # Microsoft Office 365
        ("smtp.gmail.com", 587),      # Google Workspace
        ("mail.tristone-partners.com", 587),  # Custom company server
        ("smtp.office365.com", 25),   # Alternative port
        ("smtp.gmail.com", 465),      # Gmail SSL port
    ]
    
    print(f"Testing email configurations for: {username}")
    print(f"Test email will be sent to: {test_email}")
    print()
    
    working_configs = []
    
    for server, port in smtp_configs:
        if test_smtp_config(server, port, username, password, test_email):
            working_configs.append((server, port))
        print()
    
    print("=" * 60)
    print("RESULTS:")
    print("=" * 60)
    
    if working_configs:
        print("✅ Working SMTP configurations:")
        for server, port in working_configs:
            print(f"   - {server}:{port}")
        print()
        print("Update your config.env file with one of the working configurations.")
    else:
        print("❌ No working SMTP configurations found.")
        print()
        print("Possible solutions:")
        print("1. Contact your IT department for correct SMTP settings")
        print("2. Check if your password needs to be an 'App Password'")
        print("3. Verify if multi-factor authentication is required")
        print("4. Check if external SMTP access is blocked by company policy")

if __name__ == '__main__':
    main()
