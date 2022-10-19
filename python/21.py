from santas_little_helpers.helpers import print_solutions
from collections import deque, Counter
from itertools import product


def deterministic_die():
    roll = 0
    while True:
        if roll < 100:
            roll += 1
        else:
            roll = 1
        yield roll


def wrap_position(in_num):
    remainder = in_num % 10
    if remainder == 0:
        return 10
    else:
        return remainder


def play_deterministic_game(initial_positions):
    scores = [0, 0]
    positions = list(initial_positions)
    is_player_two = False
    total_rolls = 0

    while not any(score >= 1000 for score in scores):
        total = sum(next(deterministic) for _ in range(3))
        new_pos = wrap_position(positions[is_player_two] + total)
        scores[is_player_two] += new_pos
        positions[is_player_two] = new_pos
        total_rolls += 3
        is_player_two = not is_player_two

    return total_rolls * min(scores)


DIRAC_DIE_SUMS = Counter(sum(tris) for tris in product((1, 2, 3), repeat=3))

def play_game(initial_state):
    universes = [0, 0]
    games = deque([initial_state])

    while games:
        positions, scores, player_two_turn, univs_leading_to_this  = games.pop()
        for roll, frequency in DIRAC_DIE_SUMS.items():
            new_univs_leading = univs_leading_to_this * frequency
            new_positions = list(positions)
            new_scores = list(scores)
            new_pos = positions[player_two_turn] + roll
            if new_pos > 10:
                new_positions[player_two_turn] = new_pos - 10
            else:
                new_positions[player_two_turn] = new_pos
            new_scores[player_two_turn] += new_positions[player_two_turn]
            if any(score >= 21 for score in new_scores):
                universes[player_two_turn] += new_univs_leading
            else:
                games.append([new_positions, new_scores, not player_two_turn, new_univs_leading])

    return max(universes)




deterministic = deterministic_die()

initial_positions = [7, 6]
initial_scores = [0, 0]

party_1 = play_deterministic_game(initial_positions)


start_game = (initial_positions, initial_scores, False, 1)

party_2 = play_game(start_game)

print_solutions(party_1, party_2)
