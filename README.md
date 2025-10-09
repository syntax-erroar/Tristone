# Tristone Partners Dashboard

A modern React frontend application with Flask backend for SEC tools, featuring authentication, OTP verification, and a beautiful green/white theme.

## Features

- **Authentication System**
  - User registration with @tristone-partners.com email validation
  - Email verification with OTP (One-Time Password)
  - Secure login with JWT tokens
  - Protected routes and session management

- **Modern UI/UX**
  - Tristone Partners branding with green/white theme
  - Responsive design for desktop and mobile
  - Beautiful animations and transitions
  - Professional dashboard interface

- **Security**
  - Password hashing with bcrypt
  - JWT token-based authentication
  - Email domain validation
  - OTP expiration and rate limiting

## Quick Start

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables** (create a `.env` file):
   ```env
   SECRET_KEY=your-secret-key-here
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   FROM_EMAIL=noreply@tristone-partners.com
   FLASK_ENV=development
   ```

3. **Run the backend server:**
   ```bash
   python backend_app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Start the React development server:**
   ```bash
   npm start
   ```
   The application will open at `http://localhost:3000`

## Email Configuration

For OTP functionality, you'll need to configure SMTP settings:

### Gmail Setup (Recommended)
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. Use the app password in `SMTP_PASSWORD`

### Other Email Providers
Update the SMTP settings in your `.env` file according to your email provider's documentation.

## Project Structure

```
├── public/                 # Static files
├── src/
│   ├── components/
│   │   ├── Auth/          # Authentication components
│   │   └── Dashboard/     # Dashboard components
│   ├── contexts/          # React contexts
│   └── ...
├── backend_app.py         # Flask backend
├── requirements.txt       # Python dependencies
└── package.json          # Node.js dependencies
```

## API Endpoints

- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/verify-otp` - Email verification
- `POST /api/auth/resend-otp` - Resend OTP
- `GET /api/auth/profile` - Get user profile (protected)
- `GET /api/health` - Health check

## Authentication Flow

1. **Registration:**
   - User enters details with @tristone-partners.com email
   - System sends OTP to email
   - User verifies email with OTP

2. **Login:**
   - User enters email and password
   - System validates credentials
   - JWT token issued for session management

3. **Dashboard Access:**
   - Protected routes require valid JWT token
   - Token stored in localStorage
   - Automatic logout on token expiration

## Customization

### Theme Colors
The application uses CSS custom properties for theming. Update `src/index.css` to modify colors:

```css
:root {
  --primary-green: #10B981;
  --primary-green-dark: #059669;
  --secondary-green: #065F46;
  /* ... other colors */
}
```

### Email Templates
Modify the `create_otp_email_body()` function in `backend_app.py` to customize email appearance.

## Security Considerations

- Passwords are hashed using bcrypt
- JWT tokens expire after 24 hours
- OTP codes expire after 10 minutes
- Email domain validation prevents unauthorized registrations
- CORS is configured for frontend-backend communication

## Deployment

### Backend Deployment
1. Set production environment variables
2. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 backend_app:app
   ```

### Frontend Deployment
1. Build the React application:
   ```bash
   npm run build
   ```
2. Serve the `build` folder using a web server

## Troubleshooting

### Common Issues

1. **Email not sending:**
   - Check SMTP credentials
   - Verify app password for Gmail
   - Check firewall/network restrictions

2. **CORS errors:**
   - Ensure backend is running on port 5000
   - Check proxy configuration in package.json

3. **Database errors:**
   - SQLite database is created automatically
   - Check file permissions in the project directory

## Support

For issues or questions, please contact the Tristone Partners development team.

## License

© 2024 Tristone Partners. All rights reserved.
