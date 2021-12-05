# Day 5: Hydrothermal Venture

from santas_little_helpers import *
from collections import Counter

data = get_input('inputs/05.txt')

# if we need a range in descending order this helps
direction = lambda start, end: 1 if end > start else -1

is_hor_ver = lambda sx, ex, sy, ey: sx == ex or sy == ey
is_45 = lambda sx, ex, sy, ey: abs((sx - ex)/(sy - ey)) == 1

def line_from_endpoints(starts, ends, diagonals=False):
    sx, sy = starts
    ex, ey = ends
    dx = direction(sx, ex)
    dy = direction(sy, ey)

    if is_hor_ver(sx, ex, sy, ey):
        return {(x, y) for x in range(sx, ex+dx, dx) for y in range(sy, ey+dy, dy)}
    elif is_45(sx, ex, sy, ey) and diagonals:
        return {(x,  y) for x, y in zip(range(sx, ex+dx, dx), range(sy, ey+dy, dy))}
    else:
        return {}

def count_overlaps(end_points, diagonals=False):
    lines = [line_from_endpoints(starts, ends, diagonals) for starts, ends in end_points]
    all_points = [point for line in lines for point in line]
    points_count = Counter(all_points)
    return sum(freq >=2 for _, freq in points_count.most_common())

end_points = []
for line in data:
    start, end = line.split('->')
    starts = tuple(int(num) for num in start.split(','))
    ends = tuple(int(num) for num in end.split(','))
    end_points.append(tuple((starts, ends)))


party_1, party_2 = (count_overlaps(end_points, diagonals) for diagonals in (False, True))

print_solutions(party_1, party_2)
