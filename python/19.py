from santas_little_helpers.helpers import *
from itertools import product, permutations
from collections import Counter, defaultdict

ROLL = [(1, 0, 0), (0, 0, -1), (0, 1, 0)]
PITCH = [(0, 0, 1), (0, 1, 0), (-1, 0, 0)]
YAW = [(0, -1, 0), (1, 0, 0), (0, 0, 1)]

def diff(first, second):
    return (first[0] - second[0], first[1] - second[1], first[2] - second[2])

def most_common_distance(first, second):
    """"Returns most common distance from `second` to `first` coordinates"""
    return Counter((diff(two, one) for one, two in product(first, second))).most_common(1)[0]

def dotproduct(matrix, vector):
    return(tuple(sum(r*c for r, c, in zip(row, vector)) for row in matrix))

def generate_rotated_coordinates(in_coords):
    # in the worst case, this yields 4 + 16 + 64 times
    # which is not ideal, but I am hoping we'll not always need to yield so much
    # there will be duplicates, of course, but the idea is to just yield until
    # the first instance od 12 matches is found

    # first four rolls
    roll = list(in_coords)
    rolls = []
    for _ in range(4):
        roll = [dotproduct(ROLL, coord) for coord in roll]
        rolls.append(roll)
        yield roll

    # then additional four pitches for each of the rolls
    pitched_rolls = []
    for roll in rolls:
        pitched_roll = roll
        for _ in range(4):
            pitched_roll = [dotproduct(PITCH, coord) for coord in pitched_roll]
            pitched_rolls.append(pitched_roll)
            yield pitched_roll

    # finally the four yaws on top of pitched rolls
    yawed_pitched_rolls = []
    for pitched_roll in pitched_rolls:
        yawed_pitched_roll = pitched_roll
        for _ in range(4):
            yawed_pitched_roll = [dotproduct(YAW, coord) for coord in yawed_pitched_roll]
            yawed_pitched_rolls.append(yawed_pitched_roll)
            yield yawed_pitched_roll


def align_coordinates(fixed, rotating):
    gencoords = generate_rotated_coordinates(rotating)
    while True:
        dist, count = most_common_distance(fixed, rotating)
        if count >= 12:
            return dist, rotating
        else:
            try:
                rotating = next(gencoords)
            except StopIteration:
                return

def overlap(in_scanners):
    """"returns a dictionary {scanner_name: list of tupples (matched_scanner, distance, rotated_coordinates)"""
    results = defaultdict(list)
    for scanner1, scanner2 in permutations(scanners.keys(), r=2):
        if scanner1 != scanner2:
            alignment = align_coordinates(scanners[scanner1], scanners[scanner2])
            if alignment:
                distance, coordinates = alignment
                results[scanner1].append((scanner2, distance, coordinates))
    return results


scanners = dict()
for scanner in get_input('inputs/19-e.txt', False, '\n\n'):
    scanner_data = scanner.split('\n')
    name = scanner_data[0]
    coords = set(eval('(' + line + ')') for line in scanner_data[1:])
    scanners[name] = coords

