# Placeholder de dados. Substitua por fonte oficial em produção.
import random, datetime as dt
async def fetch_live_symbols():
    return ["EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","NZDUSD","USDCHF","EURGBP","EURJPY","GBPJPY"]
async def get_candles(symbol: str, tf="M5", limit=150):
    now = dt.datetime.utcnow(); out=[]
    for i in range(limit):
        t = now - dt.timedelta(minutes=5*(limit-i))
        base = 1.10 + random.random()/100
        o = base + random.uniform(-0.001, 0.001)
        c = base + random.uniform(-0.001, 0.001)
        h = max(o,c) + random.uniform(0, 0.0008)
        l = min(o,c) - random.uniform(0, 0.0008)
        v = random.randint(100, 500)
        out.append({"time": t.isoformat(), "open": o, "high": h, "low": l, "close": c, "volume": v})
    return out
async def get_candle_at(symbol: str, tf="M5", time=None):
    return {"close": 1.10000}
