# Day 10: Syntax Scoring

from santas_little_helpers import *
from collections import deque


lines = get_input('inputs/10.txt')

POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0,}
AUTOCOMPLETE_POINTS = { ')': 1, ']': 2, '}': 3, '>': 4, None: 0,}
MATCHING = {')': '(', ']': '[', '}': '{', '>': '<',}
MATCHING_rev = {op: cl for cl, op in MATCHING.items()}

def calculate_score(remaining):
    score = 0
    for char in remaining:
        score = score*5 + AUTOCOMPLETE_POINTS[char]
    return score

def autocomplete(in_line, is_part_2=False):
    line = deque(in_line)
    opens = deque()
    while line:
        current = line.popleft()
        if current in ('([{<'):
            opens.append(current)
        elif current in (')]}>'):
            last_opened = opens.pop()
            if MATCHING[current] == last_opened:
                pass
            else:
                # incomplete line! return first illegal
                return current
    if is_part_2:
        return [MATCHING_rev[c] for c in reversed(list(opens))]


party_1 = sum(POINTS[autocomplete(line)] for line in lines)

incomplete_lines = [line for line in lines if autocomplete(line) is None]

completion_strings = [autocomplete(line, True) for line in incomplete_lines]
scores = [calculate_score(remaining) for remaining in completion_strings]
party_2 = sorted(scores)[len(scores)//2]

print_solutions(party_1, party_2)
