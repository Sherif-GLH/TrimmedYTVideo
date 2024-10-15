from moviepy.editor import VideoFileClip
import boto3
import os 
import random
import string
from .models import VideoTrimmed
from moviepy.video.io.VideoFileClip import VideoFileClip
from.scraping import downloadVideo


def generate_random_string(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


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

    video_title, path = downloadVideo(url)
    title = generate_random_string(10)
    video_path = f"Media/{path}.mp4"
    
    trimmed_video_path = f"Media/{title}.mp4"
    
    try:
        # Trim video using moviepy
        video_clip = VideoFileClip(video_path).subclip(start_time, end_time)
        video_clip.write_videofile(trimmed_video_path, codec="libx264")

        print("Trimming completed successfully")
    except Exception as e:
        print(f"Error trimming video: {str(e)}")
        return

    #trimmed video/audio to S3
    try:
        upload_to_s3(trimmed_video_path, f"trimmed_videos/{title}.mp4")
    except Exception as e:
        print(f"Error uploading files to S3: {str(e)}")

    remove_local_file(video_path)
    remove_local_file(trimmed_video_path)


    video_trimmed = VideoTrimmed.objects.create(
    title=video_title, 
    trimmed_video=f"/trimmed_videos/{title}.mp4")
    return video_trimmed
