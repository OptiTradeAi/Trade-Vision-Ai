import { useSignals } from '../state/useSignals'
export function IntervalCard(){
  const next = useSignals(s=>s.nextEta)
  return (
Intervalo Entre Sinais
{next ? Math.max(0,next) : 0}s
Sistema pronto para enviar próxima oportunidade
  )
}
