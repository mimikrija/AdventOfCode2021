from santas_little_helpers import *

crab_data = get_input('inputs/07.txt', True,',')
#crab_data = get_input('inputs/07-ex.txt', True,',')

fuell = lambda x: x *(1 + x)/2



relatives = []
minimal=float('inf')

for position in range(min(crab_data), max(crab_data)+1):

    relatives +=  [sum(abs(position-num) for num in crab_data)]
    new_fuel = sum(fuell(abs(position-num)) for num in crab_data)
    if new_fuel < minimal:
        minimal = new_fuel


print(min(relatives))
print(int(minimal))