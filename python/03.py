
from santas_little_helpers import *
from collections import Counter

consumption = lambda x, y: int(x, 2) * int(y, 2)

data = get_input('inputs/03.txt')
size = len(data[0])


gamma = ''.join(Counter(column_position).most_common()[0][0] for column_position in zip(*data))
# epsilon is just an inverse of gamma
epsilon = gamma.translate(str.maketrans('01', '10'))

party_1 = consumption(gamma, epsilon)


# party 2

def scrubox(data, criterion='most'):
    result = list(data)
    # loop through the columns of data input
    for column_pos in range(size):
        # since data reduces per each iteration, we need to construct the column manually
        current_column = [c[column_pos] for c in result]
        # do it only if there is at least 2 numbers left
        if len(result) > 1:
            # if criterion is equal to 'least' we actually point to the most common beacuse
            # everything is zero-indexed, and vice-versa
            # this will work only if we have two possible bit values (we do)
            bit_value, quantity = Counter(current_column).most_common()[int(criterion == 'least')]
            # check if we have a tie in numbers with/without the bit_value in that column
            if quantity == len(current_column) / 2:
                # and set the value to choose
                bit_value = str(int(criterion == 'most'))
            # keep only those numbers which have bit_value in current column position
            result = [bit for bit in result if bit[column_pos] == bit_value]
    # this works nice even though result is a list of strings ?
    return ''.join(c for c in result)

scrubber = scrubox(data, 'most')
oxygen = scrubox(data, 'least')

party_2 = consumption(scrubber, oxygen)

print_solutions(party_1, party_2)
