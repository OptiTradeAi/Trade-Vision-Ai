import os
class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tradevision.db")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
    TZ = os.getenv("TZ", "America/Sao_Paulo")
    SIGNAL_MIN_CONFIDENCE = float(os.getenv("SIGNAL_MIN_CONFIDENCE", "0.8"))
    SIGNAL_GLOBAL_COOLDOWN_SECONDS = int(os.getenv("SIGNAL_GLOBAL_COOLDOWN_SECONDS", "600"))
    TIMEFRAME = os.getenv("TIMEFRAME", "M5")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "")
    INVESTING_DATA_SOURCE = os.getenv("INVESTING_DATA_SOURCE", "none")
settings = Settings()
