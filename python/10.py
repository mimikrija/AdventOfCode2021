from santas_little_helpers import *
from collections import deque


lines = get_input('inputs/10.txt')
#lines = get_input('inputs/example.txt')

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0,
}

AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    None: 0,
}

def calculate_score(remaining):
    score = 0
    for char in remaining:
        score *= 5
        score += AUTOCOMPLETE_POINTS[char]
    return score

MATCHING = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

MATCHING_rev = {op: cl for cl, op in MATCHING.items()}

def find_first_illegal(in_line):
    chars = deque(in_line)
    open = deque()
    while chars:
        current = chars.popleft()
        if current in ('([{<'):
            open.append(current)
        elif current in (')]}>'):
            last_opened = open.pop()
            if MATCHING[current] == last_opened:
                pass
            else:
                return current

def get_closing(in_line):
    chars = deque(in_line)
    open = deque()
    while chars:
        current = chars.popleft()
        if current in ('([{<'):
            open.append(current)
        elif current in (')]}>'):
            last_opened = open.pop()
            if MATCHING[current] == last_opened:
                pass
    return [MATCHING_rev[c] for c in reversed(list(open))]

party_1 = sum(POINTS[find_first_illegal(line)] for line in lines)

incomplete_lines = [line for line in lines if find_first_illegal(line) is None]
print(len(incomplete_lines))

completion_strings = [get_closing(line) for line in incomplete_lines]
scores = [calculate_score(remaining) for remaining in completion_strings]
party_2 = sorted(scores)[len(scores)//2]

print_solutions(party_1, party_2)