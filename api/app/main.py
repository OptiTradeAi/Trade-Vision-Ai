from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from .routers import health, status, history
from .engine.runner import engine_loop
from .service.bus import BUS
import asyncio, json
app = FastAPI(title="TradeVision API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)
app.include_router(health.router, prefix="")
app.include_router(status.router, prefix="")
app.include_router(history.router, prefix="")
Base.metadata.create_all(bind=engine)
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(engine_loop())
@app.websocket("/ws/signals")
async def ws_signals(ws: WebSocket):
    await ws.accept()
    q = BUS.subscribe()
    while True:
        msg = await q.get()
        await ws.send_text(json.dumps(msg))
