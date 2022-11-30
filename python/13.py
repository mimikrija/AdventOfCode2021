# Day 13: Transparent Origami

from santas_little_helpers.helpers import *


def fold(coordinates, axis, axis_position):
    axis_position = int(axis_position)
    folded = set(coordinates)
    sym = axis == 'y'
    same = not sym
    for coordinate in coordinates:
        if coordinate[sym] > axis_position:
            new = 2 * axis_position - coordinate[sym]
            old = coordinate[same]
            fold_point = tuple(coord for pos, coord in sorted(zip([sym, same], [new, old])))
            folded.add(fold_point)
    return {coordinate for coordinate in folded if coordinate[sym] < axis_position}

def solve(coordinates, instructions):
    # follow the folding instructions
    for step, instruction in enumerate(instructions, start=1):
        coordinates = fold(coordinates, *instruction)
        if step == 1:
            party_1 = len(coordinates)
    print_solutions(party_1)
    print_from_set(coordinates)
    return(party_1)


coordinates, instructions = get_input('inputs/13.txt', False, '\n\n')
coordinates = {tuple(int(line.split(',')[n]) for n in (0, 1)) for line in coordinates.split('\n')}
instructions = [line.split()[2].split('=') for line in instructions.split('\n')]

party_1 = solve(coordinates, instructions)

party_2 = 'EPZGKCHU'


def test_one():
    assert party_1 == 837
def test_two():
    assert party_2 == 'EPZGKCHU'
