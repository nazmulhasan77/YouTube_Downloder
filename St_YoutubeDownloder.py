import os
import yt_dlp
import streamlit as st

st.title("YouTube Video/Playlist Downloader")

# Define the playlist URL
video_url = st.text_input("📥 Type YouTube Video/Playlist URL:").strip()

# Define the server-side download directory
download_dir = 'YouTube_Download'

# Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Download options for yt-dlp
ydl_opts = {
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
}

# Add a button to trigger the download
if st.button("Click Here"):
    if video_url:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            # Find the downloaded file in the directory
            downloaded_files = os.listdir(download_dir)
            downloaded_file = os.path.join(download_dir, downloaded_files[0])  # Assuming one file is downloaded

            # Provide a download link for the user
            with open(downloaded_file, "rb") as f:
                st.download_button(
                    label="Download Video",
                    data=f,
                    file_name=downloaded_file.split(os.path.sep)[-1],
                    mime="video/mp4",  # Change MIME type as needed
                )

            st.success('Click Download Video Button !')

        except Exception as e:
            st.error(f'❌ An error occurred: {e}')
    else:
        st.error('❌ Please enter a valid video or playlist URL.')
