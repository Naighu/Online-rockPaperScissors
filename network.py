import socket
import pickle
from game import Game
class Network():
    def __init__(self):
        self.server = "192.168.0.106"
        self.port = 5555
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.id = self.connect()
    def get_P(self):
        return int(self.id)
    def connect(self):
        addr = (self.server,self.port)
        self.client.connect(addr)
        return self.client.recv(4000).decode()
    def send(self,data):
        self.client.send(str.encode(data))
        try:
            result = pickle.loads(self.client.recv(4000))
            return result
        except socket.error as e:
            print(str(e))
            result = Game(self.get_P()) 
            result.quit = True
            return result
            
                