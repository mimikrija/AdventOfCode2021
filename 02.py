# Day 2: Dive!

from santas_little_helpers import *

def find_position(instructions, is_part_2=False):
    MOVE = {
    'forward': 1+0j,
    'down': 0+1j,
    'up': 0-1j,
    }

    position = 0+0j
    aim = 0
    depth = 0
    for direction, qt in instructions:
        position += MOVE[direction]*qt
        aim += MOVE[direction].imag*qt
        if is_part_2 and direction == 'forward':
            depth += aim*qt
            position = complex(position.real, depth)
    return position

solution_format = lambda x: int(x.real * x.imag)


raw_instructions = get_input('inputs/02.txt')

instructions = [(line.split()[0], int(line.split()[1])) for line in raw_instructions]
party_1, party_2 = (solution_format(find_position(instructions, is_part_2)) for is_part_2 in {False, True})

print_solutions(party_1, party_2)
