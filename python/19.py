from santas_little_helpers.helpers import *
from itertools import product
from collections import Counter

def diff(first, second):
    return (first[0] - second[0], first[1] - second[1], first[2] - second[2])

def overlap(first, second):
    """"Returns most common distance from `second` to `first` coordinates"""
    return Counter((diff(two, one) for one, two in product(first, second))).most_common(1)[0]


scanners = dict()
for scanner in get_input('inputs/19.txt', False, '\n\n'):
    scanner_data = scanner.split('\n')
    name = scanner_data[0]
    coords = set(eval('(' + line + ')') for line in scanner_data[1:])
    scanners[name] = coords

