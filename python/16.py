from santas_little_helpers.helpers import *
from collections import deque
from operator import add, mul, gt, lt, eq
from functools import reduce

OPERATORS = {
    0: add,
    1: mul,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq,
}

def pop_and_join(packet, num_of_pops):
    return ''.join(packet.popleft() for _ in range(num_of_pops))

def to_binary(hex):
    return "".join(f"{byte:08b}" for byte in bytes.fromhex(hex))

def calculate(operator, data):
    return int(reduce(OPERATORS[operator],data))

def read_packet(packet, packet_versions):

    packet_version = int(pop_and_join(packet, 3), 2)
    type_id = int(pop_and_join(packet, 3), 2)
    packet_versions.append(packet_version)


    if type_id == 4:
        literal = ''
        while True:
            keep_reading = packet.popleft() == '1'
            literal += pop_and_join(packet, 4)
            if not keep_reading:
                result = int(literal, 2)
                break
    else:
        length_type_id = packet.popleft()
        values = []
        if length_type_id == '0':
            total_length = int(pop_and_join(packet, 15), 2)
            len_diff = len(packet) - total_length
            while True:
                _, result = read_packet(packet, packet_versions)
                values.append(result)
                if len(packet) <= len_diff:
                    result = calculate(type_id, values)
                    break
        else:
            number_of_subpackets = int(pop_and_join(packet, 11), 2)
            for _ in range(number_of_subpackets):
                _, result = read_packet(packet, packet_versions)
                values.append(result)
            result = calculate(type_id, values)

    return sum(packet_versions), result


data = deque([to_binary(line) for line in get_input('inputs/16.txt')][0])

party_1, party_2 = read_packet(data, [])
print_solutions(party_1, party_2)
