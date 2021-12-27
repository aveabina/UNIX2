import socket
import os
import datetime
import threading

dir = os.getcwd()

PORT = 9090
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Port: ", PORT)

def process(req):
    now = datetime.datetime.now()
    date = now.strftime("%a, %d %b %Y %H:%M:%S")

    with open("logs.txt", "a") as fi:
        print(f"Client> {addr}; Comand> {req}; Date/Time> {date}\n", file=fi)

    if req == 'pwd':
        return os.getcwd()
    elif req == 'ls':
        return os.listdir(dir)
    elif 'mkdir' in req:
        req = req[6:]
        os.mkdir(req)
        return ("Added directory:" + req)
    elif 'rmdir' in req:
        req = req[6:]
        os.rmdir(req)
        return("Deleted directory:" + req)
    elif 'rmfile' in req:
        req = req[7:]
        os.remove(req)
        return("Deleted file:" + req)
    elif 'mkfile' in req:
        req = req[7:]
        open(req, "w")
        return("Added file:" + req)
    elif 'rename' in req:
        req1 = req.split(" ")[1]
        req2 = req.split(" ")[2]
        os.rename(req1,req2)
        return(req1 + " renamed to " + req2)
    elif 'chdir' in req:
        req = req[6:]
        os.chdir(req)
        return("Go to directory: " + req) 
    elif req == 'exit':
        sock.close()
        return("Stop server.")

def checking(li):
    ans = li.split(',')[0]
    name = li.split(',')[1]
    pswd = li.split(',')[2]
    if ans == '1':
        now = datetime.datetime.now()
        date = now.strftime("%a, %d %b %Y %H:%M:%S")
        with open("users.txt", "a+") as f:
            print(f"{name}:{pswd}:{date}\n", file=f)
        os.mkdir(name)
        return("Success autorization!")

    elif ans == "2":
        check = 0
        with open("users.txt", "r") as f:
            for line in f:
                if line.split(':')[0] == name:
                    check = 1
                    if line.split(':')[1][-1] == pswd:
                        print("Success log in!")
                    else:
                        print("Invalid password!")
        if check == 0:
            print("Login not found")
    os.chdir(name)
    dir = os.getcwd()

def Connect(conn, addr):    
        li = conn.recv(1024).decode()
        response1 = checking(li)
        conn.send(response1.encode())        


        while True:
            conn, addr = sock.accept()
            request = conn.recv(1024).decode()
            print(request)
            response2 = process(request)
            conn.send(response2.encode())
        
        conn.close()

while True:
    conn, addr = sock.accept()
    print("Client: ", addr, "\n")
    tr = threading.Thread(target=Connect, args=(conn, addr))
    tr.start()   
