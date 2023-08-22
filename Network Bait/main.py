import os 
import socket
import random
from datetime import datetime

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
white = "\033[1;37m"

s = socket.socket()
port = 8080
ip_address = socket.gethostbyname(socket.gethostname())

s.bind((ip_address, port))
os.system("clear")
print(f"{green}[+]{white} We are live on {port}")
s.listen(5)
print(f"""{green}[+]{white} Hosted at {ip_address}:{port}
{green}[+]{white} Waiting for connections...""")

while True:
    c, addr = s.accept()
    num = random.randint(1,9) # bait to make it look like they get something if they connect to the ip
    c.send(f"Welcome to our server! Your random number is {num}. Please connect to us again!\n".encode())
    time = datetime.now()
    time_on_conn = time.strftime("%H:%M:%S")
    print(f"{red}[$$ KOALA-LOGGER $$]{yellow} [{time_on_conn}]{white} Got a connection from {addr}")
    c.close()