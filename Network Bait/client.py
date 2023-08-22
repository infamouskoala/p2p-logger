import socket
print("connecting...")
koala = socket.socket()

ip = input("ip: ") # or set this manually 
port = int(input("port: ")) # or set this manually aswell

koala.connect((ip, port))
koala.send("hello from koala!".encode())