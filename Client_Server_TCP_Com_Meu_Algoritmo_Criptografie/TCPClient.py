#!/usr/bin/python
from socket import *

#Algoritmos de Criptografia_ Decriptocrafia
keys = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','j','J','i','I','k','K','l','L','n','N','m','M','o','O',
       'p','P','q','Q','r','R','s','S','t','T','x','X','y','Y','z','Z','u','U','v','V','w','W'] 
cKeys = ['*/501089/', '*/510311/', '*/541129/', '*/550519/','*/576899/','*/592087/','*/602887/','*/623719/','*/643619/',
         '*/682951/','*/662369/','*/693353/','*/697121/','*/700933/','*/713129/','*/734443/','*/750817/','*/764149/',
         '*/774577/','*/790429/','*/801407/','*/810239/','*/830279/','*/840467/','*/853949/','*/901339/','*/910519/',
         '*/920539/','*/930499/','*/944497/','*/960137/','*/997019/','*/989309/','*/478711/','*/455093/','*/430739/',
         '*/408979/','*/399473/','*/376949/','*/355933/','*/338579/','*/318457/','*/298247/','*/278801/','*/254977/',
         '*/238709/','*/218657/','*/199921/','*/178781/','*/158009/','*/99721/','*/89051/']

encryp = ''
decryp = ''

def simpleEncrypt(string):
    global keys
    global cKeys
    global encryp  
        
    for letter in string:
        if (letter.isalpha()):
            sid = keys.index(letter)
            encryp = encryp + cKeys[sid]
        else:
            encryp = encryp + letter
    #print (encryp)
    return encryp

def simpleDecrypt(string):
    global keys
    global cKeys
    global decryp
    i = 1
    dec = string.split('*')
    for setConj in dec:
        if (setConj == '' or setConj == ' '):
            continue
        if (setConj[-1] == '/'):
            decSet = '*' + setConj
            did = cKeys.index(decSet)
            decryp = decryp + keys[did]
        else:
            while setConj[-i] != '/':
                i= i+1
            decSet = '*' + setConj[:(-i+1)]
            did = cKeys.index(decSet)
            decryp = decryp + keys[did]+ setConj[(-i+1):]
        i=1
    #print (decryp)
    return decryp
##############################################


serverName = '10.11.208.55'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
informacao = raw_input("Imput lower sentence");
message= simpleEncrypt(informacao)
clientSocket.sendto(message, (serverName,serverPort))
modifiedMessage= clientSocket.recv (1024)
answers = simpleDecrypt(modifiedMessage)
print answers
clientSocket.close()
