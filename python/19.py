from santas_little_helpers.helpers import *
from itertools import product, permutations
from collections import Counter

ROLL = [(1, 0, 0), (0, 0, -1), (0, 1, 0)]
PITCH = [(0, 0, 1), (0, 1, 0), (-1, 0, 0)]
YAW = [(0, -1, 0), (1, 0, 0), (0, 0, 1)]

def diff(first, second):
    return (first[0] - second[0], first[1] - second[1], first[2] - second[2])

def overlap(first, second):
    """"Returns most common distance from `second` to `first` coordinates"""
    return Counter((diff(two, one) for one, two in product(first, second))).most_common(1)[0]

def dotproduct(matrix, vector):
    return(tuple(sum(r*c for r, c, in zip(row, vector)) for row in matrix))



def rotate_coordinates(in_coord):
    coord = in_coord

    # keep rolling
    rolls = []
    for _ in range(4):
        coord = dotproduct(ROLL, coord)
        rolls.append(coord)

    # keep pitching
    rollpitchs = []
    for coord in rolls:
        for _ in range(4):
            coord = dotproduct(PITCH, coord)
            rollpitchs.append(coord)

    # keep yawing
    rollpitchyaws = []
    for coord in rollpitchs:
        for _ in range(4):
            coord = dotproduct(YAW, coord)
            rollpitchyaws.append(coord)

    return set(rollpitchyaws)


scanners = dict()
for scanner in get_input('inputs/19.txt', False, '\n\n'):
    scanner_data = scanner.split('\n')
    name = scanner_data[0]
    coords = set(eval('(' + line + ')') for line in scanner_data[1:])
    scanners[name] = coords

