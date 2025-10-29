from fastapi import APIRouter
from ..service.store import STORE
router = APIRouter()
@router.get("/history")
def history():
    data = STORE.history(100)
    return [
        {
            "id": s.id, "pair": s.pair, "side": s.side,
            "openTime": s.open_time.isoformat() if s.open_time else None,
            "closeTime": s.close_time.isoformat() if s.close_time else None,
            "result": s.result, "confidence": s.confidence, "reason": s.reason
        } for s in data
    ]
