from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Global constants
HOST = "localhost"
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

# Global variables
messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messages():
    """
    Receive message from server
    :return:None
    """
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            messages.append(msg)
            print(msg)

        except Exception as e:
            print(f"[EXCEPTION] {e}")
            break


def send_message(msg):
    """
    Send message to server
    :param msg: None
    :return:
    """
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("Gabriel")
send_message("Hello World")
