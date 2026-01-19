from flask import Flask, request, send_file, render_template_string
import yt_dlp
import tempfile
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>BORADER</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <link rel="manifest" href="/manifest.json">
                <meta name="theme-color" content="#667eea">
                <style>
                    body {
                        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                        min-height: 100vh;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 20px 15px;
                    }
                    .card {
                        border: none;
                        border-radius: 20px;
                        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                        backdrop-filter: blur(10px);
                        background: rgba(255, 255, 255, 0.95);
                        transition: transform 0.3s ease, box-shadow 0.3s ease;
                    }
                    .card:hover {
                        transform: translateY(-5px);
                        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
                    }
                    .btn-download {
                        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
                        border: none;
                        border-radius: 12px;
                        font-weight: 600;
                        letter-spacing: 0.5px;
                        transition: all 0.3s ease;
                        position: relative;
                        overflow: hidden;
                    }
                    .btn-download:hover {
                        transform: translateY(-2px);
                        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
                    }
                    .btn-download:active {
                        transform: translateY(0);
                    }
                    .form-control {
                        border-radius: 12px;
                        border: 2px solid #e1e5e9;
                        transition: border-color 0.3s ease, box-shadow 0.3s ease;
                    }
                    .form-control:focus {
                        border-color: #667eea;
                        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
                    }
                    .form-label {
                        font-weight: 600;
                        color: #495057;
                        margin-bottom: 8px;
                    }
                    h1 {
                        font-weight: 700;
                        background: linear-gradient(45deg, #667eea, #764ba2);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;
                        margin-bottom: 1rem;
                        text-align: center;
                    }
                    .logo-container {
                        text-align: center;
                        margin-bottom: 1rem;
                    }
                    .logo-container img {
                        max-width: 100%;
                        height: auto;
                        max-height: 120px;
                    }
                    .title-separator {
                        width: 100%;
                        height: 2px;
                        background: linear-gradient(90deg, transparent, #667eea, transparent);
                        margin: 1rem 0;
                    }
                    .text-muted {
                        color: #6c757d !important;
                    }
                    .progress {
                        height: 25px;
                        border-radius: 12px;
                    }
                    @media (max-width: 576px) {
                        .card {
                            margin: 10px;
                            padding: 2rem 1.5rem !important;
                        }
                        body {
                            padding: 10px 5px;
                        }
                    }
                </style>
            </head>
            <body>
                <div class="container d-flex align-items-center justify-content-center min-vh-100">
                    <div class="card p-5 w-100" style="max-width: 500px;">
                        <div class="logo-container">
                            <img src="/img/Phka Ramdol.png" alt="Logo">
                        </div>
                        <div class="title-separator"></div>
                        <h1>🎥 BORADER</h1>
                        <div class="title-separator"></div>
                        <p class="text-danger text-center">Please enter a URL</p>
                        <form method="post" class="mb-3">
                            <div class="mb-3">
                                <label for="url" class="form-label">Video URL</label>
                                <input type="url" class="form-control" id="url" name="url" placeholder="https://www.youtube.com/watch?v=..." required>
                            </div>
                            <button type="submit" class="btn btn-download btn-lg w-100 text-white">⬇️ Download Video</button>
                        </form>
                        <p class="text-muted text-center small">Supports YouTube, TikTok, and more. Downloads in MP4 format.</p>
                    </div>
                </div>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
            ''')
        
        try:
            # Universal multi-strategy download system for all platforms including YouTube
            # Check for cookies.txt file for authenticated YouTube access
            cookies_path = os.path.join(os.path.dirname(__file__), 'cookies.txt')
            has_cookies = os.path.exists(cookies_path)
            
            strategies = [
                    # Strategy 1: With cookies (if available) for authenticated access
                    {
                        'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                        'format': 'best[height<=1080]/best',
                        'cookiefile': cookies_path if has_cookies else None,
                        'http_headers': {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Referer': 'https://www.youtube.com/',
                        },
                        'geo_bypass': True,
                        'nocheckcertificate': True,
                        'retries': 10,
                        'fragment_retries': 10,
                        'socket_timeout': 30,
                    },
                    # Strategy 2: yt-dlp default extractor (most reliable for YouTube)
                    {
                        'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                        'format': 'best[height<=720]/best',
                        'cookiefile': cookies_path if has_cookies else None,
                    },
                    # Strategy 3: Mobile client (often bypasses restrictions)
                    {
                        'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                        'format': 'best[height<=480]/best',
                        'http_headers': {
                            'User-Agent': 'com.google.android.youtube/17.36.4 (Linux; U; Android 12; en_US) gzip',
                        },
                        'cookiefile': cookies_path if has_cookies else None,
                        'geo_bypass': True,
                    }
            ]

            last_error = None
            for i, ydl_opts in enumerate(strategies, 1):
                try:
                    print(f"Trying download strategy {i}/{len(strategies)} (retries: {ydl_opts['fragment_retries']}, sleep: {ydl_opts.get('sleep_interval', 0)}s)...")
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=True)
                        filename = ydl.prepare_filename(info)
                        print(f"✅ Strategy {i} succeeded!")
                        return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
                except Exception as e:
                    last_error = str(e)
                    print(f"❌ Strategy {i} failed: {last_error[:150]}")
                    continue

            # If all strategies failed, raise the last error
            raise Exception(last_error)
        except Exception as e:
            error_msg = str(e)
            # Handle specific errors with more detailed messages
            if "Sign in to confirm" in error_msg or "confirm you're not a bot" in error_msg:
                error_msg = "Download failed after trying 5 different bypass strategies. This video may have special restrictions. Please try again or use a different video quality."
            elif "Video unavailable" in error_msg or "This video is not available" in error_msg:
                error_msg = "This video is not available or has been removed. Please check the URL and try again."
            elif "Private video" in error_msg:
                error_msg = "This is a private video that cannot be downloaded."
            elif "Age-restricted" in error_msg or "age-restricted" in error_msg:
                error_msg = "This video is age-restricted and cannot be downloaded."
            elif "Region blocked" in error_msg or "not available in your country" in error_msg:
                error_msg = "This video is not available in your region."
            elif "HTTP Error 429" in error_msg or "Too Many Requests" in error_msg:
                error_msg = "Too many requests. Please wait a few minutes and try again."
            else:
                error_msg = f"Download failed after trying multiple strategies: {error_msg[:150]}..." if len(error_msg) > 150 else f"Download failed: {error_msg}"
            return render_template_string('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>BORADER - Error</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <link rel="manifest" href="/manifest.json">
                <meta name="theme-color" content="#667eea">
                <style>
                    body {
                        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                        min-height: 100vh;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 20px 15px;
                    }
                    .card {
                        border: none;
                        border-radius: 20px;
                        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                        backdrop-filter: blur(10px);
                        background: rgba(255, 255, 255, 0.95);
                    }
                    .logo-container {
                        text-align: center;
                        margin-bottom: 1rem;
                    }
                    .logo-container img {
                        max-width: 100%;
                        height: auto;
                        max-height: 120px;
                    }
                    .title-separator {
                        width: 100%;
                        height: 2px;
                        background: linear-gradient(90deg, transparent, #667eea, transparent);
                        margin: 1rem 0;
                    }
                    @media (max-width: 576px) {
                        .card {
                            margin: 10px;
                            padding: 2rem 1.5rem !important;
                        }
                        body {
                            padding: 10px 5px;
                        }
                    }
                </style>
            </head>
            <body>
                <div class="container d-flex align-items-center justify-content-center min-vh-100">
                    <div class="card p-5 w-100" style="max-width: 500px;">
                        <div class="logo-container">
                            <img src="/img/Phka Ramdol.png" alt="Logo">
                        </div>
                        <div class="title-separator"></div>
                        <h1>❌ Error</h1>
                        <div class="title-separator"></div>
                        <p class="text-danger text-center">''' + error_msg + '''</p>
                        <div class="text-center">
                            <button class="btn btn-secondary" onclick="window.location.href='/'">⬅️ Back</button>
                        </div>
                    </div>
                </div>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
            ''')
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BORADER</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="manifest" href="/manifest.json">
        <meta name="theme-color" content="#667eea">
        <style>
            body {
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 20px 15px;
            }
            .card {
                border: none;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                backdrop-filter: blur(10px);
                background: rgba(255, 255, 255, 0.95);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 30px 60px rgba(0,0,0,0.15);
            }
            .btn-download {
                background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
                border: none;
                border-radius: 12px;
                font-weight: 600;
                letter-spacing: 0.5px;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            .btn-download:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
            }
            .btn-download:active {
                transform: translateY(0);
            }
            .form-control {
                border-radius: 12px;
                border: 2px solid #e1e5e9;
                transition: border-color 0.3s ease, box-shadow 0.3s ease;
            }
            .form-control:focus {
                border-color: #667eea;
                box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
            }
            .form-label {
                font-weight: 600;
                color: #495057;
                margin-bottom: 8px;
            }
            h1 {
                font-weight: 700;
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 1rem;
                text-align: center;
            }
            .logo-container {
                text-align: center;
                margin-bottom: 1rem;
            }
            .logo-container img {
                max-width: 100%;
                height: auto;
                max-height: 120px;
            }
            .title-separator {
                width: 100%;
                height: 2px;
                background: linear-gradient(90deg, transparent, #667eea, transparent);
                margin: 1rem 0;
            }
            .text-muted {
                color: #6c757d !important;
            }
            @media (max-width: 576px) {
                .card {
                    margin: 10px;
                    padding: 2rem 1.5rem !important;
                }
                body {
                    padding: 10px 5px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container d-flex align-items-center justify-content-center min-vh-100">
            <div class="card p-5 w-100" style="max-width: 500px;">
                        <div class="logo-container">
                            <img src="/img/Phka Ramdol.png" alt="Logo">
                        </div>
                        <div class="title-separator"></div>
                        <h1>🎥 BORADER</h1>
                        <div class="title-separator"></div>
                <p class="text-center text-muted mb-4">Download videos from YouTube, TikTok, and more in MP4 format</p>
                <form method="post" class="mb-3">
                    <div class="mb-3">
                        <label for="url" class="form-label fw-bold">Video URL</label>
                        <input type="url" class="form-control form-control-lg" id="url" name="url" placeholder="https://www.youtube.com/watch?v=..." required>
                    </div>
                    <button type="submit" class="btn btn-download btn-lg w-100 text-white fw-bold">⬇️ Download Video</button>
                </form>
                <div class="text-center">
                    <small class="text-muted">🚀 <strong>Power Toolkit:</strong> Advanced YouTube bypass for direct downloads</small><br>
                    <small class="text-muted">📱 Mobile users: Videos download to your device's default Downloads folder. You can move them to Gallery from there.</small>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)