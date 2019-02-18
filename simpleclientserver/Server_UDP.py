from socket import *
from datetime import datetime

# Pick port to bind socket to
serverPort = 12003

# Create socket and bind to port
# -> use IPv4 and UDP (datagram)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

# Create default response
response = "Error: Invalid Request Format"

while (True):
    # Wait for message from client
    message, clientAddress = serverSocket.recvfrom(2048)

    # If message is in correct form, then send back date and time
    if (message.decode() == "What is the current date and time?"):
        today = datetime.now()
        response = today.strftime("Current Date and Time – %m/%d/%Y %H:%M:%S")
        serverSocket.sendto(response.encode(), clientAddress)
    # Otherwise send back default response
    else:
        serverSocket.sendto(response.encode(), clientAddress)
