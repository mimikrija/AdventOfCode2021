# Day 9: Smoke Basin

from santas_little_helpers import *
from collections import deque
from operator import mul
from functools import reduce

DELTAS ={
    -1+0j, # left
     1+0j, # right
     0+1j, # down
     0-1j, # up
}

def get_neighbors(location, cave_floor):
    return {candidate for candidate in (location + delta for delta in DELTAS) if candidate in cave_floor}

def traverse_floor(cave_floor, cave_heights, start=0+0j, part_2=False):
    lowpoints = set()
    frontier = deque([start])
    reached = set({start})

    while frontier:
        current = frontier.pop()
        current_height = cave_heights[current]
        neighbors = get_neighbors(current, cave_floor)
        # part 1: find single lowest points
        if all(cave_heights[neighbor] > current_height for neighbor in neighbors) and not part_2:
            lowpoints.add(current)
        for neighbor in neighbors:
            if neighbor not in reached:
                if not part_2:
                    frontier.append(neighbor)
                    reached.add(neighbor)
                # part 2: find basins
                elif cave_heights[neighbor] > current_height and cave_heights[neighbor] != 9:
                        frontier.append(neighbor)
                        reached.add(neighbor)
    if part_2:
        return reached
    return lowpoints

def part_1(lowpoints):
    return sum(cave_heights[low_point]+1 for low_point in lowpoints)

def part_2(lowpoints, cave_floor, cave_heights):
    basins = (len(traverse_floor(cave_floor, cave_heights, low_point, True)) for low_point in lowpoints)
    return reduce(mul, sorted(basins, reverse=True)[:3])

lines = get_input('inputs/09.txt')

cave_floor = []
cave_heights = dict()
for row, line in enumerate(lines):
    for col, height in enumerate(line):
        position = complex(row, col)
        cave_floor.append(position)
        cave_heights[position] = int(height)

lowpoints = traverse_floor(cave_floor, cave_heights)
print_solutions(part_1(lowpoints), part_2(lowpoints, cave_floor, cave_heights))
