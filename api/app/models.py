from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from .db import Base
class Signal(Base):
    __tablename__ = "signals"
    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, index=True)
    side = Column(String)  # CALL/PUT
    open_time = Column(DateTime)
    close_time = Column(DateTime)
    entry_price = Column(Float, nullable=True)
    exit_price = Column(Float, nullable=True)
    confidence = Column(Float)
    reason = Column(Text)
    result = Column(String, nullable=True)  # WIN/LOSS
    created_at = Column(DateTime)
