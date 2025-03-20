import os
import yt_dlp
import streamlit as st

st.title("YouTube Video/Playlist Downloader")

# Define the playlist URL and directory
video_url = st.text_input("📥 Type YouTube Video/Playlist URL:").strip()

# Define the download directory
download_dir = 'YouTube_Download'

# Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Download options for yt-dlp
ydl_opts = {
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
}

# Add a button to trigger the download
if st.button("Download"):
    if video_url:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            st.success('✅ Video downloaded successfully!')
        except Exception as e:
            st.error(f'❌ An error occurred: {e}')
    else:
        st.error('❌ Please enter a valid video or playlist URL.')
