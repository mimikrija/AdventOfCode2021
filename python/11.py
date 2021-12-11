# Day 11: Dumbo Octopus

from santas_little_helpers import *


def increase_energy(octopi):
    # First, the energy level of each octopus increases by 1.
    for y, row in enumerate(octopi):
        for x, e in enumerate(row):
            octopi[y][x] += 1

def get_adjacents(current_octopus):
    adjacents = set()
    x, y = current_octopus
    for delta_x in (-1, 0, 1):
        for delta_y in (-1, 0, 1):
            xn = x + delta_x
            yn = y + delta_y
            if 0 <= xn < LIMIT and 0 <= yn < LIMIT and not(xn == x and yn == y):
                adjacents.add((xn, yn))
    return adjacents


def run_step(energy_levels):
    flashed_total = set()
    # Then, any octopus with an energy level greater than 9 flashes.
    while True:
        #print(energy_levels)
        flashed = {(x, y) for y, row in enumerate(energy_levels) for x, E in enumerate(row) if E > 9 and (x, y) not in flashed_total}
        #print(flashed)
        for octopus in flashed:
            for x, y in get_adjacents(octopus):
                if (x, y) not in flashed:
                    energy_levels[y][x] += 1
        #print(energy_levels)
        flashed_total |= flashed
        # for x, y in flashed:
        #     energy_levels[y][x] = 0
        if not flashed:
            break
    for x, y in flashed_total:
        energy_levels[y][x] = 0
    return energy_levels, len(flashed_total)
                
    print(flashed)
    quit()
    rest = octopi - flashed
    # This increases the energy level of all adjacent octopuses by 1 including octopuses that are diagonally adjacent.
    adjacents = {adjacent for octopus in flashed for adjacent in get_adjacents(octopi, octopus)}
    increased_adjacent = increase_energy(adjacents)
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    # (An octopus can only flash at most once per step.)

energy_levels = [[int(num) for num in row] for row in get_input('inputs/example.txt')]
LIMIT = len(energy_levels)

party_1 = 0
for steps in range(1,1000):
    increase_energy(energy_levels)
    energy_levels, flashes = run_step(energy_levels)
    party_1 += flashes
    if all(e==0 for row in energy_levels for e in row):
        party_2 = steps
        break

print_solutions(party_1, party_2)

