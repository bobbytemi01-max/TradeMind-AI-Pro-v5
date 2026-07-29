class ChartAnnotator:

    def annotate(self, ax, analysis):

        levels = [
            ("ENTRY", analysis["entry"]),
            ("SL", analysis["stop_loss"]),
            ("TP1", analysis["tp1"]),
            ("TP2", analysis["tp2"]),
            ("TP3", analysis["tp3"]),
        ]

        xmax = ax.get_xlim()[1]

        for label, price in levels:
            ax.text(
                xmax,
                price,
                f" {label} ",
                fontsize=8,
                ha="left",
                va="center",
                bbox=dict(boxstyle="round", alpha=0.6),
            )


chart_annotator = ChartAnnotator()
