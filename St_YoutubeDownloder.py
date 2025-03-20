import os
import yt_dlp
import streamlit as st
from pathlib import Path

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes', None)
        speed = d.get('speed', 0)
        
        if total and total > 0:
            progress = min(max(downloaded / total, 0.0), 1.0)
        else:
            progress = 0.0
        
        st.session_state.progress_bar.progress(progress)
        st.session_state.status_text.text(f"Downloading... {progress * 100:.2f}% | Speed: {speed / 1024:.2f} KB/s")

def get_download_folder():
    return str(Path.home() / "Downloads")

def download_video(video_url, download_dir):
    os.makedirs(download_dir, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook]
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return f"✅ Video downloaded successfully in {download_dir}!"
    except Exception as e:
        return f'❌ An error occurred: {e}'

st.title("YouTube Video/Playlist Downloader")
video_url = st.text_input("📥 Enter YouTube Video/Playlist URL:")
download_dir = get_download_folder()

if 'progress_bar' not in st.session_state:
    st.session_state.progress_bar = st.progress(0)
if 'status_text' not in st.session_state:
    st.session_state.status_text = st.empty()

if st.button("Download"):
    if video_url:
        message = download_video(video_url, download_dir)
        st.session_state.status_text.text(message)
    else:
        st.error("Please enter a valid URL.")

st.markdown("---")
st.markdown("### Created by Nazmul Hasan Nayeem")
