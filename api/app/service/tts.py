import os, requests
def tts_bytes(text: str) -> bytes:
    key=os.getenv("ELEVENLABS_API_KEY"); voice=os.getenv("ELEVENLABS_VOICE_ID","")
    if not key or not voice: return b""
    r=requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
        headers={"xi-api-key":key,"Content-Type":"application/json"},
        json={"text":text,"model_id":"eleven_turbo_v2"})
    r.raise_for_status(); return r.content
