import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            transcript = openai.Audio.transcribe("whisper-1", f, response_format="verbose_json")

        words = []
        if "segments" in transcript:
            for segment in transcript["segments"]:
                start = segment["start"]
                for word in segment["text"].split():
                    words.append({"text": word, "start": round(start, 2)})
        return words
    except Exception as e:
        return {"error": str(e)}
