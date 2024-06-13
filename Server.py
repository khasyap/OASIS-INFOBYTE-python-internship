import socket
import threading

def handle_client(client_socket, client_address, clients):
    print(f"[NEW CONNECTION] {client_address} connected.")
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"[{client_address}] {message}")

            for client in clients:
                if client != client_socket:
                    client.send(f"[{client_address}] {message}".encode('utf-8'))
    except ConnectionResetError:
        pass
    finally:
        print(f"[DISCONNECT] {client_address} disconnected.")
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen()

    print("[STARTING] Server is starting...")

    clients = []
    while True:
        client_socket, client_address = server.accept()
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, client_address, clients))
        client_handler.start()

if __name__ == '__main__':
    start_server()
