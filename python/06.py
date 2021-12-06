from santas_little_helpers import *

fish = get_input('inputs/06.txt', True, ',')

days = 80

timer_update = lambda t: t-1 if t>0 else 6

for _ in range(days):
    new_fish = [8] * fish.count(0)
    fish = [timer_update(timer) for timer in fish]
    fish += new_fish


party_1 = len(fish)
print_solutions(party_1)
