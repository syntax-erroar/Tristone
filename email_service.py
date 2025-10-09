#!/usr/bin/env python3
"""
Free Email Service Integration for Tristone Partners
Supports multiple free email services for OTP verification
"""

import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self):
        self.service_type = os.getenv('EMAIL_SERVICE', 'brevo')  # Default to Brevo
        
    def send_otp_email(self, to_email, otp_code, first_name):
        """Send OTP email using the configured service"""
        
        if self.service_type == 'brevo':
            return self._send_via_brevo(to_email, otp_code, first_name)
        elif self.service_type == 'gmail':
            return self._send_via_gmail(to_email, otp_code, first_name)
        elif self.service_type == 'resend':
            return self._send_via_resend(to_email, otp_code, first_name)
        else:
            return self._send_via_brevo(to_email, otp_code, first_name)  # Default
    
    def _send_via_brevo(self, to_email, otp_code, first_name):
        """Send email via Brevo (Sendinblue) - 300 emails/day free"""
        
        api_key = os.getenv('BREVO_API_KEY')
        if not api_key:
            print("Warning: BREVO_API_KEY not set, using demo mode")
            # For demo purposes, we'll simulate success
            print(f"Demo: Would send OTP {otp_code} to {to_email}")
            return True
        
        url = "https://api.brevo.com/v3/smtp/email"
        
        headers = {
            "accept": "application/json",
            "api-key": api_key,
            "content-type": "application/json"
        }
        
        html_content = self._create_otp_email_html(otp_code, first_name)
        
        payload = {
            "sender": {
                "name": "Tristone Partners",
                "email": "noreply@tristone-partners.com"
            },
            "to": [
                {
                    "email": to_email,
                    "name": first_name
                }
            ],
            "subject": "Tristone Partners - Email Verification Code",
            "htmlContent": html_content
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 201:
                print(f"✅ Email sent successfully via Brevo to {to_email}")
                return True
            else:
                print(f"❌ Brevo API error: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Brevo email sending failed: {e}")
            return False
    
    def _send_via_gmail(self, to_email, otp_code, first_name):
        """Send email via Gmail with app password"""
        
        gmail_user = os.getenv('GMAIL_USER')
        gmail_password = os.getenv('GMAIL_APP_PASSWORD')
        
        if not gmail_user or not gmail_password:
            print("Warning: Gmail credentials not set")
            return False
        
        try:
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = to_email
            msg['Subject'] = "Tristone Partners - Email Verification Code"
            
            html_content = self._create_otp_email_html(otp_code, first_name)
            msg.attach(MIMEText(html_content, 'html'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            
            text = msg.as_string()
            server.sendmail(gmail_user, to_email, text)
            server.quit()
            
            print(f"✅ Email sent successfully via Gmail to {to_email}")
            return True
            
        except Exception as e:
            print(f"❌ Gmail email sending failed: {e}")
            return False
    
    def _send_via_resend(self, to_email, otp_code, first_name):
        """Send email via Resend - 3000 emails/month free"""
        
        api_key = os.getenv('RESEND_API_KEY')
        if not api_key:
            print("Warning: RESEND_API_KEY not set")
            return False
        
        url = "https://api.resend.com/emails"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        html_content = self._create_otp_email_html(otp_code, first_name)
        
        payload = {
            "from": "Tristone Partners <noreply@tristone-partners.com>",
            "to": [to_email],
            "subject": "Tristone Partners - Email Verification Code",
            "html": html_content
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"✅ Email sent successfully via Resend to {to_email}")
                return True
            else:
                print(f"❌ Resend API error: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Resend email sending failed: {e}")
            return False
    
    def _create_otp_email_html(self, otp_code, first_name):
        """Create beautiful HTML email template"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: 'Arial', sans-serif; margin: 0; padding: 0; background-color: #f0fdf4; }}
                .container {{ max-width: 600px; margin: 0 auto; background-color: #ffffff; }}
                .header {{ background: linear-gradient(135deg, #10B981 0%, #059669 100%); padding: 2rem; text-align: center; }}
                .logo {{ width: 60px; height: 60px; background-color: rgba(255,255,255,0.2); border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1rem; }}
                .logo-text {{ color: white; font-size: 1.5rem; font-weight: bold; }}
                .header h1 {{ color: white; margin: 0; font-size: 1.5rem; }}
                .content {{ padding: 2rem; }}
                .otp-box {{ background-color: #f0fdf4; border: 2px solid #10B981; border-radius: 8px; padding: 1.5rem; text-align: center; margin: 1.5rem 0; }}
                .otp-code {{ font-size: 2rem; font-weight: bold; color: #064E3B; letter-spacing: 0.5rem; font-family: 'Courier New', monospace; }}
                .footer {{ background-color: #f9fafb; padding: 1rem; text-align: center; font-size: 0.875rem; color: #6b7280; }}
                .button {{ display: inline-block; background: #10B981; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; margin: 1rem 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <div class="logo">
                        <span class="logo-text">TP</span>
                    </div>
                    <h1>Tristone Partners</h1>
                </div>
                <div class="content">
                    <h2>Email Verification</h2>
                    <p>Hello {first_name},</p>
                    <p>Welcome to Tristone Partners! Please use the following verification code to complete your account setup:</p>
                    
                    <div class="otp-box">
                        <div class="otp-code">{otp_code}</div>
                    </div>
                    
                    <p>This code will expire in 10 minutes for security purposes.</p>
                    <p>If you didn't request this verification, please ignore this email.</p>
                    
                    <p>Best regards,<br>The Tristone Partners Team</p>
                </div>
                <div class="footer">
                    <p>© 2024 Tristone Partners. All rights reserved.</p>
                    <p>This is an automated message, please do not reply to this email.</p>
                </div>
            </div>
        </body>
        </html>
        """

# Demo mode for testing without API keys
def demo_email_service():
    """Demo email service that simulates sending emails"""
    print("🎯 DEMO MODE: Email service running in demo mode")
    print("In production, this would send real emails via Brevo/Gmail/Resend")
    return True
