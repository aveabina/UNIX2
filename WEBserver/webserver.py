import socket
import os
import webbrowser
import datetime
import threading
from settings import cport, eport, dir, maxsize
types = ['html', 'css', 'js', 'png', 'gif', 'jpeg'] 

def GetWay(conn, addr, data, dir):
    msg = data.decode()
    print(msg)
    search = msg.split()[1][1:]
    check = search.split('.')
    if check[1] not in types:
        search = "er403.html"
    elif search == "" or os.path.exists(search)==False:
        search = "er404.html"
    search = dir + "/" + search
    webbrowser.open(search)
    now = datetime.datetime.now()
    date = now.strftime("%a, %d %b %Y %H:%M:%S")

    with open("logs.txt", "a") as f:
        if search == dir + "/er403.html":
            print(f"ERROR: 403\nDate/Time> {date}\nIP> {addr}\nFile> {search}", file=f)
        elif search == dir + "/er404.html":
            print(f"ERROR: 404\nDate/Time> {date}\nIP> {addr}\nFile> {search}", file=f)
        else:
            print(f"Date/Time> {date}\nIP> {addr}\nFile> {search}", file=f)
    try:
        size = os.path.getsize(search)

    except FileNotFoundError:
        resp = f"""HTTP/1.1 404 Not Found
	ERROR 404
	Date/Time> {date}"""
        with open("logs.txt", "a") as f:
            print("Error> 404", file=f)

        resp = resp.encode()
    else:
        decr = search.split(".")[-1]
        if decr not in types:
            resp = f"""HTTP/1.1 403 Access Denied 
	    ERROR 403 
	    Date/Time> {date}"""
            with open("logs.txt", "a") as f:
                print("Error> 403", file=f)
        else:
            try:
                with open(search, "r", encoding="utf-8") as file:
                    resp = f"""HTTP/1.1 200 OK
                    Date/Time> {date}
                    Content-Type> text/{decr};charset=utf-8
                    Content-Length> {size}
                    """
                    resp += file.read()
                resp = resp.encode()
            except UnicodeDecodeError:
                resp = f"""HTTP/1.1 200 OK
                Date/Time> {date}
                Content-Type> image/{decr}
                Content-Length> {size}
                """
                fi = open(search, 'rb')
                c = fi.read()
                fi.close()
                resp=c
    conn.send(resp)

def Connect(conn, addr, dir):
    data = conn.recv(maxsize)
    if not data:
        return
    GetWay(conn, addr, data, dir)
    conn.close()

sock = socket.socket()
try:
    sock.bind(('', cport))
    print(f"Port: {cport}")
except OSError:
    sock.bind(('', eport))
    print(f"Port: {eport}")
sock.listen(5)
conn, addr = sock.accept()

while True:
    print("Client: ", addr, "\n")
    tr = threading.Thread(target=Connect, args=(conn, addr, dir))
    tr.start()
    conn, addr = sock.accept()
