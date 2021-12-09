from typing import Deque
from santas_little_helpers import *
from collections import deque
from operator import mul
from functools import reduce

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

def get_basin_neighbors(current, cave_floor):
    neighbors = list()
    location = current
    for dx in {-1, 1}:
        candidate = location + complex(dx, 0)
        if candidate in cave_floor and cave_heights[candidate] == cave_heights[location] + 1:
            neighbors.append(candidate)
    for dy in {-1, 1}:
        candidate = location + complex(0, dy)
        if candidate in cave_floor and cave_heights[candidate] == cave_heights[location] + 1:
            neighbors.append(candidate)
    return neighbors



def traverse_floor(cave_floor, start=0+0j, part_2=False):
    lowpoints = set()
    frontier = deque()
    frontier.append(start)
    reached = set()
    reached.add(start)
    basins = list()
    #lowpoints.append(start)

    while frontier:
        current = frontier.pop()
        current_height = cave_heights[current]
        neighbors = get_neighbors(current, cave_floor)
        if all(cave_heights[neighbor] > current_height for neighbor in neighbors) and not part_2:
            # lowpoint reached
            #lowpoints.append(current_height+1)
            lowpoints.add(current)
        for neighbor in neighbors:
            if neighbor not in reached:
                if part_2:
                    if cave_heights[neighbor] > cave_heights[current] and cave_heights[neighbor] != 9:
                        frontier.append(neighbor)
                        reached.add(neighbor)
                        lowpoints.add(neighbor)
                     #   lowpoints.add(current)
                else:
                    frontier.append(neighbor)
                    reached.add(neighbor)

    return lowpoints

def part_1(lowpoints):
    return sum(cave_heights[low_point]+1 for low_point in lowpoints)

def basins(lowpoints):
    basins = list()
    for low_point in lowpoints:
        basin = len(traverse_floor(cave_floor, low_point, True))+1
        basins.append(basin)
        #print(len(basins))
    return reduce(mul, sorted(basins, reverse=True)[:3])


lowpoints = traverse_floor(cave_floor)
party_1 = part_1(lowpoints)
party_2 = basins(lowpoints)
print_solutions(party_1, party_2)

# part 2 791200 too low