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

def traverse_floor(cave_floor, start=0+0j, part_2=False):
    lowpoints = set()
    frontier = deque()
    frontier.append(start)
    reached = set()
    reached.add(start)

    while frontier:
        current = frontier.pop()
        current_height = cave_heights[current]
        neighbors = get_neighbors(current, cave_floor)
        if all(cave_heights[neighbor] > current_height for neighbor in neighbors) and not part_2:
            lowpoints.add(current)
        for neighbor in neighbors:
            if neighbor not in reached:
                if part_2:
                    if cave_heights[neighbor] > cave_heights[current] and cave_heights[neighbor] != 9:
                        frontier.append(neighbor)
                        reached.add(neighbor)
                        lowpoints.add(neighbor)
                else:
                    frontier.append(neighbor)
                    reached.add(neighbor)

    return lowpoints

def part_1(lowpoints):
    return sum(cave_heights[low_point]+1 for low_point in lowpoints)

def part_2(lowpoints):
    basins = (len(traverse_floor(cave_floor, low_point, True))+1 for low_point in lowpoints)
    return reduce(mul, sorted(basins, reverse=True)[:3])

lines = get_input('inputs/09.txt')

cave_floor = []
cave_heights = dict()
for row, line in enumerate(lines):
    for col, height in enumerate(line):
        position = complex(row, col)
        cave_floor.append(position)
        cave_heights[position] = int(height)

lowpoints = traverse_floor(cave_floor)
print_solutions(part_1(lowpoints), part_2(lowpoints))
