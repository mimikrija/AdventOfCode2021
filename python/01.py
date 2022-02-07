# Day 1: Sonar Sweep

from santas_little_helpers.helpers import *

sea_depths = get_input('inputs/01.txt', True)

party_1 = sum(second > first for first, second in zip(sea_depths, sea_depths[1:]))
party_2 = sum(sum(sea_depths[n+1:n+4]) > sum(sea_depths[n:n+3]) for n, depth in enumerate(sea_depths[:-3]))

print_solutions(party_1, party_2)
