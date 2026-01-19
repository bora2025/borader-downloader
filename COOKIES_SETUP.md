# 🚨 SECURITY WARNING: Do NOT Share Cookies!

## ❌ **Why You Should NEVER Upload Cookies to GitHub**

### **Security Risks:**
- **🔐 Login Credentials Exposed** - Anyone can access your YouTube account
- **📊 Personal Data Leaked** - Cookies contain browsing history and preferences
- **🎯 Account Hijacking** - Malicious users could take over your account
- **📜 Terms of Service Violation** - Sharing cookies violates Google's ToS

### **Legal & Ethical Concerns:**
- **⚖️ Unauthorized Access** - Could be considered hacking
- **🚫 Account Bans** - YouTube may ban accounts with shared cookies
- **💰 Monetization Loss** - Risk losing ad revenue if you're a creator

---

# ✅ **Safe Solution: User-Provided Cookies**

Instead of sharing cookies, **teach users how to get their own** safely.

## Quick Setup (Using Browser Extension)

### Method 1: Get cookies.txt LOCALLY Extension (Recommended)

1. Install the extension:
   - Chrome: [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc)
   - Firefox: [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

2. Sign in to YouTube in your browser

3. Go to any YouTube video page

4. Click the extension icon and click "Export" or "Download"

5. Save the file as `cookies.txt` in your Downloader project folder:
   ```
   C:\Users\borax\Desktop\Downloader\cookies.txt
   ```

6. Restart the Flask app:
   ```powershell
   python app.py
   ```

7. Try downloading again - it should now work!

---

# 🎯 **Better Alternatives to Cookies**

## Option 1: Desktop Version (Recommended!)
**The desktop version works without any cookies!**

```bash
# Download ZIP from GitHub
# Extract and run:
start_gui.bat  # Windows GUI
# OR
python main.py "YOUTUBE_URL"
```

✅ **Zero setup, works immediately for YouTube!**

## Option 2: Premium YouTube API
For production apps, consider:
- **YouTube Data API v3** (requires Google API key)
- **OAuth 2.0 authentication** (proper user consent)
- **Service account access** (for business use)

## Option 3: Alternative Download Methods
- **Use different user agents** (mobile/desktop simulation)
- **Implement retry logic** with delays
- **Multiple IP addresses** (for high-traffic apps)

---

## Method 2: Manual Cookie Export (Advanced)

If you prefer not to use extensions, you can manually export cookies using browser developer tools and create a Netscape format cookies.txt file.

## Important Notes

- **Security**: Never share your cookies.txt file - it contains your login session
- **Expiry**: Cookies expire after some time. If downloads stop working, export fresh cookies
- Add `cookies.txt` to `.gitignore` to avoid committing it to git

## Why This Works

- The desktop version (main.py) works because it downloads from your local IP
- Web servers get blocked by YouTube's bot detection
- Using cookies makes YouTube think the download is from a logged-in user, bypassing the block
