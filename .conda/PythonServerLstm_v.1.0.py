import socket
import time
import numpy as np
import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import LambdaCallback
from keras.initializers import TruncatedNormal
from keras.models import save_model
from keras.models import load_model
import os

print(tf.__version__)


# Read model
model = tf.keras.models.load_model(filepath=r"./lstm_Model.h5", compile=False)
print(model.summary())

def process_data(data_received):
    # Split the string into rows based on '\n' and then split each row into values based on ';'
    rows = [row.split(';') for row in data_received.split('\n')]

    # Convert the string values to floating-point numbers
    float_rows = [[float(value) for value in row] for row in rows]

    # Convert the list of lists to a NumPy array
    data = np.array(float_rows)
    print(data)
    data = data.reshape(1, 120, 8)

    # Get result
    result = np.argmax(model.predict(data), axis=-1)
    print(result)
    return result

# Define host and port
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()
print('Waiting for connection')

# Accept a connection
client_socket, addr = server_socket.accept()
print('Connection from', addr)

while True:
    # Receive data from MQL
    dataIn = client_socket.recv(1024).decode()
    print('Data received from MQL:', dataIn)

    # Process data
    processed_data = process_data(dataIn)

    # Send processed data back to MQL
    client_socket.send(processed_data.encode())

    # # Wait for 5 minutes before the next iteration  
    # time.sleep(300)                       <--- to prawdopodobnie nie będzie potrzebne