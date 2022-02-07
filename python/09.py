# Day 9: Smoke Basin

from santas_little_helpers import *
from santas_little_helpers.helpers import *
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

def find_lowpoints(cave_floor, cave_heights):
    return {location for location in cave_floor 
                        if all(cave_heights[neighbor] > cave_heights[location]
                        for neighbor in get_neighbors(location, cave_floor))}

def traverse_floor(cave_floor, cave_heights, start):
    frontier = deque([start])
    reached = set({start})
    while frontier:
        current = frontier.pop()
        current_height = cave_heights[current]
        neighbors = get_neighbors(current, cave_floor)
        for neighbor in neighbors:
            if neighbor not in reached and cave_heights[neighbor] > current_height and cave_heights[neighbor] != 9:
                frontier.append(neighbor)
                reached.add(neighbor)
    return reached

def part_2(lowpoints, cave_floor, cave_heights):
    basins = (len(traverse_floor(cave_floor, cave_heights, low_point)) for low_point in lowpoints)
    return reduce(mul, sorted(basins, reverse=True)[:3])

lines = get_input('inputs/09.txt')

cave_floor = []
cave_heights = dict()
for row, line in enumerate(lines):
    for col, height in enumerate(line):
        position = complex(row, col)
        cave_floor.append(position)
        cave_heights[position] = int(height)

lowpoints = find_lowpoints(cave_floor, cave_heights)

party_1 = sum(cave_heights[low_point]+1 for low_point in lowpoints)
party_2 = part_2(lowpoints, cave_floor, cave_heights)

print_solutions(party_1, party_2)
