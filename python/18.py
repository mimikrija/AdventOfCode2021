from santas_little_helpers.helpers import *
from collections import deque


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
        if count_open > 4:
            break
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
    left_add, right_add = pair
    return add_to_left(left, left_add) + [0] + add_to_right(right, right_add)


snail_homework = [format_data(line) for line in get_input('inputs/18-e.txt')]

for sn in snail_homework:

    print_pretty(sn)
    print('becomes: ')
    print_pretty(explode(sn))
    print('------')

sn1 = format_data('[[[[4,3],4],4],[7,[[8,4],9]]]')
sn2 = format_data('[1,1]')

a = add_snails(sn1, sn2)
print_pretty(explode(a))