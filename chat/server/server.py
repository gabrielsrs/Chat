from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person
# a client object and each client object storage a ip address and a name(in a list for each client)

# Global constants
HOST = 'localhost'
PORT = 5500
ADOR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512

# Global variables
persons_added = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADOR)  # set up server


def broadcast(msg, name):
    """
    Send new messages to all clients
    :param msg:bytes["utf8"]
    :param name: srt
    :return: None
    """
    for person in persons_added:
        client = person.client
        client.send(bytes(name, "utf8") + msg)


def client_communication(person):
    """
    Receive a message of the client and send a broadcast function.
    If this message left this server, them would remove this client and disconnect that socket.
    :param person: Person(class)
    :return: none
    """

    client = person.client

    # get persons name
    name = client.recv(BUFSIZ).decode("utf8")
    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "")  # broadcast welcome message

    while True:
        try:
            msg = client.recv(BUFSIZ)
            print(f"{name}: ", msg.decode('utf8'))

            if msg == bytes("{quit}", "utf8"):
                broadcast(f"{name} has left the chat...", "")
                client.send(bytes("{quit}", "utf8"))
                client.close()

                persons_added.remove(person)
                break

            else:
                broadcast(msg, name + ": ")

        except Exception as e:
            print(f"[EXCEPTION] {e}")
            break


def wait_for_connections():
    """
    wait for connections from new clients, start new thread once connected
    :param SERVER: socket
    :return: none
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons_added.append(person)

            print(f"[CONNECTION] {addr} connected to the server at {time.time()}.")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print(f"[EXCEPTION] {e}")
            run = False

    print("Server crashed")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)  # List for MAX_CONNECTIONS accept
    print("[STARTED] Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connections, args=(SERVER,))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
