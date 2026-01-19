# How to Fix YouTube 403 Errors with Cookies

YouTube is blocking server-based downloads with HTTP 403 Forbidden errors. To fix this, you need to provide your YouTube session cookies.

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
