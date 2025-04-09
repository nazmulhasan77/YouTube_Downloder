import os
import yt_dlp
import subprocess


def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

if not check_ffmpeg():
    print("❌ FFmpeg is not installed!")
    exit(1)

# Define the playlist URL and directory
video_url = input("📥 Type YouTube Video/Playlist URL: ").strip()      

# Define the download directory
download_dir = 'D:\YouTube_Download'

# Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Download options for yt-dlp
ydl_opts = {
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio/best',  # Corrected format for best video & audio
    'merge_output_format': 'mp4',  # Make sure to merge video and audio into mp4
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Zip the directory containing the downloaded videos
    #shutil.make_archive(download_dir, 'zip', download_dir)

    print(f'✅ Video downloaded successfully!')

except Exception as e:
    print(f'❌ An error occurred: {e}')

