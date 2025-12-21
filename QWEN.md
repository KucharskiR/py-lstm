# QWEN.md - LSTM Financial Signal Prediction Project

## Project Overview

This is a machine learning project focused on developing LSTM (Long Short-Term Memory) neural networks to predict buy/sell signals in financial markets. The project uses technical indicators as input features and aims to optimize model performance based on both accuracy metrics and profit calculations from trading strategies.

The project is implemented primarily in Jupyter notebooks and uses TensorFlow/Keras for model building and training. It includes multiple experimental configurations to optimize various parameters like timesteps, features, model architecture, neurons, dropout rates, and learning rates.

## Key Technologies

- **Python 3.10+**
- **TensorFlow 2.20.0** (with Keras)
- **Pandas 2.2.2** (data manipulation)
- **NumPy** (numerical computing)
- **Scikit-learn** (machine learning utilities)
- **Matplotlib** (plotting)
- **Plotly** (interactive visualizations)
- **Kaleido** (image export for Plotly)
- **Jupyter Notebooks** (experimentation environment)

## Project Structure

- `jupytersVastVersions/` - Main implementation notebooks with different optimizations:
  - `02_optimizationNeurons.ipynb` - Neuron count optimization
  - `03_optimizationNeuronsF1score.ipynb` - F1 score optimization
  - `04_optimizationNeuronsDropout.ipynb` - Neuron and dropout optimization
  - `05_optimizationModels.ipynb` - Different model architectures
  - `06_optimizationTimesteps.ipynb` - Timestep optimization
  - `07_optimizationFeatures.ipynb` - Feature selection optimization

- `data/` - Contains financial data files (compressed in 2_150x9.tar.gz)
  - `2_150x9f.csv` - Features file with 9 technical indicators
  - `2_150x9l.csv` - Labels file with buy/sell signals

- Other important files:
  - `README.md` - Project documentation and architecture overview
  - `requirements.txt` - Python dependencies
  - `model_improvement_suggestions.md` - Enhancement suggestions
  - `model_improvement_prompt.md` - Implementation guidelines for improvements
  - `lstm_Model.h5` - Saved trained model
  - `results/` - Model results and performance metrics
  - `saved_models/` - Trained model checkpoints

## Key Features

### Data Preparation
- Features include 9 technical indicators: RSI, VWAP, HeikenResult, closeHeiken, CMF, Stochastic, OBV, QQE, TrendFilter
- Data is preprocessed with normalization and reshaping into time series sequences
- Features can be selected dynamically based on the `features` parameter (0, 1, or 2)

### Model Architectures
- Multiple LSTM configurations tested (models 0-4)
- Single and double LSTM layer architectures with dropout regularization
- Dense layers for output with sigmoid activation for binary classification
- Various neuron counts (50, 150, 300, 1000) tested

### Training Features
- Binary crossentropy loss function
- Adam optimizer with learning rate scheduling
- Early stopping to prevent overfitting
- Model checkpointing based on validation loss
- Custom profit-based callbacks for model evaluation during training
- Weight initialization and shuffling mechanisms

### Evaluation Metrics
- Accuracy on validation data
- Custom profit function based on trading simulation
- F1-score (in some notebooks)
- Visualization of training metrics (accuracy, loss, profit)

## Building and Running

### Environment Setup
```bash
# Create conda environment
conda create -n lstm_env python=3.10
conda activate lstm_env

# Install dependencies
pip install -r requirements.txt
```

### Running Experiments
1. Extract data: `tar -xzf 2_150x9.tar.gz` in the data directory
2. Open and run any notebook in the `jupytersVastVersions/` directory
3. Each notebook contains complete experiment logic with data loading, model training, and visualization

### Key Parameters for Experimentation
- `timeStep`: Length of time series sequences (default 150)
- `features`: Feature selection (0, 1, or 2)
- `neurons`: Number of LSTM neurons (50, 150, 300, etc.)
- `dropout`: Dropout rate for regularization
- `model`: Model architecture (0-4)
- `epochs`: Number of training epochs
- `repeats`: Number of experiment repeats for statistical significance

## Development Conventions

- Data files use semicolon (`;`) as delimiter
- Time series sequences are 150 steps long with 4-9 features
- Output is binary (buy/sell) classification
- Profit calculation assumes 0.03 spread and includes take-profit logic
- Model saving uses Keras .keras format
- Visualizations include accuracy, loss, and profit metrics

## Current Project Status

- Production-ready LSTM models for financial signal prediction
- Multiple optimization experiments completed
- Model with best performance selected based on validation metrics and profit
- Ready for enhancement implementation (attention mechanisms, GRU, additional indicators)

## Future Enhancements

Based on `model_improvement_suggestions.md`, planned enhancements include:
- Adding MACD, Bollinger Bands, and ATR technical indicators
- Feature engineering with binary signals (overbought/oversold, etc.)
- Attention mechanisms for better temporal focus
- GRU alternatives to LSTM layers
- Sentiment analysis integration

## Key Files to Modify for Enhancements

- `fit_lstmModel()` function in notebooks for architecture improvements
- `data()` function for adding new technical indicators
- `funcProfit()` for custom metric calculations
- Experiment functions for testing new configurations