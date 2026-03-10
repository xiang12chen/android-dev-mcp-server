# MCP Server Implementation

import socket
import threading

class MCPServer:
    def __init__(self, host='0.0.0.0', port=9000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"MCP Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket):
        request = client_socket.recv(1024)
        print(f"Received: {request}")
        client_socket.send(b'ACK')
        client_socket.close()

    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == '__main__':
    server = MCPServer()
    server.run()