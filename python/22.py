from email.policy import default
from santas_little_helpers.helpers import *
from re import findall
from operator import mul, neg
from functools import reduce
from collections import defaultdict, deque, Counter

class Cuboid():
    def __init__(self, borders_x, borders_y, borders_z, on=True):
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
        return all(self_right < other_left or self_left > other_right for
            (self_left, self_right), (other_left, other_right) in zip(self_borders, other_borders))

    def all_in(self, other):
        ''' checks if self is completely within other '''
        self_borders = [self.borders[axis] for axis in ('x', 'y', 'z')]
        other_borders = [other.borders[axis] for axis in ('x', 'y', 'z')]
        return all(other_left < self_left < self_right < other_right for
            (self_left, self_right), (other_left, other_right) in zip(self_borders, other_borders))

    def volume(self):
        return reduce(mul, ((max + 1 - min) for (min, max) in self.borders.values()))

    def __ge__(self, other):
        return self.volume() >= other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()


def get_intersection(first, second):
    if first == second:
        intersection = first.copy()
        intersection.switch = False
    elif first.all_in(second):
        intersection = first.copy()
        intersection.switch = False
    elif second.all_in(first):
        intersection = second.copy()
        intersection.switch = False
    else:
        # actual intersection
        intersection = Cuboid((0, 0), (0, 0), (0,0), False)
        for axis in('x', 'y', 'z'):
            intersection.borders[axis] = (max(first.borders[axis][0], second.borders[axis][0]), min(first.borders[axis][1], second.borders[axis][1]))

    return intersection


def intersect_existing_intersections(negatives, new_intersection):

    if not any(intersection.no_overlap(new_intersection) for intersection in negatives):
        return []

    # at least one intersection intersects with the new one, no need to put it in the list, just the intersections
    # between the existing and the new, and they should be positive (otherwise I'd need to calculate the union)
    output_pos = []
    for intersection in negatives:
        if not intersection.no_overlap(new_intersection):
            new_positive = get_intersection(intersection, new_intersection)
            new_positive.switch = True
            output_pos.append(new_positive)
    
    
    return output_pos


cuboids = []
for line in get_input('inputs/22-e.txt'):
    min_x, max_x, min_y, max_y, min_z, max_z = map(int, findall(r'-?\d+', line))
    is_on = line[:2] == 'on'
    cuboids.append(Cuboid((min_x, max_x), (min_y, max_y), (min_z, max_z), is_on))

to_check_new = [cuboids[0]]
remaining = deque(cuboids[1:])

volumes = list(to_check_new)


while remaining:
    attacker = remaining.popleft()
    to_check = list(to_check_new)
    for cuboid in to_check:
        if not cuboid.no_overlap(attacker):
            intersection = get_intersection(cuboid, attacker)
            volumes.append(intersection)
            negatives = [volume for volume in volumes if not volume.switch]
            
            volumes += intersect_existing_intersections(negatives, intersection)
    if attacker.switch:
        volumes.append(attacker)
        to_check_new.append(attacker)



sign = lambda x: 1 if x else -1
total_on = sum(sign(cub.switch)*cub.volume() for cub in volumes)


print_solutions(total_on)
