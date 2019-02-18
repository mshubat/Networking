from socket import *

# Server information and constants
serverPort = 12003
serverIP = "192.168.2.198"
failed_response = "Error: Invalid Request Format"

# Create socket (IPv4, TCP) and bind to server socket address (IP,Port)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

# Set response to failed_response so loop runs at least once
response = failed_response

# Continue to ask for user input if failed_response sent back
while (response == failed_response):
    # Get user input and send message to connected server
    sentence = input("Input server request: ")
    clientSocket.send(sentence.encode())

    # Receive server response
    response = clientSocket.recv(2048)
    response = response.decode()

    print(response)

# Date/time has been retrieved, close the connection.
clientSocket.close()
