from typing import Deque
from santas_little_helpers import *
from collections import deque

lines = get_input('inputs/09.txt')

cave_floor = []
cave_heights = dict()
for row, line in enumerate(lines):
    for col, height in enumerate(line):
        position = complex(row, col)
        cave_floor.append(position)
        cave_heights[position] = int(height)

def get_neighbors(current, cave_floor):
    neighbors = list()
    location = current
    for dx in {-1, 1}:
        candidate = location + complex(dx, 0)
        if candidate in cave_floor:
            neighbors.append(candidate)
    for dy in {-1, 1}:
        candidate = location + complex(0, dy)
        if candidate in cave_floor:
            neighbors.append(candidate)
    return neighbors



def traverse_floor(cave_floor, start=0+0j):
    lowpoints = list()
    frontier = deque()
    frontier.append(start)
    reached = set()
    reached.add(start)

    while frontier:
        current = frontier.pop()
        current_height = cave_heights[current]
        neighbors = get_neighbors(current, cave_floor)
        if all(cave_heights[neighbor] > current_height for neighbor in neighbors):
            lowpoints.append(current_height+1)
        for neighbor in neighbors:
            if neighbor not in reached:
                frontier.append(neighbor)
                reached.add(neighbor)
    return sum(lowpoints)

party_1 = traverse_floor(cave_floor)
print_solutions(party_1)