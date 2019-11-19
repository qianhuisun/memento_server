# import kairos library
# from database import Database
from socket import * 
import threading
import _thread

class Server(object):

    def __init__(self):
        print("__init__:")
        self.glassServerSocket = socket(AF_INET, SOCK_STREAM) # for handling request from google glass
        self.phoneServerSocket = socket(AF_INET, SOCK_STREAM) # for handling request from cell phone
        self.glassPort = 8088
        self.phonePort = 8089
    

    def runServer(self):
        print("runServer:")
        glassServerThread = threading.Thread(target=Server.startGlassServer, args=(self,))
        phoneServerThread = threading.Thread(target=Server.startPhoneServer, args=(self,))
        glassServerThread.start()
        phoneServerThread.start()
        print("server is running!")


    def handleGlassConnection(self, conn):
        print("handleGlassConnection:")
        # TODO


    def handlePhoneConnection(self, conn):
        print("handlePhoneConnection:")
        # TODO


    def startGlassServer(self):
        print("startGlassServer:")
        try:
            self.glassServerSocket.bind(('localhost', self.glassPort))
            print("GlassServerSocket binded to port: ", self.glassPort)
            self.glassServerSocket.listen(5)
            print("GlassServerSocket is listening")

            while True:
                #user_input = input()
                conn = "conn"
                #conn, addr = self.glassServerSocket.accept()
                glassConnectionThread = threading.Thread(target=Server.handleGlassConnection, args=(self, conn))
                glassConnectionThread.start()
        
        except KeyboardInterrupt:
            print("\nShutting down GlassServerSocket ...\n")
        
        self.glassServerSocket.close()


    def startPhoneServer(self):
        print("startPhoneServer:")
        try:
            self.phoneServerSocket.bind(('localhost', self.phonePort))
            print("PhoneServerSocket binded to port: ", self.phonePort)
            self.phoneServerSocket.listen(5)
            print("PhoneServerSocket is listening")

            while True:
                #user_input = input()
                conn = "conn"
                #conn, addr = self.phoneServerSocket.accept()
                phoneConnectionThread = threading.Thread(target=Server.handlePhoneConnection, args=(self, conn))
                phoneConnectionThread.start()

        except KeyboardInterrupt:
            print("\nShutting down PhoneServerSocket ...\n")
        
        self.phoneServerSocket.close()
        

server = Server()
server.runServer()