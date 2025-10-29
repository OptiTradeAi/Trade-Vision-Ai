from pydantic import BaseModel
class SignalOut(BaseModel):
    pair: str
    side: str
    openTime: str
    closeTime: str
    reason: str
    confidence: float
