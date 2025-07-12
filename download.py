import yt_dlp
import os
import uuid

def download_audio(url):
    filename = f"/tmp/{uuid.uuid4()}.m4a"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '64',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return filename if os.path.exists(filename) else None
    except Exception as e:
        print("Fehler beim Download:", e)
        return None
