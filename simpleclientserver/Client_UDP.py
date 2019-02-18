from socket import *

# Server information and constants
serverPort = 12003
serverIP = "192.168.2.209"
failed_response = "Error: Invalid Request Format"

# Create socket: using IPv4 and UDP (datagram)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set response to failed_response so loop runs at least once
response = failed_response

# Continue to ask for user input if failed_response sent back
while (response == failed_response):
    # Get user input and send message to server (specify socket addr)
    message = input("Input server request: ")
    clientSocket.sendto(message.encode(), (serverIP, serverPort))

    # Receive server response
    response, serverAddress = clientSocket.recvfrom(2048)
    response = response.decode()

    print(response)

# Date/time has been retrieved, close the connection.
clientSocket.close()
