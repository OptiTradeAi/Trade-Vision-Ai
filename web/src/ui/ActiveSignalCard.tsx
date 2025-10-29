import { useSignals } from '../state/useSignals'
export function ActiveSignalCard(){
  const sig = useSignals(s=>s.signal)
  return (
Sinal Ativo
{sig ? (
{sig.pair} — {sig.side}
Abertura: {new Date(sig.openTime).toLocaleTimeString()}

Fechamento: {new Date(sig.closeTime).toLocaleTimeString()}
Probabilidade: {sig.confidence}%
Motivo: {sig.reason}
      ) : 
Nenhum sinal em execução
}
  )
}
