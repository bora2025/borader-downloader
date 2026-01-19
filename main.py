import yt_dlp
import argparse
import os
import sys
import tkinter as tk
from tkinter import ttk
import threading

def download_video(url, output_path='downloads', progress_callback=None):
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_callback] if progress_callback else [],
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        },
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
                'player_skip': ['js'],
                'innertube_client': 'android',
            }
        },
        'geo_bypass': True,
        'sleep_interval': 2,
        'max_sleep_interval': 10,
        'sleep_interval_requests': 2,
        'retries': 10,
        'fragment_retries': 10,
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
        'socket_timeout': 30,
        'buffersize': 1024,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def launch_gui():
    root = tk.Tk()
    root.title("Video Downloader")
    root.geometry("500x250")
    
    # URL entry
    tk.Label(root, text="Video URL:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)
    
    # Output entry
    tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    output_entry = tk.Entry(root, width=50)
    output_entry.insert(0, 'downloads')
    output_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # Status label
    status_label = tk.Label(root, text="", fg="blue")
    status_label.grid(row=2, column=0, columnspan=2, pady=10)
    
    # Progress bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
    
    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded = d.get('downloaded_bytes', 0)
            if total > 0:
                percent = (downloaded / total) * 100
                root.after(0, lambda: progress_var.set(percent))
        elif d['status'] == 'finished':
            root.after(0, lambda: progress_var.set(100))
    
    def download():
        url = url_entry.get().strip()
        output = output_entry.get().strip()
        if not url:
            status_label.config(text="Please enter a URL", fg="red")
            return
        status_label.config(text="Downloading...", fg="orange")
        progress_var.set(0)
        
        def run_download():
            try:
                download_video(url, output, progress_hook)
                root.after(0, lambda: status_label.config(text="Download completed!", fg="green"))
            except Exception as e:
                root.after(0, lambda: status_label.config(text=f"Error: {str(e)}", fg="red"))
        
        thread = threading.Thread(target=run_download, daemon=True)
        thread.start()
    
    # Download button
    tk.Button(root, text="Download", command=download, bg="lightblue").grid(row=4, column=0, columnspan=2, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        launch_gui()
    else:
        parser = argparse.ArgumentParser(description='Download videos from YouTube and TikTok.')
        parser.add_argument('url', help='URL of the video to download')
        parser.add_argument('--output', default='downloads', help='Output directory (default: downloads)')
        args = parser.parse_args()
        
        try:
            download_video(args.url, args.output)
            print(f"Video downloaded to {args.output}")
        except Exception as e:
            print(f"Error: {e}")