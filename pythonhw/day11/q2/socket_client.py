from WebITS import client_request,get_res
import socket
 
 
def Main():
    host = '127.0.0.1'
    port = 1234
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect to server on local computer
    s.connect((host,port))
 
    # message you send to server
    while True:
        message = input("请输入你要翻译的话\n")
        # message sent to server
        s.send(message.encode())
 
        # message received from server
        data = s.recv(1024).decode()
 
        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :',data)
 
        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()
 
if __name__ == '__main__':
    Main()