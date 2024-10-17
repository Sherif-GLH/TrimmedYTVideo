import os, random, string, requests, json


def generate_random_string(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def downloadvideo(url):
    new_title = generate_random_string(10)
    api_url ="http://18.118.105.172:3000/download-video"
    download_directory = os.path.abspath('Media/')  # Ensure you use the absolute path
    payload = {
        "youtubeVideoUrl": url,
    }
    # Set the headers to specify the content type as JSON
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request
    print("getting url")
    response = requests.post(api_url, data=json.dumps(payload), headers=headers).json()
    url = response['video_url']
    title = response['video_title']
    print("Starting download...")
    response = requests.get(url=url, stream=True) 
    file_path = os.path.join(download_directory, f"{new_title}.mp4")
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return str(title) , file_path