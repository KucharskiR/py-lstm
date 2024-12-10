## Libraries:

Imports necessary libraries like numpy, pandas, tensorflow etc. for data manipulation, model building, and visualization.

## Data Preparation:

- Defines a function data that reads CSV files containing financial data, preprocesses it (scaling, selecting features) and splits it into training and testing sets.

## Model Building:

- Defines a function fit_lstmModel that takes various parameters like neurons, epochs, dropout etc. and builds an LSTM model with those configurations. It uses the Sequential API from Keras to create the model.
- The model architecture uses one or two LSTM layers with dropout regularization, followed by a dense layer with sigmoid activation for binary classification (buy/sell signals).
- The function also defines callbacks for saving the best model based on validation loss and early stopping to prevent overfitting.

## Experiment:

- Defines a function experiment that runs the training process multiple times (repeats) and evaluates the model's performance on unseen test data.
- It calculates accuracy and profit based on predicted buy/sell signals compared to actual price movements.
- The function also saves model training history (metrics) for later analysis.

## Output and Visualization:

- Defines a function plotsOut that uses Plotly to visualize the training history (accuracy, loss, profit) for each experiment run.

## Running the Script:

- Sets various parameters like learning rate, model architecture (model), dropout rate, epochs etc.
- Loops through different configurations like timestep size and calls the experiment function to train and evaluate the model for each configuration.
- Finally, it summarizes the results and creates visualizations.

## Key Points:

- The script utilizes Keras for building and training the LSTM model.
- It uses various techniques like dropout regularization and early stopping to improve model performance.
-The script defines custom functions for data preparation, model building, experiment execution, and visualization.
- It evaluates the model based on both accuracy and a custom profit function.