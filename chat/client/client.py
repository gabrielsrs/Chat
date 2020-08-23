from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import time


class Client:
    """
    For communicate with server
    """
    # Global constants
    HOST = "localhost"
    PORT = 5500
    ADDR = (HOST, PORT)
    BUFSIZ = 512

    def __init__(self, name):
        """
        Init object and send name to server.
        :param name: str
        """
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock = Lock()  # synchronization mechanism provided by the threading module

    def receive_messages(self):
        """
        Receive message from server
        :return:None
        """
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode("utf8")

                # make sure memory is safe to access
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()

            except Exception as e:
                print("[EXCEPTION]", e)
                break

    def send_message(self, msg):
        """
        Send message to server
        :param msg: None
        :return:
        """
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()

    def get_messages(self):
        """
        :return a list of str messages
        :return: list[str]
        """

        messages_copy = self.messages[:]

        # make sure memory is safe to access
        self.lock.acquire()
        self.messages = []
        self.lock.release()

        return messages_copy

    def disconnect(self):
        self.send_message(bytes("{quit}", "utf8"))
