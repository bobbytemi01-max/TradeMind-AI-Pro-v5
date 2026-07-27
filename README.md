# TradeMindAI

Clean project structure for TradeMindAI.

## Layout

- app/: core application package
- app/ai/: AI analysis modules
- app/indicators/: technical indicator implementations
- app/services/: service classes for market data, analysis, and risk
- app/charts/: chart rendering utilities
- app/handlers/: command handlers
- tests/: unit tests
- charts/: chart assets or export directory

## Running

1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python -m app.main
   ```

3. Run tests:
   ```bash
   python -m pytest
   ```
