from santas_little_helpers import *

crab_data = get_input('inputs/07.txt', True,',')


relatives = []

for position in set(crab_data):
    relatives +=  [sum(abs(position-num) for num in crab_data)]


print(min(relatives))