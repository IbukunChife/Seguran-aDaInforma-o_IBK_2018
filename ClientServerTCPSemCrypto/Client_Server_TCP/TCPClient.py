#!/usr/bin/python
from socket import *
serverName = '10.11.208.55'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = raw_input("Imput lower sentence");
clientSocket.sendto(message, (serverName,serverPort))
modifiedMessage= clientSocket.recv (1024)
print modifiedMessage
clientSocket.close()
