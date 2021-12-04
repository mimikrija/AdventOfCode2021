from santas_little_helpers import *
from collections import deque

class Card:
    def __init__(self, raw_card):
        self.rows = [[int(number) for number in row.split()] for row in raw_card.split('\n')]
        self.columns = list(zip(*self.rows))
        self.all_numbers = [num for row in self.rows for num in row]

    def is_bingo(self, drawn_numbers):
        for card_element in self.rows + self.columns:
            if all(card_number in drawn_numbers for card_number in card_element):
                return True
        return False
    
    def get_score(self, drawn_numbers):
        return sum(number for number in self.all_numbers if number not in drawn_numbers)



data = get_input('inputs/04.txt', False, '\n\n')
#data = get_input('inputs/04-ex.txt', False, '\n\n')

numbers_to_draw = list(map(int, data[0].split(',')))


bingo_cards = []
for raw_card in data[1:]:
    card = Card(raw_card)
    bingo_cards.append(card)

drawn_numbers = numbers_to_draw[:4]
all_numbers = deque(numbers_to_draw[4:])

def play_bingo():
    while all_numbers:
        current_number = all_numbers.popleft()
        drawn_numbers.append(current_number)
        for card_number, card in enumerate(bingo_cards, 1):
            if card.is_bingo(drawn_numbers):
                return current_number * card.get_score(drawn_numbers)

party_1 = play_bingo()

print_solutions(party_1)

