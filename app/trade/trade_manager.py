from app.ai.learning.trade_logger import trade_logger


class TradeManager:

    def open_trade(
        self,
        symbol,
        signal,
        entry,
        stop_loss,
        tp1,
        tp2,
        tp3,
        confidence,
        institutional="UNKNOWN",
        probability=0,
        session="UNKNOWN",
        zone="UNKNOWN",
        agreement=0,
        strategy="UNKNOWN",
        market_regime="UNKNOWN",
        trade_grade="UNKNOWN",
        fusion_score=0,
        confluence_score=0,
    ):

        from datetime import datetime

        trade = {
            "symbol": symbol,
            "signal": signal,
            "entry": entry,
            "stop_loss": stop_loss,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3,
            "confidence": confidence,
            "institutional": institutional,
            "probability": probability,
            "session": session,
            "zone": zone,
            "agreement": agreement,
            "strategy": strategy,
            "market_regime": market_regime,
            "trade_grade": trade_grade,
            "fusion_score": fusion_score,
            "confluence_score": confluence_score,
            "opened_at": datetime.utcnow().isoformat(),
            "status": "OPEN",
            "result": "PENDING",
        }

        trade_logger.log(trade)

        return trade

    def close_trade(
        self,
        trade_id,
        result,
    ):

        trades = trade_logger.load()

        if trade_id < 0 or trade_id >= len(trades):
            return False

        trades[trade_id]["status"] = "CLOSED"
        from datetime import datetime

        trades[trade_id]["result"] = result.upper()
        trades[trade_id]["closed_at"] = datetime.utcnow().isoformat()

        import json

        trade_logger.FILE.write_text(
            json.dumps(trades, indent=2)
        )

        return True


trade_manager = TradeManager()
