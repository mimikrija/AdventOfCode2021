# Day 8: Seven Segment Search

from santas_little_helpers import *
from santas_little_helpers.helpers import *
from collections import defaultdict, deque

is_easy = lambda x: 2 <= len(x) <= 4 or len(x) == 7

def is_three(legend, pattern):
    return len(pattern) == 5 and set(legend[1]).issubset(set(pattern))

def is_nine(legend, pattern):
    return len(set(pattern) - set(legend[7]) - set(legend[4])) == 1

def is_zero(legend, pattern):
    return set(legend[7]).issubset(set(pattern))# and set(pattern).issubset(set(legend[8]))

def is_six(legend, pattern):
    return pattern not in legend.values() and len(pattern) == 6

def is_five(legend, pattern):
    return pattern not in legend.values() and set(pattern).issubset(set(legend[6]))

def is_two(legend, pattern):
    return pattern not in legend.values()


def decypher(in_patterns):
    patterns = deque(sorted([pattern for pattern in in_patterns], key=len))
    legend = dict()

    # 1, 7, 4

    for num in [1, 7, 4]:
        legend[num] = patterns.popleft()

    # 8
    legend[8] = patterns.pop()
    for pattern in patterns:
        # 3
        if is_three(legend, pattern):
            legend[3] = pattern
        # 9
        elif is_nine(legend, pattern):
            legend[9] = pattern
        # 0
        elif is_zero(legend, pattern):
            legend[0] = pattern

        elif is_six(legend, pattern):
            legend[6] = pattern
        
    for pattern in patterns:
        if is_five(legend, pattern):
            legend[5] = pattern
        elif is_two(legend, pattern):
            legend[2] = pattern

    return {''.join(c for c in sorted(pattern)): digit for digit, pattern in legend.items()}


data = get_input('inputs/08.txt')


displays = []
for line in data:
    signal_pattern, digits = [line.split('|')[pos].split() for pos in {0,1}]
    displays.append((signal_pattern, digits))


party_1 = sum(is_easy(digit) for _, digits in displays for digit in digits)

party_2 = 0
for patterns, digits in displays:
    solution = ''
    translator = decypher(patterns)
    for code in digits:
        scode = ''.join(c for c in sorted(code))
        solution += str(translator[scode])
    party_2 += int(solution)


print_solutions(party_1, party_2)
