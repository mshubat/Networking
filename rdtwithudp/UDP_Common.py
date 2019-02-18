import struct
import hashlib

packet_struct = struct.Struct('I I 8s 32s')
unpacker = struct.Struct('I I 8s 32s')


def create_checksum(values):
    # Populate the struct.
    temp_struct = struct.Struct('I I 8s')
    packed_data = temp_struct.pack(*values)

    # Compute the checksum.
    chksum = bytes(hashlib.md5(packed_data).hexdigest(), encoding="UTF-8")

    return chksum


def buildpacket(values, chksum):
    # Append checksum to list of values.
    values.append(chksum)

    # Pack the struct with values and checksum.
    pkt = packet_struct.pack(*values)

    return pkt


def unpack(pkt):
    return unpacker.unpack(pkt)
