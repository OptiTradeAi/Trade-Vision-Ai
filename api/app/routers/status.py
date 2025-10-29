from fastapi import APIRouter
from ..service.store import STORE
router = APIRouter()
@router.get("/status/winrate")
def winrate(): return STORE.winrate_today()
