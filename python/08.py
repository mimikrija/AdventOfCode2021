
from santas_little_helpers import *
data = get_input('inputs/08.txt')
#data = get_input('inputs/08-ex.txt')
easy_data = [line.split('|')[1] for line in data]
counter = 0
for line in easy_data:
    for digit in line.split():
        if len(digit) == 2:
            counter += 1
        if len(digit) == 4:
            counter += 1
        if len(digit) == 3:
            counter += 1
        if len(digit) == 7:
            counter += 1

party_1 = counter
print_solutions(party_1)