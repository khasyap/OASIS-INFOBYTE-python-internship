import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except ConnectionAbortedError:
            print("Connection was closed by the server.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 12345))
    except Exception as e:
        print(f"Failed to connect to the server: {e}")
        return

    print("Connected to the server. Type your messages below.")
    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                client.send('Client has left the chat.'.encode('utf-8'))
                break
            client.send(message.encode('utf-8'))
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    client.close()

if __name__ == '__main__':
    start_client()
