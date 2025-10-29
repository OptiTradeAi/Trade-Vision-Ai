from ..integrations.tradingview import fetch_live_symbols, get_candles
from .signals import compute_confluence
from .utils_time import next_m5_open
class Candidate:
    def __init__(self, symbol, confidence, direction, reason, next_open_time, ttn):
        self.symbol, self.confidence, self.direction, self.reason = symbol, confidence, direction, reason
        self.next_open_time, self.time_to_next_open_sec = next_open_time, ttn
async def scan_pairs():
    symbols = await fetch_live_symbols()
    best=None
    for s in symbols:
        candles = await get_candles(s, tf="M5", limit=150)
        conf, direction, reason = compute_confluence(candles)
        nxt, ttn = next_m5_open()
        cand = Candidate(s, conf, direction, reason, nxt, ttn)
        if not best or cand.confidence > best.confidence: best = cand
    return best
