from santas_little_helpers import *
from collections import Counter

data = get_input('inputs/05.txt')
data = get_input('inputs/05-ex.txt')

def set_from_ends(starts, ends):
    s_x, s_y = starts
    e_x, e_y = ends
    if s_x > e_x:
        s_x, e_x = e_x, s_x
    if s_y > e_y:
        s_y, e_y = e_y, s_y
    if s_x == e_x or s_y == e_y:
        return {(x, y) for x in range(s_x, e_x+1) for y in range(s_y, e_y+1)}
    else:
       return set()

all_numbers = set()
party_1 = 0
ind_size = 0
all_nums_list = []
for line in data:

    start, end = line.split('->')
    starts = (int(num) for num in start.split(','))
    ends = (int(num) for num in end.split(','))
    add_set = set_from_ends(starts, ends)
    all_nums_list += list(add_set)


    all_numbers |= add_set
    ind_size += len(add_set)

    # print(len(all_numbers), ind_size)

points_count = Counter(all_nums_list)
#print(points_count)
for coord, count in points_count.most_common():
    if count >= 2:
        party_1 += 1


print_solutions(party_1)

# not 6167
