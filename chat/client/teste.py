from client import Client
from threading import Thread
import time

c1 = Client("Gabriel")
c2 = Client("Tim")
c3 = Client("name")


def update_messages():
    """
    Updates the local list of messages
    :return: None
    """
    msgs = []

    run = True
    while run:
        time.sleep(0.1)  # update every 1/10 of a second
        new_messages = c1.get_messages()  # get any new message from client
        msgs.extend(new_messages)  # add to local list of messages

        for msg in new_messages:  # display new messages
            print(msg)

            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()

c2.send_message("hello")
time.sleep(5)
c2.send_message("whats up")
time.sleep(5)
c1.send_message("nothing much, hbu")
time.sleep(5)
c1.send_message("Boring..")

time.sleep(5)
c2.disconnect()
time.sleep(5)
c1.disconnect()
time.sleep(5)
c3.disconnect()
