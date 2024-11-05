import socket
import json

# Sample data to send
data = { "type": "oussama", "model": "HP42et", "serie": "24524de52f3", "inventaire": "IN42001", "createdBy": "UserA", "client": "HABOUS" }

json_data = json.dumps(data)

host = '' # write the ip here
port = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))
    client_socket.sendall(json_data.encode())
    
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")
finally:
    client_socket.close()