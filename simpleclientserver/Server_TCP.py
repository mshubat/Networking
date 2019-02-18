from socket import *
from datetime import datetime

# Server information and constants
serverPort = 12003
serverIP = "192.168.2.198"
failed_response = "Error: Invalid Request Format"

# Create socket and bind to IP+Port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))


while (True):
    # Listen for a connection
    serverSocket.listen(1)
    # Accept connection and create connectionSocket
    connectionSocket, addr = serverSocket.accept()

    response = failed_response
    # Maintain connection untill successful response sent
    while (response == failed_response):
        # Receive request from client connection
        request = connectionSocket.recv(2048)

        # If message is in correct form, then send back date and time
        if (request.decode() == "What is the current date and time?"):
            today = datetime.now()
            response = today.strftime("Current Date and Time – %m/%d/%Y %H:%M:%S")
            connectionSocket.send(response.encode())
        # Otherwise send back default response
        else:
            connectionSocket.send(response.encode())
    # Once successful response is given, close the connection
    connectionSocket.close()
