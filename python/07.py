# Day 7: The Treachery of Whales

from santas_little_helpers import *
from statistics import median, mean

fuel_linear = lambda candidate, positions: sum(abs(position-candidate) for position in positions)
sum_series = lambda x: x * (1 + x)/2 # this is sum of range(1,x+1)
fuel_incremental = lambda candidate, positions: sum(sum_series(abs(position-candidate)) for position in positions)


def find_fuel(crab_data):
     constant_pos, incremental_pos = (round(median(crab_data)), round(mean(crab_data)))
     party_1 = min(fuel_linear(candidate, crab_data) for candidate in range(constant_pos-1, constant_pos+2))
     party_2 = min(fuel_incremental(candidate, crab_data) for candidate in range(incremental_pos-1, incremental_pos+2))
     return int(party_1), int(party_2)


crab_data = get_input('inputs/07.txt', True,',')

print_solutions(*find_fuel(crab_data))
