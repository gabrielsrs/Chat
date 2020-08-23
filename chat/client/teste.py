from client import Client
import time

c1 = Client("Gabriel")
time.sleep(2)
c2 = Client("Tim")
time.sleep(2)
c2.send_message("hello")
time.sleep(2)
c2.send_message("whats up")
time.sleep(2)
c1.send_message("nothing much, hbu")
time.sleep(2)
c1.send_message("Boring..")

time.sleep(2)
c2.disconnect()
time.sleep(2)
c1.disconnect()


def update_messages():
    msgs = []

    run = True
    while run:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)

        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()