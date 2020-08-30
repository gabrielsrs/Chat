from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person
# a client object and each client object storage a ip address and a name(in a list for each client)

# Global constants
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512

# Global variables
persons_added = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)  # set up server


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

    # first message receive is always the person name
    name = client.recv(BUFSIZ).decode("utf8")
    person.set_name(name)
    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "")  # broadcast welcome message

    while True:  # wait for messages from person
        try:
            msg = client.recv(BUFSIZ)

            if msg == bytes("{quit}", "utf8"):  # if message is quit disconnect classe
                client.close()
                persons_added.remove(person)
                broadcast(bytes(f"{name} has left the chat...", "utf8"), "")

                print(f"[DISCONNECTED] {name} disconnected.")
                break

            else:  # otherwise send message to all other clients
                broadcast(msg, name + ": ")
                print(f"{name}: ", msg.decode('utf8'))

        except Exception as e:
            print("[EXCEPTION]", e)
            break


def wait_for_connections():
    """
    wait for connections from new clients, start new thread once connected
    :param SERVER: socket
    :return: none
    """

    while True:
        try:
            client, addr = SERVER.accept()  # wait for any new connections
            person = Person(addr, client)  # creating new person for connection
            persons_added.append(person)

            print(f"[CONNECTION] {addr} connected to the server at {time.time()}.")
            Thread(target=client_communication, args=(person,)).start()
        except Exception as e:
            print("[EXCEPTION]", e)
            break

    print("Server crashed")


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)  # open server to list for MAX_CONNECTIONS accept
    print("[STARTED] Waiting for connections...")
    ACCEPT_THREAD = Thread(target=wait_for_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
