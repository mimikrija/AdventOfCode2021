# Day 18: Snailfish

from collections import deque
from itertools import permutations

from santas_little_helpers.helpers import *

intenize = lambda x: int(x) if x not in '[]' else x

def format_data(in_string):
    return [intenize(c) for c in in_string if c != ',']

def print_pretty(in_list):
    print (''.join(str(c) for c in in_list))

def add_snails(one, two):
    return ['['] + one + two + [']']

def find_split_point(snail):
    count_open = 0
    for pos, c in enumerate(snail):
        count_open += int(c == '[') - int(c ==']')
        if (to_explode := count_open > 4):
            break
    if not to_explode:
        return None, None, None
    left = snail[0:pos]
    right = snail[pos+4:]
    exploding_pair = snail[pos+1:pos+3]
    return left, exploding_pair, right

def add_to_left(in_left, number):
    left = deque(in_left)
    rest = deque([])
    while left:
        current = left.pop()
        if isinstance(current, int):
            return list(left) + [current + number] + list(rest)
        rest.appendleft(current)
    return in_left

def add_to_right(in_right, number):
    right = deque(in_right)
    rest = []
    while right:
        current = right.popleft()
        if isinstance(current, int):
            return rest + [current + number] + list(right)
        rest.append(current)
    return in_right

def explode(in_snail):
    left, pair, right = find_split_point(in_snail)
    if not left:
        return False, in_snail
    left_add, right_add = pair
    return True, add_to_left(left, left_add) + [0] + add_to_right(right, right_add)

def split(in_snail):
    snail = deque(in_snail)
    left = []
    while snail:
        current = snail.popleft()
        if isinstance(current, int) and current >= 10:
            return True, left + ['['] + [(half:=current//2)] + [current-half] + [']'] + list(snail)
        left.append(current)
    return False, in_snail

def magnitude(in_snail, counter=0):
    snail=list(in_snail)
    print('in snail', snail)
    if sum(isinstance(c, int) for c in snail) == 2:
        return(sum(c) for c in snail if isinstance(c, int))

    for pos, (first, second) in enumerate(zip(snail, snail[1:])):
        if isinstance(first, int) and isinstance(second, int):
            mag = 3* first + 2*second
            print(snail[:pos] + [mag] + snail[pos+3:])
            if counter == 10:
                return
            magnitude(snail[:pos] + [mag] + snail[pos+3:], counter+1)
            break


def to_list(in_snail):
    result = []
    for first, second in zip(in_snail, in_snail[1:]):
        result.append(first)
        if isinstance(first, int) and second == '[' or isinstance(first, int) and isinstance(second, int) or first == ']' and isinstance(second, int) or first == ']' and second == '[':
            result.append(',')
    result.append(']')

    return eval(''.join(str(c) for c in result))


def magnitude(snail):
    if isinstance(snail, int):
        return snail
    left, right = snail
    if all(isinstance(p, int) for p in (left, right)):
        return 3*left + 2*right
    else:
        return 3*magnitude(left) + 2* magnitude(right)

def get_magnitude(in_snail):
    snail = to_list(in_snail)
    return magnitude(snail)


def reduce(in_snail):
    snail = list(in_snail)
    while True:
        #print_pretty(snail)
        exploded, snail = explode(snail)
        if exploded:
            continue
        splitted, snail = split(snail)
        if not splitted:
            return snail

def solve_homework(homework):
    current_result = homework[0]
    for second in homework[1:]:
        current_result = add_snails(current_result, second)
        current_result = reduce(current_result)
    
    #print_pretty(current_result)
    return get_magnitude(current_result)


snail_homework = [format_data(line) for line in get_input('inputs/18.txt')]



def max_result(homework):
    return max(get_magnitude(reduce(add_snails(first, second))) for first, second in permutations(homework, 2))


party_1 = solve_homework(snail_homework)
party_2 = max_result(snail_homework)

print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 3411
def test_two():
    assert party_2 == 4680
