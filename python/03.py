
from santas_little_helpers import *
from collections import Counter

consumption = lambda gamma, epsilon: gamma * epsilon

data = get_input('inputs/03.txt')

gamma = ''
epsilon = ''
for stupac in zip(*data):
    gamma += Counter(stupac).most_common()[0][0]
    epsilon += Counter(stupac).most_common()[-1][0] 

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
party_1 = consumption(gamma, epsilon)

print_solutions(party_1)
