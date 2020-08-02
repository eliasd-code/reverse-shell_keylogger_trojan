import smtplib
from email.message import EmailMessage
import time
import sys
import socket
from threading import Thread
import os

#ACHTUNG!!
#bei Login problemen schauen ob die 'PO3' option im email user aktiv ist !
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
        def datei_stockt(datei_name_stockt): #Datei verschieben
                with open(datei_name_stockt,"r")as old_file:        # von datei in neue datei schreiben
                        with open("clogged","a")as new_file:
                                for element in old_file:
                                        new_file.write(element)
                old_file.close()
                new_file.close()
                while True:
                        ######
                        time.sleep(1800) #standart ist 1800 = 30 min
                        if connection_on==1:    # jede 30 minuten prüfen ob eine verbindung besteht
                                with open("clogged","r")as read_file:
                                        msg = EmailMessage()
                                        msg.set_content(read_file.read())
                                        msg['Subject'] = f'The contents of {textfile}'
                                        msg['From'] = me
                                        msg['To'] = you
                                        s = smtplib.SMTP('mail.gmx.net',587)
                                        s.starttls()    
                                        s.login(me, password)   
                                        s.send_message(msg)     
                                        s.quit()
                                        time.sleep(300) # 5 minuten
                                        os.remove("clogged")
                                        time.sleep(5)
                                        break
        
        datei_stockt_args=[datei_pfad+datei_name]
        internet_checker=Thread(target=datei_stockt,args=datei_stockt_args)
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
                internet_checker.start()

