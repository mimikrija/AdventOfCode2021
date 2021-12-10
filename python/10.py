# Day 10: Syntax Scoring

from santas_little_helpers import *


POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137, None: 0,}
AUTOCOMPLETE_POINTS = { ')': 1, ']': 2, '}': 3, '>': 4, None: 0,}

close_it = str.maketrans('([{<>}])', ')]}><{[(')

def calculate_score(remaining):
    score = 0
    for char in remaining:
        score = score*5 + AUTOCOMPLETE_POINTS[char]
    return score

def autocomplete(in_line):
    opens = []
    for current in list(in_line):
        if current in '([{<':
            opens.append(current)
        else:
            last_opened = opens.pop()
            if current.translate(close_it) == last_opened:
                pass
            else:
                # incomplete line! return first illegal
                return current
    # if line is legal we get here and return list of needed closing chars
    completion = ''.join(o for o in reversed(opens))
    completion = completion.translate(close_it)
    return list(completion)


lines = get_input('inputs/10.txt')
analysed_lines = [autocomplete(line) for line in lines]

party_1 = sum(POINTS[line] for line in analysed_lines if isinstance(line, str))

completion_strings = (line for line in analysed_lines if isinstance(line, list))
scores = [calculate_score(remaining) for remaining in completion_strings]
party_2 = sorted(scores)[len(scores)//2]

print_solutions(party_1, party_2)
