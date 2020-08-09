import socket,time
from _thread import start_new_thread
import pickle,time
from game import Game

server = "192.168.0.106"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()


idCount = 0
Games = {}


 
def handle_client(conn,p,gameId):
    global idCount
    print(idCount)
    conn.send(str.encode(str(p)))
    while True:
        try:
            data = conn.recv(4000).decode()
            # print(data)
            if gameId in Games:
                game = Games[gameId]
                if not data:
                    print("Disconnected")
                    break
                else:
                    if data == 'reset':                        
                        game.reset() 
                    elif data != 'get':
                 
                        game.play(p,data)
                # print("Sending ",game.ready)     
                conn.sendall(pickle.dumps(game))
            else:
                print("not in list")
                break

        except socket.error as e:
            print(str(e))
            break
    print("Lost Connection")
    conn.sendall(str.encode('quit'))
    try:
        print('idCount',idCount)
        idCount -= 1
        del Games[gameId]
        print("Exisiting game is deleted",gameId)
        print(idCount)
    except:
        pass
    
    # time.sleep(2)
   



    

def main():
    global idCount
    gameId = 0
    while True:
        conn,addr = s.accept()
        print(f"connected to {conn.getpeername()}")
        idCount += 1
        p = 0
        if idCount % 2 == 1:
            gameId = idCount - 1 // 2
            print(gameId)
            Games[gameId] = Game(idCount)
            print(f"Player {p} is waiting ...")
        else:
            p = 1
            print(gameId)
            Games[gameId].ready = True
        start_new_thread(handle_client,(conn,p,gameId))
        
print("Waiting For Connection")
main()