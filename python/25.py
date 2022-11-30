# Day 25: Sea Cucumber

from santas_little_helpers.helpers import *

east_herd = set()
south_herd = set()
for row, line in enumerate(get_input('inputs/25.txt')):
    for column, char in enumerate(line):
        if char == '>':
            east_herd.add((column, row))
        if char == 'v':
            south_herd.add((column, row))

max_x = 138
max_y = 136

def get_right(current, east_herd, south_herd):
    x, y = current
    if x == max_x:
        new_pos = (0, y)
    else:
        new_pos = (x + 1, y)
    
    if new_pos not in east_herd and new_pos not in south_herd:
        return new_pos


def get_down(current, east_herd, south_herd):
    x, y = current
    if y == max_y:
        new_pos = (x, 0)
    else:
        new_pos = (x, y + 1)
    
    if new_pos not in east_herd and new_pos not in south_herd:
        return new_pos

def move_cucumbers(east, south):
    new_east = set()
    for position in east:
        if (new_position := get_right(position, east, south)):
            new_east.add(new_position)
        else:
            new_east.add(position)
    
    new_south = set()
    for position in south:
        if (new_position := get_down(position, new_east, south)):
            new_south.add(new_position)
        else:
            new_south.add(position)
    
    return new_east, new_south

old_east = set(east_herd)
old_south = set(south_herd)
count = 1
while True:
    new_east, new_south = move_cucumbers(old_east, old_south)
    if old_east == new_east and old_south == new_south:
        print(f'found after {count} steps')
        break
    old_east = set(new_east)
    old_south = set(new_south)
    count += 1
