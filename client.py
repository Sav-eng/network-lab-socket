
# Python program to implement client side of chat room.  
import socket  
import select  
import sys  
from _thread import *
import time

def sending_thread():
    while True:
        message = input()
        server.sendall(str.encode(message))
        print("<You>"+message)
    

def receiving_thread():
    while True:
        message = server.recv(2048)
        print(message.decode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number") 
    exit()
IP_address = str(sys.argv[1])  
Port = int(sys.argv[2])  
server.connect((IP_address, Port))  

start_new_thread(sending_thread,())
start_new_thread(receiving_thread,())

time.sleep(1000)

server.close() 