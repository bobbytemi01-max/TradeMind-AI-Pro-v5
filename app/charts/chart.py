import os
import matplotlib.pyplot as plt


def create_chart(symbol, df, analysis):
    """
    Generate a simple price chart for Telegram.
    Returns the path to the saved PNG.
    """

    os.makedirs("charts", exist_ok=True)

    filename = f"charts/{symbol.upper()}.png"

    plt.figure(figsize=(12, 6))

    plt.plot(
        df.index,
        df["Close"],
        linewidth=2,
        label="Close Price",
    )

    if "ema20" in analysis:
        plt.axhline(
            analysis["ema20"],
            linestyle="--",
            linewidth=1,
            label="EMA20",
        )

    if "ema50" in analysis:
        plt.axhline(
            analysis["ema50"],
            linestyle="--",
            linewidth=1,
            label="EMA50",
        )

    if "ema200" in analysis:
        plt.axhline(
            analysis["ema200"],
            linestyle="--",
            linewidth=1,
            label="EMA200",
        )

    plt.title(f"{symbol.upper()} Price Chart")

    plt.xlabel("Time")
    plt.ylabel("Price")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig(filename)

    plt.close()

    return filename