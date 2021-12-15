# Day 14: Extended Polymerization

from santas_little_helpers import *
from collections import Counter, deque

def step(polymer, rules):
    polymer = deque(polymer)
    new_polymer = []
    while len(polymer) > 1:
        left = polymer.popleft()
        right = polymer[0]
        pair = left+right
        insertion = rules[pair]
        new_polymer.append(left)
        new_polymer.append(insertion)
    new_polymer.append(polymer.pop())
    return new_polymer

polymer_template, insertion_rules = get_input('inputs/ex.txt', False, '\n\n')
insertion_rules = [rule.split(' -> ') for rule in insertion_rules.split('\n')]
insertion_rules = {pair: letter for pair, letter in insertion_rules}

polymer = polymer_template
for _ in range(10):
    polymer = step(polymer, insertion_rules)

most = Counter(polymer).most_common()
party_1 = most[0][1] - most[-1][1]
print_solutions(party_1)

## part_2 approach
polymer_template, insertion_rules = get_input('inputs/ex.txt', False, '\n\n')
insertion_rules = [rule.split(' -> ') for rule in insertion_rules.split('\n')]
pair_generation = {pair: [pair[0]+letter, letter+pair[1]] for pair, letter in insertion_rules}
count_pairs = {''.join(c for c in pair): 1 for pair in zip(polymer_template, polymer_template[1:])}
print(count_pairs)