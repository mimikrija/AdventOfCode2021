from santas_little_helpers.helpers import *


def get_block(x, y):
    "return 9 pixels around of `x, y`, inclusive, in an infinite grid"
    return ((x+dx, y+dy) for dy in range(-1, 2) for dx in range(-1, 2))

def get_enhancement_number(pixel, current_image, count=1):
    if count % 2 == 1:
        outside_pixel = '.'
    else:
        outside_pixel = '#'
    number = ''.join(current_image.get(coordinate, outside_pixel) for coordinate in get_block(*pixel)).translate(str.maketrans('#.', '10'))
    return int(number, 2)

def refresh_grid(in_grid, enhancement, count=1):
    out_grid = dict()
    xx = [x for x, y in in_grid.keys()]
    yy = [y for x, y in in_grid.keys()]
    x_range = range(min(xx)-1, max(xx)+2)
    y_range = range(min(yy)-1, max(yy)+2)
    for x in x_range:
        for y in y_range:
            pos = get_enhancement_number((x, y), in_grid, count)
            out_grid[(x, y)] = enhancement[pos]
    return out_grid

def lights_on(in_grid, iterations):
    for n in range(1, iterations+1):
        in_grid = refresh_grid(in_grid, enhancement_algorithm, n)
    return sum(c == '#' for c in in_grid.values())


data = get_input('inputs/20.txt')

enhancement_algorithm = data[0]
lights = {(column, row): char for row, line in enumerate(data[2:]) for column, char in enumerate(line)}


party_1 = lights_on(lights, 2)
party_2 = lights_on(lights, 50)

print_solutions(party_1, party_2)
