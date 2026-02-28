# AGENTS.md — LSTM Financial Signal Prediction

## Project Overview

LSTM neural network for predicting buy/sell signals in financial markets using technical indicators.
Built with TensorFlow/Keras in Jupyter notebooks. The project optimizes hyperparameters
(timesteps, features, neurons, dropout, model architecture) and evaluates using both
accuracy metrics and a custom profit-based trading simulation.

## Environment Setup

- **Python**: 3.13 (per requirements.txt) — actual conda env may use 3.10+
- **Conda env**: `lstm-env` (see `.vscode/settings.json`)
- **Interpreter**: `c:/Users/RadoslawKucharski/miniconda3/envs/lstm-env`
- **Package manager**: conda (preferred), pip as fallback
- **Install packages** using the existing conda environment — never create new envs without asking

```bash
# Activate environment
conda activate lstm-env

# Install dependencies
pip install -r requirements.txt
```

## Build / Run / Test Commands

There are no formal build, lint, or test commands. This is a notebook-based ML project.

```bash
# Run a notebook (non-interactive, for CI or headless execution)
jupyter nbconvert --to notebook --execute 06_optimizationTimesteps.ipynb

# Run a specific notebook interactively
jupyter notebook 06_optimizationTimesteps.ipynb

# Quick GPU/CPU check
python -c "import tensorflow as tf; print(tf.__version__); print('GPUs:', tf.config.list_physical_devices('GPU'))"
```

### No formal test suite exists
- `tests/CPUvsGPU_Test.ipynb` is a hardware benchmark, not a unit test
- There is no pytest, unittest, or any test framework configured
- When adding tests, use pytest and place them in `tests/`

## Project Structure

```
├── 06_optimizationTimesteps.ipynb   # Main: timestep optimization experiments
├── 07_optimizationFeatures.ipynb    # Main: feature selection optimization
├── jupytersVastVersions/            # Archived notebook versions (02-06)
├── .conda/previous/                 # Legacy Python scripts and notebooks
├── data/                            # CSV data files (gitignored, semicolon-delimited)
├── results/                         # Experiment output (numbered folders 01-21)
├── saved_models/                    # Keras model checkpoints (gitignored)
├── tests/                           # Hardware benchmarks only
├── requirements.txt                 # Python dependencies
├── analysis_conclusions.md          # Experiment analysis results (in Polish)
├── model_improvement_prompt.md      # Enhancement implementation plan (in Polish)
├── optimzationParams.md             # Hyperparameter notes
├── GEMINI.md / QWEN.md              # AI-generated project docs
└── README.md                        # Architecture overview
```

## Key Functions (in notebooks)

| Function | Purpose |
|---|---|
| `data(time, features)` | Load CSV data, select features, reshape into sequences, split train/test |
| `fit_lstmModel(i, x_train, y_train, ...)` | Build and train LSTM model with given hyperparameters |
| `experiment(i, repeats, epochs, ...)` | Run multiple training repeats, evaluate accuracy and profit |
| `funcProfit(predict, Y_test)` | Custom trading profit calculation (spread=0.03, threshold=0.56) |
| `funcProfitOld(predict, Y_test)` | Legacy profit calculation (threshold=0.5) |
| `plotsOut(d, metrics)` | Plotly visualization of accuracy, loss, profit curves |
| `shuffle_weights(model)` | Random weight permutation for re-initialization between repeats |

## Code Style Guidelines

### Language
- Code is in English
- Comments and documentation may be in Polish or English (bilingual project)

### Imports — Standard Order
```python
# 1. Standard library
import os
import tarfile
from math import sqrt

# 2. Third-party — data/ML
import numpy as np
import pandas as pd
import tensorflow as tf
from pandas import DataFrame, Series, concat, read_csv
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# 3. Third-party — Keras (import from keras directly, not tf.keras)
from keras.models import Sequential, load_model
from keras.metrics import Precision, Accuracy
from keras.layers import LSTM, Dense, Dropout
from keras.callbacks import ModelCheckpoint, EarlyStopping, Callback
from keras.optimizers import schedules

# 4. Third-party — visualization
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 5. Environment config (after imports)
matplotlib.use('Agg')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
```

### Naming Conventions
- **Functions**: `camelCase` — `funcProfit`, `plotsOut`, `fit_lstmModel` (mixed, prefer camelCase)
- **Variables**: `camelCase` — `timeStep`, `batchSize`, `profitList`, `testingParameter`
- **Data variables**: lowercase with underscores — `x_train`, `y_test`, `Y_test`, `data_strings`
- **Constants/params**: `camelCase` — `timestepsPerSample`, `timestepsPerSampleWholeData`
- **Loop counters**: single letters — `i`, `r`, `idx`
- **Model variants**: integer-indexed via `modelVar` (0-4)

### Formatting
- 4-space indentation
- No strict line length limit (notebook cells can be wide)
- f-strings for string formatting: `f"Train shape: {x_train.shape}"`
- Semicolon (`;`) delimiter for CSV data files
- Comments use `#` with space, inline comments common

### Type Hints
- **Not used** in this codebase — do not add type hints to existing functions
- `# type: ignore` comments are used for Keras/TF type checker issues
- VSCode type checking set to `basic` mode

### Error Handling
- No explicit try/except patterns — errors propagate naturally
- TensorFlow warnings suppressed via `TF_CPP_MIN_LOG_LEVEL = '3'`
- Do not add error handling unless specifically requested

### Model Architecture Pattern
```python
# Models use Sequential API with numbered variants (modelVar 0-4)
model = Sequential()
model.add(LSTM(units=N, return_sequences=True/False, input_shape=(timesteps, features)))
model.add(Dropout(dropout))
model.add(Dense(y_train.shape[1], activation='sigmoid'))  # Always sigmoid output
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
```

### Data Format
- Input: CSV files with `;` delimiter, loaded via `np.genfromtxt(file, delimiter=';')`
- Shape: `(samples, 150, num_features)` — 150 timesteps, 4-9 features
- Labels: 6 columns, first 2 used for buy/sell binary classification
- Train/test split: 85/15, `shuffle=False` (time series — order matters)

### Results / Output
- Models saved to `./saved_models/` in `.keras` format
- Best model saved per experiment: `best_model_{param}_{timestep}.keras`
- Plots exported via Plotly + Kaleido as `.jpg`
- Results organized in numbered folders under `results/`

## Technical Indicators (Features)
```
Index:  0    1      2             3           4     5           6    7     8
Name:  RSI, VWAP, HeikenResult, closeHeiken, CMF, Stochastic, OBV, QQE, TrendFilter

features=0 → [RSI, CMF, Stochastic, TrendFilter]           (4 features)
features=1 → [RSI, VWAP, CMF, Stochastic, OBV, TrendFilter] (6 features)
features=2 → all 9 features
```

## Best Known Configuration (from analysis_conclusions.md)
- **Architecture**: Model 2 — 2×LSTM(150) + Dense(75) + Dense(2, sigmoid)
- **Timestep**: 10
- **Features**: Set 1 (6 features)
- **Optimizer**: Adam with InverseTimeDecay schedule
- **Batch size**: 64
- **Loss**: binary_crossentropy

## Important Notes for Agents
1. **Do not modify data files** — they are gitignored and may not be present
2. **Notebooks contain duplicated code** — the same functions appear in multiple notebooks
3. **Order matters**: train_test_split uses `shuffle=False` — never change this
4. **Profit > Accuracy**: The custom `funcProfit()` is the primary evaluation metric
5. **Weight re-init**: Between experiment repeats, weights are shuffled (not reloaded from init)
6. **Saved models are gitignored** — don't assume they exist in a fresh clone
7. **Comments in Polish** are normal — `Wycinanie wybranych kolumn` = "Cutting selected columns"
8. **No linter/formatter** configured — match existing style when editing
