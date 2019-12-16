# Palatip Wongyeekul (5910406329)
# Phatchanya Chongsheveewat (5910406337)

from socket import *
from tinydb import TinyDB, where
import random
db = TinyDB('db.json')
key = ["",""]
def addword(clientAddress):
	
	serverSocket.sendto("Question : ".encode(),clientAddress)
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode()
	key[0] = modifiedMessage
	
	
	serverSocket.sendto("Answer : ".encode(),clientAddress)
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode()
	key[1] = modifiedMessage
	db.insert({key[0]:key[1]})
	
	serverSocket.sendto("200".encode(),clientAddress)

serverPort = 12002
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')    
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode()
	print(modifiedMessage)
	a = db.search(where(modifiedMessage))
	if a == []:
		serverSocket.sendto("Add word (y/n) ?".encode(),clientAddress)
		message, clientAddress = serverSocket.recvfrom(2048)
		modifiedMessage = message.decode()
		if(modifiedMessage=='Y' or modifiedMessage=='y'):
			addword(clientAddress)
		else:
			serverSocket.sendto("404".encode(),clientAddress)
			continue
	else:
		a =  random.choice([a for a in db.search(where(modifiedMessage))]) 
		serverSocket.sendto(a[modifiedMessage].encode(),clientAddress)
        