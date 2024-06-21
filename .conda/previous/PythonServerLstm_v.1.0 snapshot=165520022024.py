import socket
import time

def process_data(data_received):
    # Implement your processing logic here
    result = f"Processed: {data_received.upper()}"
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
    data_received = client_socket.recv(1024).decode()
    print('Data received from MQL:', data_received)

    # Process data
    processed_data = process_data(data_received)

    # Send processed data back to MQL
    client_socket.send(processed_data.encode())

    # # Wait for 5 minutes before the next iteration  
    # time.sleep(300)                       <--- to prawdopodobnie nie będzie potrzebne