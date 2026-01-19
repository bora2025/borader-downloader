import json

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🎥 BORADER Video Downloader - Google Colab Version\n",
    "\n",
    "Download videos from YouTube, TikTok, Instagram, and 1000+ sites directly in Google Colab!\n",
    "\n",
    "**✅ Works for ALL YouTube videos** - No authentication required!\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Install yt-dlp\n",
    "!pip install yt-dlp\n",
    "\n",
    "# Download the main downloader script\n",
    "!wget -q https://raw.githubusercontent.com/bora2025/borader-downloader/main/main.py\n",
    "\n",
    "# Create downloads directory\n",
    "!mkdir -p downloads\n",
    "\n",
    "# Auto-detect URL from page fragment\n",
    "from IPython.display import Javascript\n",
    "import time\n",
    "\n",
    "detected_url = None\n",
    "display(Javascript('''\n",
    "    const fragment = window.location.hash.substring(1);\n",
    "    const params = new URLSearchParams(fragment);\n",
    "    const videoUrl = params.get('video_url');\n",
    "    if (videoUrl) {\n",
    "        IPython.notebook.kernel.execute('detected_url = \"' + decodeURIComponent(videoUrl) + '\"');\n",
    "    }\n",
    "'''))\n",
    "\n",
    "time.sleep(2)\n",
    "print('✅ Setup complete!')\n",
    "if detected_url:\n",
    "    print(f'🎯 Auto-detected URL: {detected_url}')\n",
    "    print('🚀 Starting download...')\n",
    "    video_url = detected_url\n",
    "    !python main.py \"$video_url\" --output downloads\n",
    "else:\n",
    "    print('Manual mode: Set video_url below')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

with open('BORADER_Colab_Auto_v4.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print('Notebook created successfully')