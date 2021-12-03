
from santas_little_helpers import *
from collections import Counter

consumption = lambda gamma, epsilon: gamma * epsilon

data = get_input('inputs/03.txt')

size = len(data[0])


gamma = ''
epsilon = ''
for stupac in zip(*data):
    gamma += Counter(stupac).most_common()[0][0]
    epsilon += Counter(stupac).most_common()[-1][0] 

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
party_1 = consumption(gamma, epsilon)



oxygen = list(data)
scrubber = list(data)
# party 2


scrubber = list(data)
for column in range(size):
    stupac = ''.join(c[column] for c in scrubber)
    if len(scrubber) > 1:
        most = Counter(stupac).most_common()[0][0]
        least = Counter(stupac).most_common()[-1][0]
        if stupac.count('1') == stupac.count('0'):
            most = '1'

        temp = list(scrubber)
        scrubber = [number for number in temp if number[column] == most]



oxygen = list(data)
for column in range(size):
    stupac = ''.join(c[column] for c in oxygen)
    if len(oxygen) > 1:
        least = Counter(stupac).most_common()[-1][0]
        if stupac.count('1') == stupac.count('0'):
            least = '0'
        temp = list(oxygen)
        oxygen = [number for number in temp if number[column] == least]
print(oxygen, scrubber)
scrubber = int(scrubber[0],2)
oxygen = int(oxygen[0], 2)
print(scrubber, oxygen)

party_2 = consumption(scrubber, oxygen)

print_solutions(party_1, party_2)