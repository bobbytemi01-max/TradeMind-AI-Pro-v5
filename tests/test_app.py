"""Basic tests for TradeMindAI."""

import unittest

from app.main import main


class AppTests(unittest.TestCase):
    def test_main_runs(self) -> None:
        self.assertIsNone(main())


if __name__ == "__main__":
    unittest.main()
