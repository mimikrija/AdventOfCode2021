from audioop import minmax
from santas_little_helpers.helpers import *

# def convert_9_pixels_to_number(pixels):
#     for pixel in pixels
def get_block(x, y):
    "return 9 pixels around of `x, y`, inclusive, in an infinite grid"
    return {(xn, yn) for xn, yn in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1))}

def get_enhancement_number(pixel, current_image):
    block = get_block(*pixel)
    number = ''
    # treba rijesiti konzistentni sort!!
    for pixel in sorted(sorted(block, key=lambda coord:coord[0]), key=lambda coord:coord[1]):

        if pixel in current_image:
            number += '#'
        else:
            number += '.'
    number = ''.join('1' if c == '#' else '0' for c in number)
    return int(number, 2)

data = get_input('inputs/20-e.txt')

enhancement_algorithm = [c == '#' for c in data[0]]
print(len(enhancement_algorithm))


lights = {(column, row) for row, line in enumerate(data[2:]) for column, char in enumerate(line) if char == '#'}
#lights = {(x, y) for x in range(0, 3) for y in range(0, 3)}



print_from_set(lights)
print(' ')
min_x, max_x = -10, 10
min_y, max_y = -10, 10
new_lights = set()
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        if enhancement_algorithm[get_enhancement_number((x, y), lights)]:
            new_lights.add((x, y))



print_from_set(new_lights)
# print(sorted(new_lights))
# print(len(sorted(new_lights)))