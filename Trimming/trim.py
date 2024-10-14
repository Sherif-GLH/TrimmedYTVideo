from moviepy.editor import VideoFileClip
import boto3
import yt_dlp
import webvtt
import json
import os 
import random
import string
from .models import VideoTrimmed
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip


def generate_random_string(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Example usage

def upload_to_s3(file_path, s3_path):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, os.getenv('AWS_STORAGE_BUCKET_NAME'), s3_path,
                       ExtraArgs={'ACL': 'public-read'})
        print(f"Uploaded {file_path} to S3 bucket.")
    except Exception as e:
        print(f"Error uploading {file_path} to S3: {str(e)}")

def remove_local_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Removed local file: {file_path}")
        else:
            print(f"File does not exist: {file_path}")
    except Exception as e:
        print(f"Error removing file {file_path}: {str(e)}")

def TrimVideo(url, start_time, end_time):

    # Download video and audio from YouTube using yt-dlp
    
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)  # Extract info without downloading
        format = info_dict['formats'][-2]
        Video_format_id = format.get('format_id', 'N/A')
        for format in info_dict['formats']:
            ext = format.get('ext', 'N/A')
            resolution = f"{format.get('width', 'N/A')}x{format.get('height', 'N/A')}"
            ### check the extention and resolution ###
            if ext == "webm" :
            # get id_vedio #
                if resolution == "NonexNone":
                    Audio_format_id = format.get('format_id', 'N/A')

    title = generate_random_string(10)
    video_path = f"Media/{title}.mp4"
    audio_path = f"Media/{title}.mp3"
    trimmed_video_path = f"Media/{title}.mp4"
    trimmed_audio_path = f"Media/{title}.mp3"

    try:
        ydl_opts = {
            'cookiefile': '/app/cookies.txt',
            'format': Video_format_id,
            'outtmpl': video_path,  
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            if 'subtitles' in info:
                print("Available subtitles:")

            else:
                print("No subtitles available for this video.")

            print("Downloaded successfully")
    except Exception as e:
        print({"error": str(e)})

    try:
        ydl_opts = {
            'cookiefile': '/app/cookies.txt',
            'format': Audio_format_id,
            'outtmpl': audio_path,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
    except Exception as e:
        print({"error": str(e)})
    try:
        # Trim video using moviepy
        video_clip = VideoFileClip(video_path).subclip(start_time, end_time)
        video_clip.write_videofile(trimmed_video_path, codec="libx264")

        # Trim audio using moviepy
        audio_clip = AudioFileClip(audio_path).subclip(start_time, end_time)
        audio_clip.write_audiofile(trimmed_audio_path)

        print("Trimming completed successfully")
    except Exception as e:
        print(f"Error trimming video/audio: {str(e)}")
        return

    #trimmed video/audio to S3
    try:
        upload_to_s3(trimmed_video_path, f"trimmed_videos/trimmed_{title}.mp4")
        upload_to_s3(trimmed_audio_path, f"trimmed_audio/trimmed_{title}.mp3")
    except Exception as e:
        print(f"Error uploading files to S3: {str(e)}")

    remove_local_file(video_path)
    remove_local_file(audio_path)
    remove_local_file(trimmed_video_path)
    remove_local_file(trimmed_audio_path)
    remove_local_file(f"Media/{title}.en.vtt")

    video_trimmed = VideoTrimmed.objects.create(
    title=info_dict['title'], 
    trimmed_video=f"/trimmed_videos/trimmed_{title}.mp4",
    trimmed_audio=f"/trimmed_audio/trimmed_{title}.mp3")
    return video_trimmed
