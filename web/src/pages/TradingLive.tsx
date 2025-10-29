import { useEffect } from 'react'
import { useSignals } from '../state/useSignals'
import { PairsCard } from '../ui/PairsCard'
import { IntervalCard } from '../ui/IntervalCard'
import { ActiveSignalCard } from '../ui/ActiveSignalCard'
import { ConfluencePanel } from '../ui/ConfluencePanel'
import { SignalOverlay } from '../ui/SignalOverlay'
export function TradingLive() {
  const { connect } = useSignals()
  useEffect(() => { connect() }, [])
  return (
TradeVision AI

LIVE

Ativar IA

TradingView M5



  )
}
