
def get_input(file_name, numbers=False, separator='\n'):
    """ Reads in data present in `file_name` separated by `separator` string. """
    with open(file_name) as input_file:
        input_data = input_file.read().split(separator)
    if numbers:
        try:
            return list(map(int, input_data))
        except:
            raise ValueError('Unable to convert data into integers')
    else:
        return input_data

def print_solutions(part_1, part_2 = None):
    print(f'Part 1 solution is: {part_1}')
    if part_2:
        print(f'Part 2 solution is: {part_2}')

def add_wrap(num_1, num_2, limit, start=0):
    " Returns sum of `num_1` and `num_2` wrapped around to `start` they go over `limit`"
    return start + (num_1 + num_2)%(limit+1)

import itertools

DELTAS_eight = {dimension: set(itertools.product({-1, 0, 1}, repeat=dimension))
            - {tuple(0 for _ in range(dimension))} for dimension in {2, 3}}

DELTAS_four = {(-1, 0), (1, 0), (0, 1), (0, -1)}

def add_coordinates(tuple_1, tuple_2):
    return tuple(t_1 + t_2 for t_1, t_2 in zip(tuple_1, tuple_2))

def is_in(tuple_1, tuple_2):
    return all(0 <= t_1 < t_2 for t_1, t_2 in zip(tuple_1, tuple_2))

def get_four_neighbors(coordinate, GRID_SIZE=None):
    neighbors_infinite = {add_coordinates(coordinate, delta) for delta in DELTAS_four}
    if GRID_SIZE:
        return {coordinate for coordinate in neighbors_infinite if is_in(coordinate, (GRID_SIZE, GRID_SIZE))}
    return neighbors_infinite

def get_eight_neighbors(x, y, GRID_SIZE):
    "return 8 neighbors of `x, y` in a fixed-size square grid of size `GRID_SIZE`"
    return {(xn, yn) for xn, yn in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1))
                    if 0 <= xn < GRID_SIZE and 0 <= yn < GRID_SIZE} - {(x, y)}

def print_from_set(in_set):
    print()
    width, heigth = (max(in_set, key=lambda coord:coord[pos])[pos] + 1 for pos in (0, 1))
    plot_area = [width * [' '] for _ in range(heigth)]
    for x,y in in_set:
        plot_area[y][x] = '#'
    for row in plot_area:
        print(''.join(c for c in row))
