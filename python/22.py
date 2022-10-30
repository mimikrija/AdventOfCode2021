from santas_little_helpers.helpers import *
from re import findall
from operator import mul
from functools import reduce
from collections import deque

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


def get_intersection(first, second, status=False):
    if first == second:
        intersection = first.copy()
        intersection.switch = status
    elif first.all_in(second):
        intersection = first.copy()
        intersection.switch = status
    elif second.all_in(first):
        intersection = second.copy()
        intersection.switch = status
    else:
        # actual intersection
        intersection = Cuboid((0, 0), (0, 0), (0,0), status)
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

def purge_intersections(old_intersections, intersections):
    # self check current intersections against themselves
    # mark them as positive
    if len(intersections) == 1:
        new_intersections = list(intersections)
    else:
        checked = deque([intersections[0]])
        to_check = deque(intersections[1:])
        new_intersections = list(intersections)
        while to_check:
            attacker = to_check.popleft()
            for cubo in checked:
                new_intersections.append(get_intersection(attacker, cubo, True))
    
    # purge new intersections from same volumes with different switch
    # for new1 in new_intersections:
    #     for new2 in new_intersections[1:]:
    #         if new1 == new2 and new1.switch != new2.switch:
    #             new_intersections.remove(new1)
    #             new_intersections.remove(new2)

    # remove any which "cancel out" (same volume, different switch, no need to keep them in)
    for old in old_intersections:
        for new in new_intersections:
            if old == new and old.switch != new.switch:
                old_intersections.remove(old)
                new_intersections.remove(new)
    
    # finally, intersect old and new
    res = []
    for old in old_intersections:
        for new in new_intersections:
            if not old.no_overlap(new):
                if old.switch and new.switch:
                    status = False
                if old.switch != new.switch:
                    status = False
                if not old.switch and not new.switch:
                    status = True
                res.append(get_intersection(old, new, status))

    return old_intersections + new_intersections + res

    # cancel out positives with the negatives if applicable
    return purged_intersections



cuboids = []
for line in get_input('inputs/22-e.txt'):
    min_x, max_x, min_y, max_y, min_z, max_z = map(int, findall(r'-?\d+', line))
    is_on = line[:2] == 'on'
    cuboids.append(Cuboid((min_x, max_x), (min_y, max_y), (min_z, max_z), is_on))

to_check_new = [cuboids[0]]
remaining = deque(cuboids[1:])

volumes = list(to_check_new)
intersections = []
existing_intersections = []

while remaining:
    attacker = remaining.popleft()
    to_check = list(to_check_new)
    for cuboid in to_check:
        if not cuboid.no_overlap(attacker):
            intersection = get_intersection(cuboid, attacker)
            intersections.append(intersection)
            #volumes.append(intersection)
            #negatives = [volume for volume in volumes if not volume.switch]
            
            #volumes += intersect_existing_intersections(negatives, intersection)
            existing_intersections = purge_intersections(existing_intersections, intersections)
    if attacker.switch:
        volumes.append(attacker)
        to_check_new.append(attacker)

volumes += existing_intersections


sign = lambda x: 1 if x else -1
total_on = sum(sign(cub.switch)*cub.volume() for cub in volumes)


print_solutions(total_on)
