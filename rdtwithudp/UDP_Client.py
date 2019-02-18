from socket import socket, AF_INET, SOCK_DGRAM, timeout
import UDP_Common as common

# LoopBack Address and Port Number Set here.
UDP_IP = "127.0.0.1"
UDP_PORT = 6005


def sendmessage(messages):
    # Initial message has sequence number 0.
    seq = 0

    # Process each message.
    for m in messages:
        mssg = bytes(m, encoding='utf-8')

        # Store message in values array and compute the checksum.
        values = [0, seq, mssg]
        chksum = common.create_checksum(values)

        # Build the packet with value and checksum.
        pkt = common.buildpacket(values, chksum)

        # Send the packet with rdt_send.
        rdt_send(pkt, seq)

        # Update sequence number.
        seq = 1 - seq


def rdt_send(packet, seq):
    # Create the socket with 9ms timeout.
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.settimeout(0.009)

    ACK_received = False

    while not ACK_received:
        # Print and Send the packet.
        print("Message to Server: ", common.unpack(packet))
        sock.sendto(packet, (UDP_IP, UDP_PORT))

        try:
            # Wait for acknowledgment from Server.
            data, server_addr = sock.recvfrom(1024)
        except timeout:
            print("Timeout reached. Packet is being resent.")
        else:
            # Unpack and print server response.
            server_response = common.unpack(data)
            print("Response from Server: ", server_response)

            # Get message body and compute checksum.
            values = [server_response[0], server_response[1], server_response[2]]
            chksum = common.create_checksum(values)

            # Check if ACK, NACK, or corrupt.
            if seq != server_response[1]:
                print("ACK with wrong sequence number received.")
            elif chksum != server_response[3]:
                print("Garbled ACK received.")
            else:
                print("Checksums Match, Packet OK.")
                ACK_received = True


if __name__ == '__main__':
    # Create messages to be sent.
    messages = ['NCC-1701', 'NCC-1664', 'NCC-1017']

    # Send the messages.
    sendmessage(messages)
