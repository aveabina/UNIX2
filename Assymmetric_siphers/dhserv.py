import socket

HOST = '127.0.0.1'
PORT = 8080
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
c, a = sock.accept()
allowed_keys = [3, 17, 151, 197]

connect = 'Connect: ' + str(a)
print(connect)

fi = open('ports.txt','a+')
fi.write('\n' + connect + '; ')
fi.close() 

while True:
    data = c.recv(1024)
    data = data.decode('utf-8')
    if data:
        break
	
new_data = data.split(' ')
g = int(new_data[0])
p = int(new_data[1])
A = int(new_data[2])

if (g in allowed_keys) and (p in allowed_keys):
	
	b = int(input("Input b > "))		
	
	file = open('keys.txt', 'a+')
	file.write('\ Private key b: ' + str(b))
	file.close()
	
	B = pow(g, b) % p
	c.send(str(B).encode('utf-8'))
	c.close()
		
	K = pow(A, b) % p
	print("Key > " + str(K))
	input("Done.")
	
else:
	print('Unresolved private key!')
