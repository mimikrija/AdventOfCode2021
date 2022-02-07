# Day 14: Extended Polymerization

from santas_little_helpers import *
from santas_little_helpers.helpers import *
from collections import defaultdict


polymer_template, insertion_rules = get_input('inputs/14.txt', False, '\n\n')
insertion_rules = [rule.split(' -> ') for rule in insertion_rules.split('\n')]
pair_generation = {pair: (pair[0]+letter, letter+pair[1]) for pair, letter in insertion_rules}


def pairs_after_steps(polymer_template, pair_generation, steps):
    polymer_pairs = [''.join(c for c in pair) for pair in zip(polymer_template, polymer_template[1:])]
    #initialize counter: run 1st step
    count_pairs = {pair_generation[pair]: polymer_pairs.count(pair) for pair in polymer_pairs}

    # remaining steps
    for _ in range(steps-1):
        count_update = defaultdict(int)
        for produced_pair, count in count_pairs.items():
            subpairs = (pair_generation[pairstr] for pairstr in produced_pair)
            for subpair in subpairs:
                count_update[subpair] += count
        count_pairs = count_update
    return count_pairs

def count_elements(count_pairs, polymer_template):
    count_letters = defaultdict(int)
    for pair, count in count_pairs.items():
        for letter in pair[0]:
            count_letters[letter] += count
    sort_most = sorted(count_letters.items(), key=lambda x:x[1], reverse=True)
    most_common_element = sort_most[0][0]
    least_common_element = sort_most[-1][0]
    return sort_most[0][1] + (most_common_element == polymer_template[-1]) - sort_most[-1][1] - (least_common_element == polymer_template[-1])


count_pairs_parts = (pairs_after_steps(polymer_template, pair_generation, steps) for steps in (10, 40))

party_1, party_2 = (count_elements(count_pairs, polymer_template) for count_pairs in count_pairs_parts)
print_solutions(party_1, party_2)

