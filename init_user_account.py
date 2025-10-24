#!/usr/bin/env python3
"""
Initialize user account for SEC Tools Suite
This script sets up the test user account with proper credentials
"""

import sqlite3
import bcrypt
import os

def init_test_user():
    """Initialize the test user account"""
    db_path = os.path.join(os.path.dirname(__file__), "tristone_auth.db")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if user already exists
        cursor.execute("SELECT id FROM users WHERE email = 'test@123'")
        existing_user = cursor.fetchone()
        
        if existing_user:
            # Update existing user
            password_hash = bcrypt.hashpw("Tristone@123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursor.execute("""
                UPDATE users 
                SET password_hash = ?, is_verified = 1, is_active = 1, role = 'user'
                WHERE email = 'test@123'
            """, (password_hash,))
            print("✅ Updated existing test user account")
        else:
            # Create new user
            password_hash = bcrypt.hashpw("Tristone@123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursor.execute("""
                INSERT INTO users (email, password_hash, first_name, last_name, is_verified, is_active, role, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
            """, ("test@123", password_hash, "Test", "User", 1, 1, "user"))
            print("✅ Created new test user account")
        
        conn.commit()
        print("✅ Test user account is ready!")
        print("   Email: test@123")
        print("   Password: Tristone@123")
        print("   Status: Verified and Active")
        
    except Exception as e:
        print(f"❌ Error setting up user account: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    init_test_user()
