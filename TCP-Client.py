#TCP CLIENT 
from socket import *

#ip do servidor TCP
serverName = "192.168.0.191"

#porta do servidor TCP
serverPort = 8000


while True:
    #socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # abre a conexão TCP
    clientSocket.connect((serverName,serverPort))

    print ("Calculadora de soma de dois valores")
    
    # mensagem do usuario
    sentence = input("Digite o primeiro número: ")

    #envia a msg para o socket
    clientSocket.send(bytes(sentence, "utf-8"))

    #mostra a mensagem enviada ao servidor
    print ("Mensagem enviada ao servidor:  ", sentence)

    # mensagem do usuario
    sentence = input("Digite o segundo número: ")

    #envia a msg para o socket
    clientSocket.send(bytes(sentence, "utf-8"))
    
    #mostra a mensagem enviada ao servidor
    print ("Mensagem enviada ao servidor:  ", sentence)

    #recebe a mensagem modificada pelo servidor
    #na porta 1024
    modifiedSentence = clientSocket.recv(1024)
    
    # mostra a mensagem recebida do servidor
    print ("Resultado: ", modifiedSentence.decode("utf-8"))

    # fecha a conexão TCP
    clientSocket.close()