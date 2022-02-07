# Day 6: Lanternfish

from santas_little_helpers import *
from santas_little_helpers.helpers import *

fish_data = get_input('inputs/06.txt', True, ',')

timer_update = lambda t: t-1 if t > 0 else 6

def fish_count(days, in_fish):
    fish_status = [in_fish.count(num) for num in range(9)]
    for _ in range(days):
        update = [0 for _ in range(9)]
        update[8] = fish_status[0]
        for status in range(9):
            update[timer_update(status)] += fish_status[status]
        fish_status = list(update)
    return sum(fish_status)

party_1, party_2 = (fish_count(days, fish_data) for days in (80, 256))
print_solutions(party_1, party_2)
