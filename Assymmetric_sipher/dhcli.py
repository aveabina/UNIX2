import socket

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

data = input("Input g p a > ")
new_data = data.split(' ')
g = int(new_data[0])
p = int(new_data[1])
a = int(new_data[2])

file = open('keys.txt','a+')
file.write('\ Public key g: ' + str(g))
file.write('\ Private key a: ' + str(a))
file.write('\ Public key p: ' + str(p))
file.close()


A = pow(g, a) % p
new_data[2] = str(A)
data = ' '.join(new_data)
data = data.encode('utf-8')
sock.send(data)

data = sock.recv(1024)
B = int(data.decode('utf-8'))
K = pow(B, a) % p
sock.close()

print("Key > " + str(K))
input("Done.")
