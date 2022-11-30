from santas_little_helpers.helpers import *
from re import findall
from operator import mul
from functools import reduce
from time import time

class Cuboid():
    def __init__(self, borders_x=(0, 0), borders_y=(0, 0), borders_z=(0, 0), on=True):
        self.switch = on
        self.borders = {
            'x': borders_x,
            'y': borders_y,
            'z': borders_z,
        }
    def __eq__(self, other):
        if self.borders == other.borders:
            return True
        return False

    def copy(self):
        return Cuboid(*self.borders.values(), self.switch)

    def no_overlap(self, other):
        self_borders = [self.borders[axis] for axis in ('x', 'y', 'z')]
        other_borders = [other.borders[axis] for axis in ('x', 'y', 'z')]
        return any(self_right < other_left or self_left > other_right for
            (self_left, self_right), (other_left, other_right) in zip(self_borders, other_borders))

    def all_in(self, other):
        ''' checks if self is completely within other '''
        self_borders = [self.borders[axis] for axis in ('x', 'y', 'z')]
        other_borders = [other.borders[axis] for axis in ('x', 'y', 'z')]
        return all(other_left < self_left < self_right < other_right for
            (self_left, self_right), (other_left, other_right) in zip(self_borders, other_borders))

    def volume(self):
        sign = 1 if self.switch else -1
        return sign*reduce(mul, ((max + 1 - min) for (min, max) in self.borders.values()))


def get_intersection(first, second):
    
    if first.no_overlap(second):
        return None
    if first == second or first.all_in(second):
        intersection = first.copy()
    elif second.all_in(first):
        intersection = second.copy()
    else:
        # actual intersection
        intersection = Cuboid()
        for axis in('x', 'y', 'z'):
            intersection.borders[axis] = (max(first.borders[axis][0], second.borders[axis][0]), min(first.borders[axis][1], second.borders[axis][1]))
    intersection.switch = not first.switch
    return intersection


def switched_on(in_cuboids):
    intersections = []
    processed = []

    for attacker in in_cuboids:
        intersections = []

        for current in processed:
            intersection = get_intersection(current, attacker)
            if intersection:
                intersections.append(intersection)
        if attacker.switch:
            processed.append(attacker)
        processed += intersections
    
    return sum(cubo.volume() for cubo in processed)

# parse intput into list of cuboids
cuboids = []
for line in get_input('inputs/22.txt'):
    min_x, max_x, min_y, max_y, min_z, max_z = map(int, findall(r'-?\d+', line))
    is_on = line[:2] == 'on'
    cuboids.append(Cuboid((min_x, max_x), (min_y, max_y), (min_z, max_z), is_on))


party_1 = switched_on(cuboids[:20])
party_2 = switched_on(cuboids)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 596598
def test_two():
    assert party_2 == 1199121349148621
