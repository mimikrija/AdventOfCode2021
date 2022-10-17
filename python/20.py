
from santas_little_helpers.helpers import *
from math import sqrt

# def convert_9_pixels_to_number(pixels):

def get_block(x, y):
    "return 9 pixels around of `x, y`, inclusive, in an infinite grid"
    return sorted(sorted({(xn, yn) for xn, yn in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1))}, key=lambda coord:coord[0]), key=lambda coord:coord[1])

def get_enhancement_number(pixel, current_image, count=1):
    if count % 2 == 1:
        outside_pixel = '.'
    else:
        outside_pixel = '#'
    number = ''.join(current_image.get(coordinate, outside_pixel) for coordinate in get_block(*pixel)).translate(str.maketrans('#.', '10'))
    return int(number, 2)

def refresh_grid(in_grid, enhancement, count=1):
    dimension = int(sqrt(len(in_grid))) + 1
    out_grid = dict()
    for x in range(-count, dimension):
        for y in range(-count, dimension):
            pos = get_enhancement_number((x, y), in_grid, count)
            out_grid[(x, y)] = enhancement[pos]
    return out_grid


data = get_input('inputs/20.txt')

enhancement_algorithm = data[0]
lights = {(column, row): char for row, line in enumerate(data[2:]) for column, char in enumerate(line)}

for n in range(1, 51):
    lights = refresh_grid(lights, enhancement_algorithm, n)


party_1 = len([c for c in lights.values() if c == '#'])
print_solutions(party_1)
