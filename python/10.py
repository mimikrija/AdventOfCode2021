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

MATCHING = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

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


party_1 = sum(POINTS[find_first_illegal(line)] for line in lines)

