from socket import socket, AF_INET, SOCK_DGRAM
import UDP_Common as common

# LoopBack Address and Port Number Set here.
UDP_IP = "127.0.0.1"
UDP_PORT = 6005


# Create the socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Initial message has sequence number 0.
expected_seq = 0


while True:
    # Receive Data
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes.
    UDP_Packet = common.unpack(data)
    print("Message from Client:", UDP_Packet)

    # Create the Checksum for comparison.
    values = [UDP_Packet[0], UDP_Packet[1], UDP_Packet[2]]
    chksum = common.create_checksum(values)

    # Compare Checksums to test for corrupt data.
    if UDP_Packet[3] == chksum:
        print('CheckSums Match, Packet OK')

        ack_values = [1, UDP_Packet[1], b'']

        # If expected sequence number then update for new expected seq.
        if UDP_Packet[1] == expected_seq:
            expected_seq = 1 - expected_seq

    else:
        print('Checksums do not match. Packet Corrupt.')

        ack_values = [1, 1-expected_seq, b'']

    # Create the Checksum for the message and build the packet.
    chksum = common.create_checksum(ack_values)
    pkt = common.buildpacket(ack_values, chksum)

    # Print the packet contents and send to client.
    print("Message to Client: ", common.unpack(pkt))
    sock.sendto(pkt, addr)
