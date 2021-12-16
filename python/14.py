# Day 14: Extended Polymerization

from typing import DefaultDict
from santas_little_helpers import *
from collections import Counter, defaultdict, deque

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
polymer_template, insertion_rules = get_input('inputs/14.txt', False, '\n\n')
insertion_rules = [rule.split(' -> ') for rule in insertion_rules.split('\n')]
pair_generation = {pair: (pair[0]+letter, letter+pair[1]) for pair, letter in insertion_rules}


count_pairs = DefaultDict(int)
# initialize counter:
for pair in zip(polymer_template, polymer_template[1:]):
    pairstr = ''.join(c for c in pair)
    count_pairs[pair_generation[pairstr]] += 1
print(count_pairs)
steps = 39
for step in range(steps):
    update_dict = DefaultDict(int)
    for produced_pair, count in count_pairs.items():
        for pairstr in produced_pair:
            subpair = pair_generation[pairstr]
            update_dict[subpair] += count
    count_pairs = defaultdict(int)
    for pair, count in update_dict.items():
        count_pairs[pair] += count


count_letters = DefaultDict(int)
for pair, count in count_pairs.items():
    for letter in pair[0]:
        count_letters[letter] += count

sort_most = sorted(count_letters.items(), key=lambda x:x[1], reverse=True)
print(sort_most[0], sort_most[-1], polymer_template[-1])
party_2 = sort_most[0][1] + 1 - sort_most[-1][1]

print(party_2)