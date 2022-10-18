from collections import deque, Counter
from itertools import product

DIRAC_DIE = {1, 2, 3}
DIRAC_DIE_SUMS = Counter(sum(tris) for tris in product((1, 2, 3), repeat=3))


initial_positions = [7, 6]
initial_scores = [0, 0]

start_game = (initial_positions, initial_scores, False, 1)



def play_game(initial_state):
    universes = [0, 0]

    games = deque([initial_state])

    while games:
        # do something to filter out multiple games
        positions, scores, player_two_turn, univs_leading_to_this  = games.pop()
        #print(positions, scores)
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
    return universes

solution = max(play_game(start_game))

print(solution)
