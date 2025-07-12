from fastapi import FastAPI, Request
from pydantic import BaseModel
from utils.download import download_audio
from utils.whisper import transcribe_audio
import os

app = FastAPI()

class TranscribeRequest(BaseModel):
    url: str

@app.post("/transcribe")
async def transcribe(req: TranscribeRequest):
    audio_path = download_audio(req.url)
    if not audio_path:
        return {"error": "Audio konnte nicht geladen werden."}

    result = transcribe_audio(audio_path)
    os.remove(audio_path)  # Clean up
    return result
