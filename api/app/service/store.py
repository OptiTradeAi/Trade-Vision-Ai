from sqlalchemy import select, func
from ..models import Signal
from ..db import SessionLocal, Base, engine
from datetime import datetime
Base.metadata.create_all(bind=engine)
class Store:
    def save_signal(self, payload: dict) -> int:
        with SessionLocal() as db:
            s = Signal(
                pair=payload["pair"], side=payload["side"],
                open_time=datetime.fromisoformat(payload["openTime"]),
                close_time=datetime.fromisoformat(payload["closeTime"]),
                confidence=float(payload["confidence"]), reason=payload["reason"],
                created_at=datetime.utcnow(),
            )
            db.add(s); db.commit(); db.refresh(s); return s.id
    def settle(self, signal_id: int, result: str, exit_price: float):
        with SessionLocal() as db:
            s = db.get(Signal, signal_id)
            if not s: return
            s.result = result; s.exit_price = exit_price; db.commit()
    def history(self, limit=100):
        with SessionLocal() as db:
            return db.execute(select(Signal).order_by(Signal.id.desc()).limit(limit)).scalars().all()
    def winrate_today(self):
        with SessionLocal() as db:
            total = db.query(Signal).filter(func.date(Signal.created_at)==func.current_date()).count()
            wins = db.query(Signal).filter(func.date(Signal.created_at)==func.current_date(), Signal.result=="WIN").count()
            return {"wins":wins,"total":total,"winrate":(wins/total*100 if total else 0)}
STORE = Store()
