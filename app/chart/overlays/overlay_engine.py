class OverlayEngine:

    def draw(self, ax, analysis):

        # Premium / Discount equilibrium
        if analysis.get("equilibrium"):
            ax.axhline(
                analysis["equilibrium"],
                linestyle="--",
                linewidth=1,
                alpha=0.6,
                label="Equilibrium"
            )

        # Equal Highs
        if analysis.get("equal_highs"):
            ax.axhline(
                analysis["equal_high_level"],
                linestyle=":",
                linewidth=1,
                alpha=0.8,
                label="Equal Highs"
            )

        # Equal Lows
        if analysis.get("equal_lows"):
            ax.axhline(
                analysis["equal_low_level"],
                linestyle=":",
                linewidth=1,
                alpha=0.8,
                label="Equal Lows"
            )

        # Fair Value Gap
        if analysis.get("fvg"):
            ax.axhspan(
                analysis["bottom"],
                analysis["top"],
                alpha=0.15,
                label="Fair Value Gap"
            )


overlay_engine = OverlayEngine()
