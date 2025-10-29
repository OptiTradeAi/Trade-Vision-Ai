import { useSignals } from '../state/useSignals'
export function SignalOverlay(){
  const sig = useSignals(s=>s.signal)
  if(!sig) return null
  return (
{sig.pair} — {sig.side} ({sig.confidence}%)
Motivo: {sig.reason}
  )
}
