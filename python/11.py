# Day 11: Dumbo Octopus

from santas_little_helpers import *


def increase_energy(octopi):
    # First, the energy level of each octopus increases by 1.
    return {(x, y, E+1) for x, y, E in octopi}

DELTAS = ()

def get_adjacents(octopi, current_octopus):
    adjacents = set()
    for octopus in octopi:
        if abs(octopus[0] - current_octopus[0]) <= 1 and abs(octopus[1] - current_octopus[1]) <= 1 and octopus != current_octopus:
            adjacents.add(octopus)
    return adjacents

def flash(octopi):
    # Then, any octopus with an energy level greater than 9 flashes.
    flashed = {(x, y, E) for x, y, E in octopi if E > 9}
    rest = octopi - flashed
    # This increases the energy level of all adjacent octopuses by 1 including octopuses that are diagonally adjacent.
    adjacents = {adjacent for octopus in flashed for adjacent in get_adjacents(octopi, octopus)}
    increased_adjacent = increase_energy(adjacents)
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    # (An octopus can only flash at most once per step.)

energy_levels = [[int(num) for num in row] for row in get_input('inputs/example.txt')]
octopi = {(x, y, E) for y, row in enumerate(energy_levels) for x, E in enumerate(row)}

octopi = increase_energy(octopi)


flash(octopi)

