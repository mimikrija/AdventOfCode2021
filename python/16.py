from santas_little_helpers.helpers import *
from collections import deque

def to_binary(hex):
    return "".join(f"{byte:08b}" for byte in bytes.fromhex(hex))

def read_packet(packet, total_sum = 0):

    packet_version = int(''.join(packet.popleft() for _ in range(3)), 2)
    type_id = int(''.join(packet.popleft() for _ in range(3)), 2)
    total_sum += packet_version

    if type_id == 4:
        literal = ''
        while True:
            keep_reading = packet.popleft() == '1'
            literal += ''.join(packet.popleft() for _ in range(4))
            if not keep_reading:
                return int(literal, 2), total_sum
    else:
        length_type_id = packet.popleft()
        if length_type_id == '0':
            total_length = int(''.join(packet.popleft() for _ in range(15)), 2)
            len_diff = len(packet) - total_length
            while True:
                value, total_number = read_packet(packet)
                if len(packet) <= len_diff:
                    return value, total_sum + total_number
        else:
            number_of_subpackets = int(''.join(packet.popleft() for _ in range(11)), 2)
            for _ in range(number_of_subpackets):
                value, total_number = read_packet(packet)
                print('value ', value)
            return value, total_sum + total_number




data = [to_binary(line) for line in get_input('inputs/16.txt')]


for binary in data:
    print(read_packet(deque(binary)))
