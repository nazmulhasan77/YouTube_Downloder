import os
import yt_dlp
 
# Define the playlist URL and directory
video_url = input("📥 Type YouTube Video/Playlist URL: ").strip()      
 
# Define the download directory
download_dir = 'D:\YouTube_Download'
 
# Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)
 
# Download options for yt-dlp
ydl_opts = {
     'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
 }
 
try:
     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
         ydl.download([video_url])
 
     print(f'✅ Video downloaded successfully!')
 
except Exception as e:
     print(f'❌ An error occurred: {e}')