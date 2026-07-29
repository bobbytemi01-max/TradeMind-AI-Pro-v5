from pathlib import Path

import mplfinance as mpf
import matplotlib.pyplot as plt
from app.chart.annotator import chart_annotator
from app.chart.overlays.overlay_engine import overlay_engine


class ChartEngine:

    def create(self, df, symbol, analysis):

        Path("charts").mkdir(exist_ok=True)

        filename = f"charts/{symbol}.png"

        entry = analysis["entry"]
        sl = analysis["stop_loss"]
        tp1 = analysis["tp1"]
        tp2 = analysis["tp2"]
        tp3 = analysis["tp3"]

        fig, axlist = mpf.plot(
            df.tail(120),
            type="candle",
            style="yahoo",
            mav=(20, 50),
            volume=True,
            returnfig=True,
        )

        ax = axlist[0]

        ax.axhline(entry, linestyle="--", linewidth=1.5, label="Entry")
        ax.axhline(sl, linestyle="--", linewidth=1.5, label="Stop Loss")
        ax.axhline(tp1, linestyle=":", linewidth=1.2, label="TP1")
        ax.axhline(tp2, linestyle=":", linewidth=1.2, label="TP2")
        ax.axhline(tp3, linestyle=":", linewidth=1.2, label="TP3")

        ax.set_title(
            f"{symbol} | {analysis['final_signal']} | "
            f"{analysis['probability']}% | "
            f"{analysis['institutional_bias']}"
        )

        ax.legend()

        overlay_engine.draw(ax, analysis)

        chart_annotator.annotate(
            ax,
            analysis,
        )

        fig.savefig(filename, dpi=220)
        plt.close(fig)

        return filename


chart_engine = ChartEngine()
