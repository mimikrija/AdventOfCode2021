# Day 15: Chiton

from santas_little_helpers import *
from santas_little_helpers.helpers import *
from queue import PriorityQueue

data = get_input('inputs/15.txt')
RISK_LEVELS = {(x, y): int(num) for x, row in enumerate(data) for y, num in enumerate(row)}
GRID_SIZE = len(data)


def calculate_risk(coordinate):
    try:
        return RISK_LEVELS[coordinate]
    except:
        mults =  [coord // GRID_SIZE for coord in coordinate]
        reduced_coord = tuple(c - GRID_SIZE*cmult for c, cmult in zip(coordinate, mults))
        risk = RISK_LEVELS[reduced_coord] + sum(mults)
        return risk % 9 if risk > 9 else risk


def find_cheapest_path(start, goal):
    '''Dijkstra algorithm from red blob games to find the cheapest path from `start` to `goal`'''
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()
        
        if current == goal:
            return cost_so_far[goal]

        for next_position in get_four_neighbors(current, 5*GRID_SIZE):
            new_cost = cost_so_far[current] + calculate_risk(next_position)
            if next_position not in cost_so_far or new_cost < cost_so_far[next_position]:
                cost_so_far[next_position] = new_cost
                priority = new_cost
                frontier.put((priority, next_position))
                came_from[next_position] = current


start = (0, 0)
ends = (tuple(n*GRID_SIZE-1 for _ in range(2)) for n in (1, 5))

party_1, party_2 = (find_cheapest_path(start, end) for end in ends)
print_solutions(party_1, party_2)

def test_one():
    assert party_1 == 410
def test_two():
    assert party_2 == 2809
