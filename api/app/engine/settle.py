from ..integrations.tradingview import get_candle_at
async def settle_signal(store, signal_id: int, sig: dict):

    close_candle = await get_candle_at(sig["pair"], tf="M5", time=sig["closeTime"])
    exitp = close_candle["close"]
    side = sig["side"]; entry = sig.get("entryPrice", exitp)
    win = (side=="CALL" and exitp>entry) or (side=="PUT" and exitp= settings.SIGNAL_MIN_CONFIDENCE and best.time_to_next_open_sec >= 60:
            sig = {
                "pair": best.symbol,
                "side": "CALL" if best.direction=="up" else "PUT",
                "openTime": best.next_open_time.isoformat(),
                "closeTime": (best.next_open_time + dt.timedelta(minutes=5)).isoformat(),
                "reason": best.reason,
                "confidence": round(best.confidence*100, 1),
            }
            signal_id = STORE.save_signal(sig)
            await BUS.broadcast({"type":"signal","payload": sig})
            last_signal_at = dt.datetime.utcnow()
        await asyncio.sleep(2)
if __name__ == "__main__":
    asyncio.run(engine_loop())
