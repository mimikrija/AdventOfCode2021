# Day 2: Dive!

from itertools import accumulate

from santas_little_helpers.helpers import *


def find_position(instructions, is_part_2=False):
    MOVE = {
    'forward': 1+0j,
    'down': 0+1j,
    'up': 0-1j,
    }

    final_position = sum(MOVE[direction]*qt for direction, qt in instructions)
    if not is_part_2:
        return final_position

    aims = accumulate([MOVE[direction].imag*qt for direction, qt in instructions])
    depth = sum(aim*qt for (direction, qt), aim in zip(instructions, list(aims)) if direction == 'forward')
    return complex(final_position.real, depth)

solution_format = lambda x: int(x.real * x.imag)


raw_instructions = get_input('inputs/02.txt')

instructions = [(line.split()[0], int(line.split()[1])) for line in raw_instructions]
party_1, party_2 = (solution_format(find_position(instructions, is_part_2)) for is_part_2 in {False, True})

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 2187380
def test_two():
    assert party_2 == 2086357770
