# BORADER

A simple application to download videos from YouTube and TikTok, available as desktop app, CLI, and web app.

## Requirements

- Python 3.6+
- yt-dlp
- flask (for web app)

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Desktop GUI Mode
Run the script without arguments to launch the graphical user interface:

```
python main.py
```

A window will open where you can:
- Enter the video URL
- Specify the output directory (defaults to 'downloads')
- Click "Download" to start downloading

### Command Line Mode
Run the script with a video URL:

```
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or for TikTok:

```
python main.py "https://www.tiktok.com/@username/video/VIDEO_ID"
```

Specify output directory:

```
python main.py "URL" --output /path/to/downloads
```

Videos will be downloaded in MP4 format for maximum compatibility with media players.

### Web App Mode
Run the Flask web application:

```
python app.py
```

Open your browser to `http://localhost:5000` and use the clean, modern web interface optimized for mobile devices with responsive logo layout. The app shows real-time download progress with an animated progress bar. Mobile users will find videos in their Downloads folder and can move them to Gallery. The app includes PWA features for installation on mobile devices.

## Deployment to Cloudflare

This project can be deployed as a web app to Cloudflare Workers for serverless hosting.

### Prerequisites
- Node.js and npm installed
- Cloudflare account
- Wrangler CLI: `npm install -g wrangler`

### Deployment Steps

1. **Install Wrangler** (if not already):
   ```
   npm install -g wrangler
   ```

2. **Login to Cloudflare**:
   ```
   wrangler auth login
   ```

3. **Create a Wrangler project**:
   ```
   wrangler init my-video-downloader
   ```
   Choose "Python" when prompted for runtime.

4. **Copy your code** to the Wrangler project directory.

5. **Create wrangler.toml** in the project root:
   ```toml
   name = "video-downloader"
   main = "app.py"
   compatibility_date = "2024-01-01"
   compatibility_flags = ["python_workers"]

   [build]
   command = "pip install -r requirements.txt"

   [[build.upload]]
   format = "modules"
   dir = "."
   include = ["app.py", "requirements.txt"]
   ```

6. **Deploy**:
   ```
   wrangler deploy
   ```

7. **Access your app** at the provided URL.

Note: Cloudflare Workers Python runtime is in beta. For production, consider using Cloudflare Pages with a static frontend and Workers for the backend API.

## Note

Ensure you comply with the terms of service of the platforms and local laws regarding video downloading.