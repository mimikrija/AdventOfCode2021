from santas_little_helpers import *
from collections import defaultdict

fish = get_input('inputs/06.txt', True, ',')

timer_update = lambda t: t-1 if t>0 else 6

def fish_count(days, in_fish):
    fish_status = {num: fish.count(num) for num in in_fish}
    fish_status[0] = 0
    for _ in range(days):
        fish_status_new = defaultdict(int)
        fish_status_new[8] = fish_status[0]
        for num in fish_status:
            fish_status_new[timer_update(num)] += fish_status[num]
        fish_status = fish_status_new
    return sum(c for c in fish_status.values())

party_1, party_2 = (fish_count(days, fish) for days in (80, 256))
print_solutions(party_1, party_2)
