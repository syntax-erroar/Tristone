# 📧 Company Email Setup Guide for Tristone Partners

## 🏢 Current Configuration
- **Email**: `nishit.wadhwani@tristone-partners.com`
- **Password**: `Wad84025`

## 🔧 SMTP Server Options

### Option 1: Microsoft Office 365/Outlook (Most Common)
```env
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
SMTP_USERNAME=nishit.wadhwani@tristone-partners.com
SMTP_PASSWORD=Wad84025
FROM_EMAIL=nishit.wadhwani@tristone-partners.com
```

### Option 2: Google Workspace (G Suite)
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=nishit.wadhwani@tristone-partners.com
SMTP_PASSWORD=Wad84025
FROM_EMAIL=nishit.wadhwani@tristone-partners.com
```

### Option 3: Custom Company SMTP Server
```env
SMTP_SERVER=mail.tristone-partners.com
SMTP_PORT=587
SMTP_USERNAME=nishit.wadhwani@tristone-partners.com
SMTP_PASSWORD=Wad84025
FROM_EMAIL=nishit.wadhwani@tristone-partners.com
```

## 🔍 How to Find Your Company's SMTP Settings

### Method 1: Check Your Email Client
1. Open Outlook/Mail app on your computer
2. Go to Account Settings
3. Look for "Server Settings" or "Advanced Settings"
4. Note the SMTP server address and port

### Method 2: Ask IT Department
Contact your IT team and ask for:
- SMTP server address
- SMTP port (usually 587 or 25)
- Authentication method
- Any special security requirements

### Method 3: Common Company Email Providers
- **Microsoft 365**: `smtp.office365.com:587`
- **Google Workspace**: `smtp.gmail.com:587`
- **Custom Exchange**: Usually `mail.yourcompany.com:587`

## 🚨 Potential Issues & Solutions

### Issue 1: Authentication Required
Some company emails require:
- **App Passwords** instead of regular passwords
- **Multi-factor authentication** setup
- **Less secure app access** to be enabled

### Issue 2: Security Policies
Your company might have:
- **Blocked external SMTP access**
- **Required VPN connection**
- **Specific authentication protocols**

### Issue 3: Firewall Restrictions
- Port 587 might be blocked
- Try port 25 or 465 instead
- Check with IT about firewall rules

## 🧪 Testing Email Configuration

I'll create a simple test script to try different SMTP configurations:

```python
# Test different SMTP servers
python test_smtp_config.py
```

## 💡 Recommended Next Steps

1. **Try Office 365 first** (most common for companies)
2. **Test the configuration** with our test script
3. **Contact IT if needed** for proper SMTP settings
4. **Consider alternative approaches** if SMTP is blocked

## 🔄 Alternative Solutions

If company SMTP doesn't work, we can:
1. **Use a service like SendGrid** for email delivery
2. **Set up email verification differently** 
3. **Use SMS verification** instead of email
4. **Create admin approval workflow** instead of OTP

## 🎯 Current Status

The authentication system works perfectly except for email delivery. You can still:
- ✅ Test the beautiful UI
- ✅ See the complete user flow  
- ✅ Experience all features except OTP email

Would you like me to:
1. Test the Office 365 configuration?
2. Create a script to try multiple SMTP settings?
3. Start the frontend so you can see the UI?
