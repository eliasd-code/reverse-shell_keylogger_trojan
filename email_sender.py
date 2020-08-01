import smtplib
from email.message import EmailMessage
import time
import sys

#ACHTUNG!!
#bei Login problemen schauen ob die 'PO3' option im email user aktiv ist !
class email_sender_class:
    def email_sender_funk(self,datei_name):
        me=""   #Sender E-Mail
        password=""    #Password des senders
        you=""  #Empfänger E-Mail
        textfile="/tmp/"+datei_name       #text file die eingelesen und dessen inhalt verschickt werden soll

# Open the plain text file whose name is in textfile for reading.
        with open(textfile) as fp:
        # Create a text/plain message
            msg = EmailMessage()
            msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
        msg['Subject'] = f'The contents of {textfile}'
        msg['From'] = me
        msg['To'] = you

# Send the message via our own SMTP server.
        s = smtplib.SMTP('smpt.gmail.com',587)    # server und port auswählen
        s.starttls()    # verschlüsselung aktivieren
        s.login(me, password)   # beim server mit email und password einloggen
        s.send_message(msg)     # message senden
        s.quit()            # verbindung cappen
