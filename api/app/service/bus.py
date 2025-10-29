import asyncio
from typing import Any, Dict
class SignalBus:
    def __init__(self): self._subs = set()
    def subscribe(self) -> asyncio.Queue:
        q: asyncio.Queue[Dict[str, Any]] = asyncio.Queue()
        self._subs.add(q); return q
    async def broadcast(self, message: Dict[str, Any]):
        dead = []
        for q in list(self._subs):
            try: await q.put(message)
            except: dead.append(q)
        for q in dead: self._subs.discard(q)
BUS = SignalBus()
