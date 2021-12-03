
from santas_little_helpers import *
from collections import Counter

consumption = lambda x, y: int(x, 2) * int(y, 2)

data = get_input('inputs/03.txt')
size = len(data[0])


gamma = ''.join(Counter(column).most_common()[0][0] for column in zip(*data))
# epsilon is just an inverse of gamma
epsilon = gamma.translate(str.maketrans('01', '10'))

party_1 = consumption(gamma, epsilon)


# party 2


scrubber = list(data)
oxygen = list(data)
for column in range(size):
    stupac = ''.join(c[column] for c in scrubber)
    if len(scrubber) > 1:
        most = Counter(stupac).most_common()[0][0]
        least = Counter(stupac).most_common()[-1][0]
        if stupac.count('1') == stupac.count('0'):
            most = '1'

        temp = list(scrubber)
        scrubber = [number for number in temp if number[column] == most]



for column in range(size):
    stupac = ''.join(c[column] for c in oxygen)
    if len(oxygen) > 1:
        least = Counter(stupac).most_common()[-1][0]
        if stupac.count('1') == stupac.count('0'):
            least = '0'
        temp = list(oxygen)
        oxygen = [number for number in temp if number[column] == least]

scrubber = int(scrubber[0],2)
oxygen = int(oxygen[0], 2)
print(scrubber, oxygen)

party_2 = consumption(scrubber, oxygen)

print_solutions(party_1, party_2)