from WebITS import client_request,get_res
import socket
from _thread import *
import threading
 
lock = threading.Lock()
 
def listenToClient(c):
    while True:
        # data received from client
        data = c.recv(1024).decode()
        if not data:
            print('Bye')
            break
        lock.acquire()
        client_request(data)
        c.send(get_res().encode())
        lock.release()
    # connection closed
    c.close()
 
 
def Main():
    host = "127.0.0.1"
    port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    while True:
        # establish connection with client
        c, addr = s.accept()
        threading.Thread(target=listenToClient,args=(c,)).start()
 
if __name__ == '__main__':
    Main()
