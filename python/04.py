# Day 4: Giant Squid

from santas_little_helpers import *

class Card:
    def __init__(self, raw_card):
        self.rows = [[int(number) for number in row.split()] for row in raw_card.split('\n')]
        self.columns = list(zip(*self.rows))
        self.all_numbers = [num for row in self.rows for num in row]
        self.score = 0
        self.won = False

    def bingo_hit(self, drawn_numbers):
        for card_element in self.rows + self.columns:
            if all(card_number in drawn_numbers for card_number in card_element) and not self.won:
                self.score = self.get_score(drawn_numbers)
                self.won = True
                return True
        return False
    
    def get_score(self, drawn_numbers):
        return sum(number for number in self.all_numbers if number not in drawn_numbers)*drawn_numbers[-1]



data = get_input('inputs/04.txt', False, '\n\n')

numbers_to_draw = list(map(int, data[0].split(',')))


bingo_cards = [Card(raw_card) for raw_card in data[1:]]

def play_bingo(bingo_cards, numbers_to_draw):
    winning_cards = []
    for pos, _ in enumerate(numbers_to_draw, 5):
        so_far_drawn_numbers = numbers_to_draw[:pos]
        winning_cards += [card for card in bingo_cards if card.bingo_hit(so_far_drawn_numbers)]

    return winning_cards[0].score, winning_cards[-1].score


party_1, party_2 = play_bingo(bingo_cards, numbers_to_draw)

print_solutions(party_1, party_2)
