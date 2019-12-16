# Palatip Wongyeekul (5910406329)
# Phatchanya Chongsheveewat (5910406337)

from socket import *
serverName = 'localhost'
serverPort = 12002
clientSocket = socket(AF_INET,SOCK_DGRAM)
while 1:
    
    message = input("> ")
    if(message == 'exit'):
        break
    clientSocket.sendto(message.encode(),(serverName,serverPort)) 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    if(modifiedMessage.decode() == "200"):
        print("Add Success")
    elif(modifiedMessage.decode() == "404"):
        print("Send Again")
    else:
        print(modifiedMessage.decode())
clientSocket.close()
