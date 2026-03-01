# PROJECT KNOWLEDGE BASE

**Generated:** 2026-03-01
**Domain:** MQL4 / MetaTrader 4

## OVERVIEW
MQL4 Expert Advisor and scripts for historical data export and live socket streaming.

## ROLE
Data source and live trading bridge.
Extracts raw market data from MetaTrader 4.
Calculates technical indicators.
Normalizes features for machine learning.
Feeds the Python LSTM model for inference.
Executes trades based on received model signals.

## STRUCTURE
- `include/generateFunc.mqh`: Core indicator logic and feature normalization.
- `Scripts/`: Tools for bulk historical data export to CSV.
- `Experts/`: Live trading EA.
- `Experts/` (Socket): Handles TCP connections and trade execution.

## CONVENTIONS
- **Language**: Strict MQL4.
- **Normalization**: Features pre-normalized to [-1, 1] before export.
- **Formatting**: Semicolon-delimited CSVs for historical data.
- **Types**: Use `double` for price data and indicators.
- **Error Handling**: Print socket errors to MT4 terminal log.
- **State**: Maintain minimal state in EA to prevent memory leaks.

## INTERFACE
- **Historical**: Writes `.csv` files. Python reads these for training.
- **Live Data**: Sends 21-feature strings via TCP socket.
- **Buffer**: 8KB socket buffer size.
- **Signals**: Receives Buy/Sell/Hold commands from Python server.
- **Protocol**: Synchronous request-response over local network.