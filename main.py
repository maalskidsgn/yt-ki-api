from fastapi import FastAPI
from pydantic import BaseModel
from utils.download import download_audio
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class TranscribeRequest(BaseModel):
    url: str

@app.post("/transcribe")
async def transcribe(request: TranscribeRequest):
    try:
        mp3_path = download_audio(request.url)
        with open(mp3_path, "rb") as f:
            transcript = openai.audio.transcriptions.create(
                file=f,
                model="whisper-1",
                response_format="verbose_json"
            )
        return transcript
    except Exception as e:
        return {"error": str(e)}
