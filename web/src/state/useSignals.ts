import { create } from 'zustand'
type Signal = { pair:string; side:'CALL'|'PUT'; openTime:string; closeTime:string; reason:string; confidence:number }
type Store = { ws?: WebSocket; signal?: Signal; nextEta?: number; connect: () => void }
export const useSignals = create((set) => ({
  connect: () => {
    const url = import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws/signals'
    const ws = new WebSocket(url)
    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data)
      if (msg.type === 'signal') set({ signal: msg.payload })
      if (msg.type === 'status') set({ nextEta: msg.payload.nextEtaSec })
    }
    set({ ws })
  }
}))
