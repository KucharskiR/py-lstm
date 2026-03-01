import socket
import numpy as np
import tensorflow as tf
from keras.models import load_model
import os

# Configuration
TIMESTEPS = 10
FEATURES = 21  # Matches the updated MQL generateFunc.mqh (21 columns)
MODEL_PATH = "./saved_models/last_saved_model.keras"
HOST = '127.0.0.1'
PORT = 12345

print(f"TensorFlow version: {tf.__version__}")

# Load model
if os.path.exists(MODEL_PATH):
    # compile=False since we only use it for prediction
    model = load_model(MODEL_PATH, compile=False)
    print(f"Model loaded successfully from {MODEL_PATH}")
    model.summary()
else:
    print(f"CRITICAL ERROR: Model file not found at {MODEL_PATH}")
    print("Please train the model in Jupyter first using 'features = 3' setting.")
    exit()

def process_data(data_received):
    try:
        # Clean input and split into rows
        lines = data_received.strip().split('\n')
        float_rows = []
        for line in lines:
            if not line.strip():
                continue
            # Split by semicolon as defined in MQL generateData()
            values = [float(v) for v in line.split(';') if v.strip()]
            if len(values) == FEATURES:
                float_rows.append(values)
        
        # Validation: check if we have enough timesteps for a single prediction
        if len(float_rows) < TIMESTEPS:
            print(f"Warning: Received only {len(float_rows)} valid rows, expected {TIMESTEPS}")
            return "0"
            
        # Take the last TIMESTEPS rows if more were sent
        float_rows = float_rows[-TIMESTEPS:]

        # Reshape to (samples, timesteps, features) -> (1, 10, 21)
        data = np.array(float_rows).reshape(1, TIMESTEPS, FEATURES)
        
        # Run prediction
        # Output shape is (1, 2) where [0][0] is Sell prob and [0][1] is Buy prob
        result = model.predict(data, verbose=0)
        p_sell = result[0][0]
        p_buy = result[0][1]
        
        print(f"Inference - Buy Prob: {p_buy:.4f}, Sell Prob: {p_sell:.4f}")

        # Signal Logic (Code 3: Buy, Code 5: Sell, Code 0: None)
        # These codes match the original PythonServerLstm_v.1.1.py
        if p_buy > 0.7 and p_buy > p_sell:
            print(">>> SIGNAL: BUY (3)")
            return "3"
        elif p_sell > 0.7 and p_sell > p_buy:
            print(">>> SIGNAL: SELL (5)")
            return "5"
        else:
            return "0"
            
    except Exception as e:
        print(f"Error processing received data: {e}")
        return "0"

# Initialize Socket Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allow immediate reuse of the port after restart
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind((HOST, PORT))
except socket.error as e:
    print(f"Bind failed. Error: {e}")
    exit()

server_socket.listen(1)
print(f'Production Server v1.2 listening on {HOST}:{PORT}...')

while True:
    client_socket, addr = server_socket.accept()
    print(f'New connection from {addr}')
    
    try:
        while True:
            # Buffer size increased to 8KB to handle 21 features string comfortably
            dataIn = client_socket.recv(8192).decode('utf-8')
            if not dataIn:
                break
            
            # print(f"Received raw data length: {len(dataIn)}")
            response = process_data(dataIn)
            client_socket.send(response.encode('utf-8'))
            
    except Exception as e:
        print(f"Socket session error: {e}")
    finally:
        client_socket.close()
        print("Client disconnected. Waiting for next connection...")