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
            # Strategy 1: Advanced Web Client (Primary)
            ydl_opts = {
                'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'merge_output_format': 'mp4',
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Cache-Control': 'max-age=0',
                    'Sec-Ch-Ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'Sec-Ch-Ua-Mobile': '?0',
                    'Sec-Ch-Ua-Platform': '"Windows"',
                    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
                },
                'extractor_args': {
                    'youtube': {
                        'player_client': ['web', 'android', 'ios', 'web_embedded', 'tv', 'web_music', 'web_creator', 'mweb'],
                        'player_skip': ['js', 'webpage'],
                        'innertube_client': 'web',
                        'innertube_context': {
                            'client': {
                                'clientName': 'WEB',
                                'clientVersion': '2.20241206.01.00',
                            }
                        },
                        'formats': 'missing_pot',
                        'innertube_host': 'www.youtube.com',
                        'innertube_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
                        'skip': ['translated_subs', 'automatic_captions'],
                    }
                },
                'geo_bypass': True,
                'sleep_interval': 1,
                'max_sleep_interval': 5,
                'sleep_interval_requests': 1,
                'retries': 20,
                'fragment_retries': 20,
                'retry_sleep_functions': {
                    'http': lambda n: min(64, 2 ** n),
                    'fragment': lambda n: min(64, 2 ** n),
                },
                'no_check_certificate': True,
                'ignoreerrors': False,
                'extract_flat': False,
                'force_generic_extractor': False,
                'no_warnings': False,
                'quiet': False,
                'socket_timeout': 60,
                'buffersize': 1024,
                'concurrent_fragment_downloads': 1,
                'throttled_rate': '100K',
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
            except Exception as e1:
                error_msg = str(e1)
                
                # Strategy 2: iOS Safari Simulation (Fallback 1)
                if "Sign in to confirm" in error_msg or "confirm you're not a bot" in error_msg or "Video unavailable" in error_msg:
                    ios_opts = {
                        'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                        'format': 'best[ext=mp4]/best',
                        'http_headers': {
                            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.9',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'DNT': '1',
                            'Connection': 'keep-alive',
                            'Upgrade-Insecure-Requests': '1',
                            'Sec-Fetch-Dest': 'document',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-Site': 'none',
                            'Sec-Fetch-User': '?1',
                            'Cache-Control': 'max-age=0',
                        },
                        'extractor_args': {
                            'youtube': {
                                'player_client': ['ios', 'web'],
                                'player_skip': ['js'],
                                'innertube_client': 'ios',
                                'formats': 'missing_pot',
                            }
                        },
                        'geo_bypass': True,
                        'sleep_interval': 2,
                        'retries': 25,
                        'fragment_retries': 25,
                        'no_check_certificate': True,
                        'socket_timeout': 90,
                    }
                    
                    try:
                        with yt_dlp.YoutubeDL(ios_opts) as ydl:
                            info = ydl.extract_info(url, download=True)
                            filename = ydl.prepare_filename(info)
                            return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
                    except Exception as e2:
                        # Strategy 3: Android App Simulation (Fallback 2)
                        android_opts = {
                            'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                            'format': 'best[ext=mp4]/best',
                            'http_headers': {
                                'User-Agent': 'com.google.android.youtube/19.09.36 (Linux; U; Android 11; en_US) gzip',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                'Accept-Language': 'en-US,en;q=0.9',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'DNT': '1',
                                'Connection': 'keep-alive',
                            },
                            'extractor_args': {
                                'youtube': {
                                    'player_client': ['android', 'web'],
                                    'player_skip': ['js'],
                                    'innertube_client': 'android',
                                    'formats': 'missing_pot',
                                }
                            },
                            'geo_bypass': True,
                            'sleep_interval': 3,
                            'retries': 30,
                            'fragment_retries': 30,
                            'no_check_certificate': True,
                            'socket_timeout': 120,
                        }
                        
                        try:
                            with yt_dlp.YoutubeDL(android_opts) as ydl:
                                info = ydl.extract_info(url, download=True)
                                filename = ydl.prepare_filename(info)
                                return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
                        except Exception as e3:
                            # Strategy 4: Desktop TV App Simulation (Final Fallback)
                            tv_opts = {
                                'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
                                'format': 'best[ext=mp4]/best',
                                'http_headers': {
                                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                    'Accept-Language': 'en-US,en;q=0.9',
                                    'Accept-Encoding': 'gzip, deflate, br',
                                    'DNT': '1',
                                    'Connection': 'keep-alive',
                                },
                                'extractor_args': {
                                    'youtube': {
                                        'player_client': ['tv', 'web_embedded'],
                                        'player_skip': ['js'],
                                        'innertube_client': 'tv',
                                        'formats': 'missing_pot',
                                    }
                                },
                                'geo_bypass': True,
                                'sleep_interval': 5,
                                'retries': 35,
                                'fragment_retries': 35,
                                'no_check_certificate': True,
                                'socket_timeout': 180,
                            }
                            
                            try:
                                with yt_dlp.YoutubeDL(tv_opts) as ydl:
                                    info = ydl.extract_info(url, download=True)
                                    filename = ydl.prepare_filename(info)
                                    return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
                            except Exception as e4:
                                # All strategies failed, raise the most relevant error
                                raise e1
        except Exception as e:
            error_msg = str(e)
            # Handle specific YouTube errors with more aggressive approach
            if "Sign in to confirm" in error_msg or "confirm you're not a bot" in error_msg:
                error_msg = "Download failed due to YouTube restrictions. The app tried multiple bypass methods but couldn't access this video. Try a different video or use the desktop version."
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
                # For other errors, provide a generic message but keep some technical details
                error_msg = f"Download failed: {error_msg[:200]}..." if len(error_msg) > 200 else f"Download failed: {error_msg}"
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