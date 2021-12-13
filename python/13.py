
from santas_little_helpers import *

coordinates, instructions = get_input('inputs/13.txt', False, '\n\n')
coordinates = {tuple(int(line.split(',')[n]) for n in (0, 1)) for line in coordinates.split('\n')}
instructions = [line.split()[2].split('=') for line in instructions.split('\n')]

def fold(coordinates, axis, number):
    number = int(number)
    folded = set(coordinates)
    if axis == 'y':
        for x, y in coordinates:
            if y > number:
                y = number - (y - number)
                folded.add((x, y))
        # remove folding line
        folded = {coordinate for coordinate in folded if coordinate[1] < number}
    if axis == 'x':
        for x, y in coordinates:
            if x > number:
                x = number - (x - number)
                folded.add((x, y))
        # remove folding line
        folded = {coordinate for coordinate in folded if coordinate[0] < number}
    return folded


for step, instruction in enumerate(instructions, start=1):
    coordinates = fold(coordinates, *instruction)
    if step == 1:
        party_1 = len(coordinates)

width = heigth = 0
for x,y in coordinates:
    if x > width:
        width = x
    if y > heigth:
        heigth = y

width += 1
heigth +=1


def print_from_set(in_set):
    hull = [width * [' '] for _ in range(heigth)]
    for x,y in in_set:
        hull[y][x] = '#'
    for line in hull:
        print(''.join(c for c in line))



print_solutions(party_1)

print_from_set(coordinates)
