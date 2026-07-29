import json
from pathlib import Path


class TradeLogger:

    FILE = Path("data/trades.json")


    def load(self):

        if not self.FILE.exists():
            return []

        import json

        return json.loads(
            self.FILE.read_text()
        )

    def log(self, trade):

        self.FILE.parent.mkdir(exist_ok=True)

        if self.FILE.exists():
            data = json.loads(self.FILE.read_text())
        else:
            data = []

        data.append(trade)

        self.FILE.write_text(
            json.dumps(data, indent=2)
        )


trade_logger = TradeLogger()
