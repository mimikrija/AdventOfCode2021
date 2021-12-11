# Day 11: Dumbo Octopus

from santas_little_helpers import *

def increase_energy(energy_levels):
    for y, row in enumerate(energy_levels):
        for x, e in enumerate(row):
            energy_levels[y][x] += 1

def run_step(energy_levels):
    # First, the energy level of each octopus increases by 1.
    increase_energy(energy_levels)

    flashed_total = set()
    while True:
    # Then, any octopus with an energy level greater than 9 flashes.
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
        flashed = {(x, y) for y, row in enumerate(energy_levels) for x, e in enumerate(row)
                            if e > 9 and (x, y) not in flashed_total}
    # This increases the energy level of all adjacent octopuses by 1 
    # including octopuses that are diagonally adjacent.
        for octopus in flashed:
            for x, y in get_eight_neighbors(*octopus, GRID_SIZE) - flashed:
                    energy_levels[y][x] += 1
        flashed_total |= flashed # (An octopus can only flash at most once per step.)

    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
        if not flashed:
            break

    # Finally, any octopus that flashed during this step has its energy level set to 0,
    # as it used all of its energy to flash
    for x, y in flashed_total:
        energy_levels[y][x] = 0

    return len(flashed_total)

def solve(energy_levels):
    count_flashes = 0
    for steps in range(1,1000):
        flashes = run_step(energy_levels)
        if steps <= 100:
            count_flashes += flashes
        if all(e == 0 for row in energy_levels for e in row):
            sync_day = steps
            break
    return count_flashes, sync_day


energy_levels = [[int(num) for num in row] for row in get_input('inputs/example.txt')]
GRID_SIZE = len(energy_levels)

print_solutions(*solve(energy_levels))
