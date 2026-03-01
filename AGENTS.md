# PROJECT KNOWLEDGE BASE

**Generated:** 2026-03-01
**Commit:** N/A (Local development)
**Branch:** N/A

## OVERVIEW
LSTM-based financial signal prediction system. Uses technical indicators to generate Buy/Sell signals via raw TCP socket inference.

## STRUCTURE
```
.
├── 06_optimizationTimesteps.ipynb    # Main experiment: Timestep optimization
├── 07_optimizationFeatures.ipynb     # Main experiment: Feature set optimization
├── 10_Final_Training_Attention.ipynb # Production pipeline: LSTM + Attention
├── PythonServerLstm_v.1.2.py         # Production inference server (Socket)
├── data/                             # Datasets (.tar.gz and extracted .csv)
├── docs/                             # Project documentation and notes
├── logs/                             # Session logs and operation history
├── scripts/                          # Utility and maintenance scripts
├── results/                          # Sequential experiment archives (01-21) [See results/AGENTS.md]
├── saved_models/                     # Keras model checkpoints (.keras)
├── Tempkeras-source/                 # Cloned Keras repository (unintegrated reference) [See Tempkeras-source/AGENTS.md]
└── ExportAiData/                     # [Peer Project] MQL4 data export scripts [See ExportAiData/AGENTS.md]
## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Update Indicators | `ExportAiData/include/generateFunc.mqh` | Peer project handles data origin |
| Change Architecture | `10_Final_Training_Attention.ipynb` | Edit `fit_lstmModel()` |
| Inference Logic | `PythonServerLstm_v.1.2.py` | Handles socket communication |
| Past Conclusions | `docs/analysis_conclusions.md` | Summaries of previous runs |

## CODE MAP
| Symbol | Type | Location | Role |
|--------|------|----------|------|
| `data` | Function | Notebooks | Loads and reshapes semicolon-delimited CSVs |
| `fit_lstmModel` | Function | Notebooks | Builds LSTM architectures (Sequential/Functional) |
| `experiment` | Function | Notebooks | Main training loop with multiple repeats |
| `funcProfit` | Function | Notebooks | Core evaluation metric (Profit > Accuracy) |
| `MyCallback` | Class | Notebooks | Custom Keras callback for profit-based saving |

## CONVENTIONS
- **Notebook-Centric**: Logic is duplicated across notebooks for isolation.
- **CamelCase**: Functions and internal variables use camelCase.
- **Snake_case**: Data arrays (e.g., `x_train`) use snake_case.
- **Normalization**: MQL4 pre-normalizes most features to [-1, 1].

## ANTI-PATTERNS (THIS PROJECT)
- **Do NOT** add type hints to existing functions (per current style).
- **NEVER** use `shuffle=True` in `train_test_split` (Time series data).
- **Avoid** importing from `Tempkeras-source` (cloned repo is reference only).

## COMMANDS
```bash
# Headless training run
jupyter nbconvert --to notebook --execute 10_Final_Training_Attention.ipynb

# Production inference server
python PythonServerLstm_v.1.2.py
```

## NOTES
- **Buffer Size**: Socket server uses 8KB buffer for 21-feature strings.
- **Scaling**: Labels use `MinMaxScaler` fitted on whole dataset.
- **Weight Init**: Shuffled between repeats via `shuffle_weights()` to maintain start state.

