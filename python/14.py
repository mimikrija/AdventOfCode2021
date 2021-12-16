# Day 14: Extended Polymerization

from santas_little_helpers import *
from collections import defaultdict, Counter


## part_2 approach
polymer_template, insertion_rules = get_input('inputs/14.txt', False, '\n\n')
insertion_rules = [rule.split(' -> ') for rule in insertion_rules.split('\n')]
pair_generation = {pair: (pair[0]+letter, letter+pair[1]) for pair, letter in insertion_rules}


def pairs_after_steps(polymer_template, pair_generation, steps):
    polymer_pairs = [''.join(c for c in pair) for pair in zip(polymer_template, polymer_template[1:])]
    #initialize counter: run 1st step
    count_pairs = {pair_generation[pair]: polymer_pairs.count(pair) for pair in polymer_pairs}
    
    # remaining steps
    for _ in range(steps-1):
        update_dict = defaultdict(int)
        for produced_pair, count in count_pairs.items():
            subpairs = [pair_generation[pairstr] for pairstr in produced_pair]
            
            for subpair in subpairs:
                update_dict[subpair] += count
        count_pairs = update_dict.copy()
    return count_pairs

count_pairs = pairs_after_steps(polymer_template, pair_generation, 40)

count_letters = defaultdict(int)
for pair, count in count_pairs.items():
    for letter in pair[0]:
        count_letters[letter] += count

sort_most = sorted(count_letters.items(), key=lambda x:x[1], reverse=True)

party_2 = sort_most[0][1] + 1 - sort_most[-1][1]

print(party_2)
