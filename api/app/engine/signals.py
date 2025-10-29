import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands
def compute_confluence(candles):
    closes = pd.Series([c['close'] for c in candles])
    if len(closes) < 50: return 0.0, "up", "dados insuficientes"
    rsi = RSIIndicator(closes, window=14).rsi().iloc[-1]
    macd = MACD(closes,12,26,9); hist = macd.macd_diff().iloc[-1]
    bb = BollingerBands(closes,20,2)
    upper = bb.bollinger_hband().iloc[-1]; lower = bb.bollinger_lband().iloc[-1]
    last = closes.iloc[-1]
    score=0.0; reasons=[]
    if rsi<30 and last<=lower: score+=0.4; reasons.append("reversão banda inferior + RSI sobrevendido")
    if rsi>70 and last>=upper: score+=0.4; reasons.append("reversão banda superior + RSI sobrecomprado")
    if hist>0: score+=0.1; reasons.append("momentum positivo")
    if hist<0: score+=0.1; reasons.append("momentum negativo")
    direction = "up" if (rsi<35 or hist>0) else "down"
    return float(min(0.99,score)), direction, (" | ".join(reasons) or "contexto neutro")
