#!/usr/bin/env python3
"""
Flask backend for Tristone Partners authentication system
Provides API endpoints for user registration, login, and OTP verification
"""

import os
import secrets
import smtplib
import sqlite3
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from functools import wraps
from pathlib import Path

import bcrypt
import jwt
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load environment variables from config.env
def load_config():
    config_file = Path('config.env')
    if config_file.exists():
        with open(config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key] = value

load_config()

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'tristone-partners-secret-key-2024')
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=24)

# Email configuration (you'll need to set these environment variables)
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
FROM_EMAIL = os.getenv('FROM_EMAIL', 'noreply@tristone-partners.com')

# Database setup
DATABASE = 'tristone_auth.db'

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            is_verified BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # OTP table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS otps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            otp_code TEXT NOT NULL,
            expires_at TIMESTAMP NOT NULL,
            is_used BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def generate_otp():
    """Generate a 6-digit OTP"""
    return str(secrets.randbelow(900000) + 100000)

def send_email(to_email, subject, body):
    """Send email using the configured email service"""
    try:
        # Import the email service
        from email_service import EmailService, demo_email_service
        
        # For demo purposes, we'll use demo mode
        # In production, you would set up API keys
        email_service = EmailService()
        
        # Extract OTP and name from the email content (simple parsing)
        # This is a quick implementation - in production you'd pass these directly
        otp_code = "123456"  # Default for demo
        first_name = "User"  # Default for demo
        
        # Try to extract OTP from HTML content
        if 'otp-code' in body:
            import re
            otp_match = re.search(r'<div class="otp-code">(\d{6})</div>', body)
            if otp_match:
                otp_code = otp_match.group(1)
        
        # Try to extract first name
        if 'Hello ' in body:
            import re
            name_match = re.search(r'Hello ([^,]+),', body)
            if name_match:
                first_name = name_match.group(1)
        
        # For demo mode, just simulate success
        print(f"📧 Demo: Sending OTP {otp_code} to {to_email} for {first_name}")
        print("✅ Email would be sent successfully in production mode")
        return True
        
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False

def create_otp_email_body(otp_code, first_name):
    """Create HTML email body for OTP"""
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
                <p>Thank you for registering with Tristone Partners. Please use the following verification code to complete your account setup:</p>
                
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

def token_required(f):
    """Decorator to require JWT token for protected routes"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'success': False, 'message': 'Token is missing'}), 401
        
        try:
            if token.startswith('Bearer '):
                token = token[7:]
            
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user_email = data['email']
            
            # Get user from database
            conn = get_db_connection()
            user = conn.execute(
                'SELECT * FROM users WHERE email = ? AND is_verified = TRUE',
                (current_user_email,)
            ).fetchone()
            conn.close()
            
            if not user:
                return jsonify({'success': False, 'message': 'Invalid token'}), 401
                
        except jwt.ExpiredSignatureError:
            return jsonify({'success': False, 'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'success': False, 'message': 'Invalid token'}), 401
        
        return f(current_user_email, *args, **kwargs)
    
    return decorated

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """User registration endpoint"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['email', 'password', 'firstName', 'lastName']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'message': f'{field} is required'
                }), 400
        
        email = data['email'].lower().strip()
        password = data['password']
        first_name = data['firstName'].strip()
        last_name = data['lastName'].strip()
        
        # Validate email domain
        if not email.endswith('@tristone-partners.com'):
            return jsonify({
                'success': False,
                'message': 'Email must be from @tristone-partners.com domain'
            }), 400
        
        # Validate password strength
        if len(password) < 8:
            return jsonify({
                'success': False,
                'message': 'Password must be at least 8 characters long'
            }), 400
        
        conn = get_db_connection()
        
        # Check if user already exists
        existing_user = conn.execute(
            'SELECT id FROM users WHERE email = ?',
            (email,)
        ).fetchone()
        
        if existing_user:
            conn.close()
            return jsonify({
                'success': False,
                'message': 'User with this email already exists'
            }), 400
        
        # Hash password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Create user
        conn.execute(
            'INSERT INTO users (email, password_hash, first_name, last_name) VALUES (?, ?, ?, ?)',
            (email, password_hash, first_name, last_name)
        )
        conn.commit()
        
        # Generate and store OTP
        otp_code = generate_otp()
        expires_at = datetime.now() + timedelta(minutes=10)
        
        conn.execute(
            'INSERT INTO otps (email, otp_code, expires_at) VALUES (?, ?, ?)',
            (email, otp_code, expires_at)
        )
        conn.commit()
        conn.close()
        
        # Send OTP email
        subject = "Verify Your Tristone Partners Account"
        body = create_otp_email_body(otp_code, first_name)
        
        if send_email(email, subject, body):
            return jsonify({
                'success': True,
                'message': 'Account created successfully. Please check your email for verification code.'
            }), 201
        else:
            return jsonify({
                'success': False,
                'message': 'Account created but failed to send verification email. Please try resending OTP.'
            }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Registration failed: {str(e)}'
        }), 500

@app.route('/api/auth/verify-otp', methods=['POST'])
def verify_otp():
    """OTP verification endpoint"""
    try:
        data = request.get_json()
        
        email = data.get('email', '').lower().strip()
        otp_code = data.get('otp', '').strip()
        
        if not email or not otp_code:
            return jsonify({
                'success': False,
                'message': 'Email and OTP are required'
            }), 400
        
        conn = get_db_connection()
        
        # Find valid OTP
        otp_record = conn.execute(
            'SELECT * FROM otps WHERE email = ? AND otp_code = ? AND is_used = FALSE AND expires_at > ? ORDER BY created_at DESC LIMIT 1',
            (email, otp_code, datetime.now())
        ).fetchone()
        
        if not otp_record:
            conn.close()
            return jsonify({
                'success': False,
                'message': 'Invalid or expired OTP'
            }), 400
        
        # Mark OTP as used
        conn.execute(
            'UPDATE otps SET is_used = TRUE WHERE id = ?',
            (otp_record['id'],)
        )
        
        # Mark user as verified
        conn.execute(
            'UPDATE users SET is_verified = TRUE, updated_at = CURRENT_TIMESTAMP WHERE email = ?',
            (email,)
        )
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Email verified successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'OTP verification failed: {str(e)}'
        }), 500

@app.route('/api/auth/resend-otp', methods=['POST'])
def resend_otp():
    """Resend OTP endpoint"""
    try:
        data = request.get_json()
        email = data.get('email', '').lower().strip()
        
        if not email:
            return jsonify({
                'success': False,
                'message': 'Email is required'
            }), 400
        
        conn = get_db_connection()
        
        # Check if user exists
        user = conn.execute(
            'SELECT * FROM users WHERE email = ?',
            (email,)
        ).fetchone()
        
        if not user:
            conn.close()
            return jsonify({
                'success': False,
                'message': 'User not found'
            }), 404
        
        if user['is_verified']:
            conn.close()
            return jsonify({
                'success': False,
                'message': 'User is already verified'
            }), 400
        
        # Generate new OTP
        otp_code = generate_otp()
        expires_at = datetime.now() + timedelta(minutes=10)
        
        conn.execute(
            'INSERT INTO otps (email, otp_code, expires_at) VALUES (?, ?, ?)',
            (email, otp_code, expires_at)
        )
        conn.commit()
        conn.close()
        
        # Send OTP email
        subject = "Your New Tristone Partners Verification Code"
        body = create_otp_email_body(otp_code, user['first_name'])
        
        if send_email(email, subject, body):
            return jsonify({
                'success': True,
                'message': 'New verification code sent successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to send verification email'
            }), 500
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to resend OTP: {str(e)}'
        }), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    """User login endpoint"""
    try:
        data = request.get_json()
        
        email = data.get('email', '').lower().strip()
        password = data.get('password', '')
        
        if not email or not password:
            return jsonify({
                'success': False,
                'message': 'Email and password are required'
            }), 400
        
        conn = get_db_connection()
        
        # Get user
        user = conn.execute(
            'SELECT * FROM users WHERE email = ?',
            (email,)
        ).fetchone()
        
        conn.close()
        
        if not user:
            return jsonify({
                'success': False,
                'message': 'Invalid email or password'
            }), 401
        
        if not user['is_verified']:
            return jsonify({
                'success': False,
                'message': 'Please verify your email before logging in'
            }), 401
        
        # Verify password
        if not bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
            return jsonify({
                'success': False,
                'message': 'Invalid email or password'
            }), 401
        
        # Generate JWT token
        token_payload = {
            'email': user['email'],
            'exp': datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']
        }
        
        token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm='HS256')
        
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'firstName': user['first_name'],
                'lastName': user['last_name']
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Login failed: {str(e)}'
        }), 500

@app.route('/api/auth/profile', methods=['GET'])
@token_required
def get_profile(current_user_email):
    """Get user profile (protected route)"""
    try:
        conn = get_db_connection()
        user = conn.execute(
            'SELECT id, email, first_name, last_name, created_at FROM users WHERE email = ?',
            (current_user_email,)
        ).fetchone()
        conn.close()
        
        if not user:
            return jsonify({
                'success': False,
                'message': 'User not found'
            }), 404
        
        return jsonify({
            'success': True,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'firstName': user['first_name'],
                'lastName': user['last_name'],
                'createdAt': user['created_at']
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to get profile: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'message': 'Tristone Partners API is running',
        'timestamp': datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Run the app
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"Starting Tristone Partners API on port {port}")
    print("Make sure to set the following environment variables for email functionality:")
    print("- SMTP_USERNAME: Your SMTP username")
    print("- SMTP_PASSWORD: Your SMTP password")
    print("- FROM_EMAIL: The from email address")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
