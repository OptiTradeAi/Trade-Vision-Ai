### TradeVision AI — Intelligent Binary Options Agent (M5)

Funcionalidades:

- Rotação autônoma por pares abertos
- Sinais com antecedência >= 1 min para a próxima vela M5
- Probabilidade >= 80%, motivo, TTS, overlay no gráfico
- 1 sinal por vez, cooldown 10 min
- Win/Loss e histórico
- Fuso: America/Sao_Paulo

Rodar local

1) Copie .env.example para .env e ajuste chaves.
2) docker compose up --build
3) Frontend: http://localhost:5173
4) Backend: http://localhost:8000 | WS: ws://localhost:8000/ws/signals

Deploy (Render)

- Crie serviço “Web Service” para api/ (Dockerfile).
- Crie serviço “Web Service” (ou Static) para web/ (Dockerfile).
- Defina VITE_WS_URL no frontend com o wss do backend: wss://SEU-BACKEND.onrender.com/ws/signals
