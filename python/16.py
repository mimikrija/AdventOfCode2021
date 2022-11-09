from santas_little_helpers.helpers import *
from collections import deque

def to_binary(hex):
    return "".join(f"{byte:08b}" for byte in bytes.fromhex(hex))

def read_packet(packet, packet_versions=[]):

    packet_version = int(''.join(packet.popleft() for _ in range(3)), 2)
    type_id = int(''.join(packet.popleft() for _ in range(3)), 2)
    packet_versions.append(packet_version)


    if type_id == 4:
        literal = ''
        while True:
            keep_reading = packet.popleft() == '1'
            literal += ''.join(packet.popleft() for _ in range(4))
            if not keep_reading:
                break
                return int(literal, 2), packet_versions
    else:
        length_type_id = packet.popleft()
        if length_type_id == '0':
            total_length = int(''.join(packet.popleft() for _ in range(15)), 2)
            len_diff = len(packet) - total_length
            while True:
                read_packet(packet, packet_versions)
                if len(packet) <= len_diff:
                    break
        else:
            number_of_subpackets = int(''.join(packet.popleft() for _ in range(11)), 2)
            for _ in range(number_of_subpackets):
                read_packet(packet, packet_versions)

    return packet_versions


data = deque([to_binary(line) for line in get_input('inputs/16.txt')][0])



party_1 = sum(read_packet(data))

print_solutions(party_1)
