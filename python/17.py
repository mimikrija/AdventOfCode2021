# Day 17: Trick Shot

from santas_little_helpers.helpers import *
from santas_little_helpers.helpers import *
from re import findall
from itertools import product

data = get_input('inputs/17.txt')[0]
MIN_X, MAX_X, MIN_Y, MAX_Y = map(int, findall(r'-?\d+', data))


def update(x_pos, x_vel, y_pos, y_vel):
    x_pos += x_vel
    x_vel -= x_vel > 0 - x_vel < 0
    y_pos += y_vel
    y_vel -= 1
    return x_pos, x_vel, y_pos, y_vel

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

def valid_velocities():
    velocities = list()
    for x_vel_init, y_vel_init in product(range(1, MAX_X + 1), range(MIN_Y, -MIN_Y+1)):
        x = 0
        y = 0
        x_vel = x_vel_init
        y_vel = y_vel_init

        while keep_going(x, x_vel, y):
            x, x_vel, y, y_vel = update(x, x_vel, y, y_vel)
            if in_target(x, y):
                velocities.append((x_vel_init, y_vel_init))
                break
    return velocities

def peak(vel):
    if vel > 0:
        return vel**2 - sum(range(vel))
    return 0

def highest_point_of_all(initial_velocities):
    return peak(max(initial_velocities, key=lambda x:x[1])[1])


initial_velocities = valid_velocities()

party_1 = highest_point_of_all(initial_velocities)
party_2 = len(initial_velocities)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 5995
def test_two():
    assert party_2 == 3202
