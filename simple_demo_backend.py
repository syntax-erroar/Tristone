#!/usr/bin/env python3
"""
Simple Demo Backend for Tristone Partners
Shows OTP codes in console for immediate testing
"""

import os
import secrets
import sqlite3
from datetime import datetime, timedelta
from functools import wraps

import bcrypt
import jwt
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'tristone-partners-secret-key-2024'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=24)

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

def send_demo_email(to_email, otp_code, first_name):
    """Demo email function - shows OTP in console"""
    print("\n" + "="*60)
    print("📧 DEMO EMAIL SERVICE - OTP VERIFICATION")
    print("="*60)
    print(f"To: {to_email}")
    print(f"Subject: Tristone Partners - Email Verification")
    print(f"")
    print(f"Hello {first_name},")
    print(f"")
    print(f"Your verification code is: {otp_code}")
    print(f"")
    print(f"This code expires in 10 minutes.")
    print("="*60)
    print("💡 Copy the code above to verify your email!")
    print("="*60)
    return True

@app.route('/api/auth/signup-no-email', methods=['POST'])
def signup_no_email():
    """User registration endpoint without email sending"""
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
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Account created successfully. OTP will be sent via EmailJS.'
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Registration failed: {str(e)}'
        }), 500

@app.route('/api/auth/store-otp-advanced', methods=['POST'])
def store_otp_advanced():
    """Store advanced OTP data with secret for otplib verification"""
    try:
        data = request.get_json()
        email = data.get('email', '').lower().strip()
        secret = data.get('secret', '').strip()
        otp_code = data.get('code', '').strip()
        expires_at_str = data.get('expiresAt', '')
        
        if not email or not secret or not otp_code:
            return jsonify({
                'success': False,
                'message': 'Email, secret, and OTP code are required'
            }), 400
        
        # Validate email domain
        if not email.endswith('@tristone-partners.com'):
            return jsonify({
                'success': False,
                'message': 'Email must be from @tristone-partners.com domain'
            }), 400
        
        # Parse expires_at
        try:
            expires_at = datetime.fromisoformat(expires_at_str.replace('Z', '+00:00'))
            if expires_at.tzinfo:
                expires_at = expires_at.replace(tzinfo=None)
        except:
            expires_at = datetime.now() + timedelta(minutes=5)
        
        conn = get_db_connection()
        
        # Update OTP table to include secret
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS advanced_otps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                secret TEXT NOT NULL,
                otp_code TEXT NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                is_used BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Store advanced OTP
        cursor.execute(
            'INSERT INTO advanced_otps (email, secret, otp_code, expires_at) VALUES (?, ?, ?, ?)',
            (email, secret, otp_code, expires_at)
        )
        conn.commit()
        conn.close()
        
        print(f"Advanced OTP {otp_code} stored for {email} (expires at {expires_at})")
        
        return jsonify({
            'success': True,
            'message': 'Advanced OTP stored successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to store advanced OTP: {str(e)}'
        }), 500

@app.route('/api/auth/store-otp', methods=['POST'])
def store_otp():
    """Legacy OTP storage for backward compatibility"""
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
        expires_at = datetime.now() + timedelta(minutes=10)
        
        # Store OTP
        conn.execute(
            'INSERT INTO otps (email, otp_code, expires_at) VALUES (?, ?, ?)',
            (email, otp_code, expires_at)
        )
        conn.commit()
        conn.close()
        
        print(f"Legacy OTP {otp_code} stored for {email} (expires in 10 minutes)")
        
        return jsonify({
            'success': True,
            'message': 'OTP stored successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to store OTP: {str(e)}'
        }), 500

@app.route('/api/auth/store-otp-simple', methods=['POST'])
def store_otp_simple():
    """Store simple OTP for Phone.Email integration"""
    try:
        data = request.get_json()
        email = data.get('email', '').lower().strip()
        otp_code = data.get('code', '').strip()
        expires_at_str = data.get('expiresAt', '')
        
        if not email or not otp_code:
            return jsonify({
                'success': False,
                'message': 'Email and OTP code are required'
            }), 400
        
        # Validate email domain
        if not email.endswith('@tristone-partners.com'):
            return jsonify({
                'success': False,
                'message': 'Email must be from @tristone-partners.com domain'
            }), 400
        
        # Parse expires_at
        try:
            expires_at = datetime.fromisoformat(expires_at_str.replace('Z', '+00:00'))
            if expires_at.tzinfo:
                expires_at = expires_at.replace(tzinfo=None)
        except:
            expires_at = datetime.now() + timedelta(minutes=5)
        
        conn = get_db_connection()
        
        # Create simple OTP table if needed
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS simple_otps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                otp_code TEXT NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                is_used BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Store simple OTP
        cursor.execute(
            'INSERT INTO simple_otps (email, otp_code, expires_at) VALUES (?, ?, ?)',
            (email, otp_code, expires_at)
        )
        conn.commit()
        conn.close()
        
        print(f"Phone.Email OTP {otp_code} stored for {email} (expires at {expires_at})")
        
        return jsonify({
            'success': True,
            'message': 'Phone.Email OTP stored successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to store Phone.Email OTP: {str(e)}'
        }), 500

@app.route('/api/auth/user-info/<email>', methods=['GET'])
def get_user_info(email):
    """Get user information by email"""
    try:
        email = email.lower().strip()
        
        conn = get_db_connection()
        user = conn.execute(
            'SELECT first_name, last_name, email FROM users WHERE email = ?',
            (email,)
        ).fetchone()
        conn.close()
        
        if not user:
            return jsonify({
                'success': False,
                'message': 'User not found'
            }), 404
        
        return jsonify({
            'success': True,
            'firstName': user['first_name'],
            'lastName': user['last_name'],
            'email': user['email']
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to get user info: {str(e)}'
        }), 500

@app.route('/api/auth/verify-otp', methods=['POST'])
def verify_otp():
    """Advanced OTP verification endpoint using otplib"""
    try:
        data = request.get_json()
        
        email = data.get('email', '').lower().strip()
        otp_code = data.get('otp', '').strip()
        
        if not email or not otp_code:
            return jsonify({
                'success': False,
                'message': 'Email and OTP are required'
            }), 400
        
        # Validate email domain
        if not email.endswith('@tristone-partners.com'):
            return jsonify({
                'success': False,
                'message': 'Email must be from @tristone-partners.com domain'
            }), 400
        
        conn = get_db_connection()
        
        # Try simple OTP first (Phone.Email integration)
        simple_otp = conn.execute(
            'SELECT * FROM simple_otps WHERE email = ? AND is_used = FALSE AND expires_at > ? ORDER BY created_at DESC LIMIT 1',
            (email, datetime.now())
        ).fetchone()
        
        if simple_otp:
            # Verify Phone.Email OTP
            if simple_otp['otp_code'] == otp_code:
                # Mark simple OTP as used
                conn.execute(
                    'UPDATE simple_otps SET is_used = TRUE WHERE id = ?',
                    (simple_otp['id'],)
                )
                
                # Mark user as verified
                conn.execute(
                    'UPDATE users SET is_verified = TRUE, updated_at = CURRENT_TIMESTAMP WHERE email = ?',
                    (email,)
                )
                
                conn.commit()
                conn.close()
                
                print(f"Phone.Email OTP verified successfully for {email}")
                
                return jsonify({
                    'success': True,
                    'message': 'Email verified successfully with Phone.Email OTP'
                }), 200
        
        # Try advanced OTP (fallback)
        advanced_otp = conn.execute(
            'SELECT * FROM advanced_otps WHERE email = ? AND is_used = FALSE AND expires_at > ? ORDER BY created_at DESC LIMIT 1',
            (email, datetime.now())
        ).fetchone()
        
        if advanced_otp:
            # Verify using advanced OTP
            if advanced_otp['otp_code'] == otp_code:
                # Mark advanced OTP as used
                conn.execute(
                    'UPDATE advanced_otps SET is_used = TRUE WHERE id = ?',
                    (advanced_otp['id'],)
                )
                
                # Mark user as verified
                conn.execute(
                    'UPDATE users SET is_verified = TRUE, updated_at = CURRENT_TIMESTAMP WHERE email = ?',
                    (email,)
                )
                
                conn.commit()
                conn.close()
                
                print(f"Advanced OTP verified successfully for {email}")
                
                return jsonify({
                    'success': True,
                    'message': 'Email verified successfully with advanced OTP'
                }), 200
        
        # Fallback to legacy OTP
        legacy_otp = conn.execute(
            'SELECT * FROM otps WHERE email = ? AND otp_code = ? AND is_used = FALSE AND expires_at > ? ORDER BY created_at DESC LIMIT 1',
            (email, otp_code, datetime.now())
        ).fetchone()
        
        if legacy_otp:
            # Mark legacy OTP as used
            conn.execute(
                'UPDATE otps SET is_used = TRUE WHERE id = ?',
                (legacy_otp['id'],)
            )
            
            # Mark user as verified
            conn.execute(
                'UPDATE users SET is_verified = TRUE, updated_at = CURRENT_TIMESTAMP WHERE email = ?',
                (email,)
            )
            
            conn.commit()
            conn.close()
            
            print(f"Legacy OTP verified successfully for {email}")
            
            return jsonify({
                'success': True,
                'message': 'Email verified successfully'
            }), 200
        
        conn.close()
        return jsonify({
            'success': False,
            'message': 'Invalid or expired OTP'
        }), 400
        
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
        
        # Send demo email (shows in console)
        send_demo_email(email, otp_code, user['first_name'])
        
        return jsonify({
            'success': True,
            'message': 'New verification code generated. Check the console!'
        }), 200
        
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
        
        print(f"\nUser logged in successfully: {email}")
        
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

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'message': 'Tristone Partners Demo API is running',
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/explorium/integrations', methods=['GET'])
def get_explorium_integrations():
    """Get Explorium integrations"""
    try:
        from explorium_service import ExploriumService, demo_explorium_service
        
        service = ExploriumService()
        result = service.get_integrations()
        
        if not result['success']:
            # Fall back to demo data
            demo_result = demo_explorium_service()
            return jsonify({
                'success': True,
                'data': demo_result['data']['integrations'],
                'message': 'Demo integrations (set up Explorium API for production)',
                'demo_mode': True
            }), 200
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to get integrations: {str(e)}'
        }), 500

@app.route('/api/explorium/enrich', methods=['POST'])
def enrich_company_data():
    """Enrich company data using Explorium"""
    try:
        data = request.get_json()
        ticker = data.get('ticker', '').upper()
        
        if not ticker:
            return jsonify({
                'success': False,
                'message': 'Ticker is required'
            }), 400
        
        from explorium_service import ExploriumService, demo_explorium_service
        
        service = ExploriumService()
        result = service.enrich_company_data(ticker)
        
        if not result['success']:
            # Fall back to demo data
            demo_result = demo_explorium_service()
            enriched_data = demo_result['data']['company_enrichment'].copy()
            enriched_data['ticker'] = ticker
            
            return jsonify({
                'success': True,
                'data': enriched_data,
                'message': f'Demo enrichment for {ticker} (set up Explorium API for production)',
                'demo_mode': True
            }), 200
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to enrich company data: {str(e)}'
        }), 500

@app.route('/api/explorium/insights', methods=['POST'])
def get_market_insights():
    """Get market insights using Explorium"""
    try:
        data = request.get_json()
        tickers = data.get('tickers', [])
        
        if not tickers:
            return jsonify({
                'success': False,
                'message': 'Tickers are required'
            }), 400
        
        from explorium_service import ExploriumService, demo_explorium_service
        
        service = ExploriumService()
        result = service.get_market_insights(tickers)
        
        if not result['success']:
            # Fall back to demo data
            demo_result = demo_explorium_service()
            insights_data = demo_result['data']['market_insights'].copy()
            insights_data['tickers'] = tickers
            
            return jsonify({
                'success': True,
                'data': insights_data,
                'message': f'Demo insights for {", ".join(tickers)} (set up Explorium API for production)',
                'demo_mode': True
            }), 200
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to get market insights: {str(e)}'
        }), 500

@app.route('/api/auth/verify-phone-email', methods=['POST'])
def verify_phone_email():
    """Verify email using Phone.Email JSON URL"""
    try:
        data = request.get_json()
        user_json_url = data.get('user_json_url')
        
        if not user_json_url:
            return jsonify({
                'success': False,
                'message': 'User JSON URL is required'
            }), 400
        
        print(f"Phone.Email verification request for URL: {user_json_url}")
        
        # Fetch user data from Phone.Email JSON URL
        import urllib.request
        import json as json_module
        
        try:
            with urllib.request.urlopen(user_json_url) as url:
                user_data = json_module.loads(url.read().decode())
            
            # Extract user email
            user_email = user_data.get('user_email_id')
            
            if not user_email:
                return jsonify({
                    'success': False,
                    'message': 'No email found in Phone.Email response'
                }), 400
            
            # Validate domain
            if not user_email.lower().endswith('@tristone-partners.com'):
                return jsonify({
                    'success': False,
                    'message': 'Email must be from @tristone-partners.com domain'
                }), 400
            
            print(f"Phone.Email verified email: {user_email}")
            
            # Check if user exists, if not create them
            conn = get_db_connection()
            existing_user = conn.execute(
                'SELECT * FROM users WHERE email = ?',
                (user_email.lower(),)
            ).fetchone()
            
            if not existing_user:
                # Create user with Phone.Email verification
                # Generate a temporary password (user will set it later)
                import secrets
                temp_password = secrets.token_urlsafe(16)
                password_hash = bcrypt.hashpw(temp_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                
                # Extract name from email
                email_parts = user_email.split('@')[0].split('.')
                first_name = email_parts[0].capitalize() if len(email_parts) > 0 else 'User'
                last_name = email_parts[1].capitalize() if len(email_parts) > 1 else 'Name'
                
                conn.execute(
                    'INSERT INTO users (email, password_hash, first_name, last_name, is_verified) VALUES (?, ?, ?, ?, ?)',
                    (user_email.lower(), password_hash, first_name, last_name, True)
                )
                conn.commit()
                
                print(f"Created new user via Phone.Email: {user_email}")
            else:
                # Mark existing user as verified
                conn.execute(
                    'UPDATE users SET is_verified = TRUE WHERE email = ?',
                    (user_email.lower(),)
                )
                conn.commit()
                
                print(f"Verified existing user via Phone.Email: {user_email}")
            
            conn.close()
            
            return jsonify({
                'success': True,
                'email': user_email,
                'message': 'Email verified successfully via Phone.Email',
                'verification_method': 'phone_email'
            }), 200
            
        except Exception as url_error:
            print(f"Error fetching Phone.Email data: {url_error}")
            return jsonify({
                'success': False,
                'message': f'Failed to fetch verification data: {str(url_error)}'
            }), 400
        
    except Exception as e:
        print(f"Phone.Email verification error: {e}")
        return jsonify({
            'success': False,
            'message': f'Phone.Email verification failed: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    print("TRISTONE PARTNERS DEMO AUTHENTICATION API")
    print("=" * 50)
    print("Demo mode: OTP codes will be shown in this console")
    print("No email setup required - works immediately!")
    print("Perfect for testing the complete authentication flow")
    print("=" * 50)
    print("Starting server on http://localhost:5000")
    print("Frontend will be available at http://localhost:3000")
    print("=" * 50)
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)
