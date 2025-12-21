## Project Overview

This project is dedicated to the development and optimization of a Long Short-Term Memory (LSTM) neural network for financial forecasting. The primary goal is to predict buy and sell signals in financial markets to maximize profitability. The project is structured around a series of Jupyter notebooks, each focusing on a specific aspect of model optimization, such as tuning the number of neurons, dropout rates, learning rates, timesteps, and feature sets.

The core of the project is a set of Python functions that handle data loading and preprocessing, LSTM model construction, training, and evaluation. The models are built using the TensorFlow and Keras libraries, with Pandas and Scikit-learn used for data manipulation. Plotly and Matplotlib are used for visualizing the results of the experiments.

## Building and Running

This project is primarily based on Jupyter notebooks. To run the project, you will need to have a Python environment with the necessary libraries installed.

### Dependencies

The project requires the following Python libraries:

*   pandas
*   scikit-learn
*   keras
*   matplotlib
*   kaleido
*   plotly
*   tensorflow

You can install these dependencies using pip:

```bash
pip install pandas scikit-learn keras matplotlib kaleido plotly tensorflow
```

### Running the Notebooks

To run the experiments and optimizations, open and execute the Jupyter notebooks (`.ipynb` files) in a Jupyter environment. The notebooks are self-contained and include the code for data loading, model training, and evaluation.

The main notebooks for optimization are:

*   `06_optimizationTimesteps.ipynb`: Optimizes the number of timesteps used in the LSTM model.
*   `07_optimizationFeatures.ipynb`: Optimizes the set of features used for training the model.

Other notebooks in the `jupytersVastVersions` and `.conda/previous` directories contain previous versions of the optimization experiments.

### TODO: Add explicit build and test commands

The project does not currently have explicit build or test commands. For a more robust development workflow, it would be beneficial to add a build script and a suite of unit tests.

## Development Conventions

The project follows a set of conventions for development and experimentation:

*   **Jupyter Notebooks for Experimentation:** All experiments and optimizations are conducted in Jupyter notebooks. Each notebook is focused on a specific hyperparameter or aspect of the model.
*   **Model Saving:** The trained models are saved in the `saved_models` directory in `.h5` or `.keras` format.
*   **Results and Visualizations:** The results of the experiments, including plots and metrics, are saved in the `results` directory.
*   **Parameter Optimization:** The `optimzationParams.md` file documents the parameters that have been optimized and the results of the optimizations.
*   **Profit Function:** The models are evaluated not only on accuracy but also on a custom profit function, which is defined in the notebooks.
*   **Code Structure:** The code is organized into functions for data preparation, model building, experimentation, and visualization. This modular structure makes it easier to reuse and modify the code.
