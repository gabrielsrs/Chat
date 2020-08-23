class Person:
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None

    def __set_name__(self, name):
        self.name = name

    def __repr__(self):
        return f"Personal ({self.addr}, {self.name}) "
