# Day 17: Trick Shot

from santas_little_helpers import *
from re import findall
from itertools import product

data = get_input('inputs/17.txt')[0]
MIN_X, MAX_X, MIN_Y, MAX_Y = map(int, findall(r'-?\d+', data))


def update_x(x_pos, x_vel):
    x_pos += x_vel
    x_vel -= x_vel > 0 - x_vel < 0
    return x_pos, x_vel

def update_y(y_pos, y_vel, max_y):
    y_pos += y_vel
    y_vel -= 1
    if y_pos > max_y:
        max_y = y_pos
    return y_pos, y_vel, max_y

def keep_going(x_pos, x_vel, y_pos):
    if x_pos < MIN_X and x_vel == 0:
        return False
    if x_pos > MAX_X:
        return False
    if y_pos < MIN_Y:
        return False
    return True

def in_target(x_pos, y_pos):
    return MIN_X <= x_pos <= MAX_X and MIN_Y <= y_pos <= MAX_Y

def solution_max_y(x_vel, y_vel):
    x = 0
    y = 0
    max_y = 0
    step = 0

    while keep_going(x, x_vel, y):
        step += 1
        x, x_vel = update_x(x, x_vel)
        y, y_vel, max_y = update_y(y, y_vel, max_y)
        if in_target(x, y):
            return max_y
    return -1


highs = [solution_max_y(x_vel, y_vel) for x_vel, y_vel in product(range(0, MAX_X + 1), range(MIN_Y, -MIN_Y+1))]
party_1 = max(highs)
party_2 = sum(c >= 0 for c in highs)

print_solutions(party_1, party_2)
