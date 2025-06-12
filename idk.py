import os
import subprocess

VIDEO_URL = "https://www.youtube.com/watch?v=R4-d2XBwpaQ"
VIDEO_FILE = "input_video.mp4"
OUTPUT_DIR = "clips"

# Step 1: Download the video using yt-dlp
def download_video(url, output_filename):
    subprocess.run([
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "-o", output_filename,
        url
    ], check=True)

# Step 2: Extract 1-minute clips using ffmpeg
def extract_clips(input_filename, output_dir, clip_count=8):
    os.makedirs(output_dir, exist_ok=True)
    for i in range(clip_count):
        start_time = i * 60  # seconds
        output_file = os.path.join(output_dir, f"clip_{i+1:02d}.mp4")
        subprocess.run([
            "ffmpeg",
            "-ss", str(start_time),
            "-i", input_filename,
            "-t", "60",
            "-c", "copy",
            output_file
        ], check=True)

if __name__ == "__main__":
    print("Downloading video...")
    download_video(VIDEO_URL, VIDEO_FILE)
    
    print("Extracting clips...")
    extract_clips(VIDEO_FILE, OUTPUT_DIR)

    print("Done.")
