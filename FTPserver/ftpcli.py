import socket
import threading
HOST = 'localhost'
PORT = 9090

def Log_in():
    while True:    
        choise = input('Enter "1" to create account, "2" to log in: ')
        log = input("Enter login:")
        passwd=input("Enter password: ")
        li = ''
        for i in choise, log, passwd:
            li = li + i + ','
        li = li.encode()

        sock = socket.socket()
        sock.connect((HOST, PORT))

        sock.send(li)
        response1 = sock.recv(1024).decode()
        print(response1)    

def Com():
    while True:
        request = input('>')

        sock = socket.socket()
        sock.connect((HOST, PORT))

        sock.send(request.encode())
        
        response2 = sock.recv(1024).decode()
        print(response2)
        
        if request == 'exit':
            sock.close()    
            break

threading.Thread(target=Log_in).start()
threading.Thread(target=Com).start()
