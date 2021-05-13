#TCP SERVER 

from socket import *

#porta do servidor
serverPort = 8000

# cria socket TCP
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(1)

# 
print ("Server ON ... ")
print ("Aguardando mensagens ... ")


while 1:
    # servidor aguarda por requisição
    connectionSocket, addr = serverSocket.accept()
     
    # leitura da mensagem enviada pelo cliente na porta 1024
    numero1 = connectionSocket.recv(1024)
    
    # mostra a mensagem recebida do cliente
    print ("Mensagem Recebida: ", numero1.decode("UTF-8") , " de ", addr)

    #mostra o tipo de dados da mensagem
    print (numero1)
    
    #altera o tipo do dado para integer
    numero1 = numero1.decode("utf-8")
    print(type(numero1))
    
    # leitura da mensagem enviada pelo cliente na porta 1024
    numero2 = connectionSocket.recv(1024)
        
    # mostra a mensagem recebida do cliente
    print ("Mensagem Recebida: ", numero2.decode("UTF-8") , " de ", addr) 
    
    # mostra o tipo de dados da mensagem
    print (numero2)
    
    #altera o tipo do dado para integer
    numero2 = numero2.decode("utf-8")
    print(type(numero2))
    
    # realiza a soma 
    resultado = int(numero1) + int(numero2)
    print ("soma: ", resultado)
    
    #altera o tipo do dado da soma de integer para string
    resultado = str(resultado)
    print(type(resultado))
    
    # envia a resposta da som para o cliente
    connectionSocket.send(bytes(resultado, "utf-8"))
   
    # mostra a mensagem enviada para cliente
    print ("Mensagem Enviada:", resultado)
	 
    # fecha a conexão
connectionSocket.close()