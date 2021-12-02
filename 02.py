# 

from santas_little_helpers import *

MOVE = {
    'forward': 1+0j,
    'down': 0-1j,
    'up': 0+1j,
}

MOVE_AIM = {
    'forward': 0,
    'down': 1,
    'up': -1,
}

data = get_input('inputs/02.txt')

position = 0+0j

for instruction in data:
    where, qt = instruction.split()
    qt = int(qt)
    position += MOVE[where]*qt
    
party_1 = int(position.real * position.imag)

print_solutions(party_1)

position = 0+0j
aim = 0

for instruction in data:
    where, qt = instruction.split()
    qt = int(qt)
    aim += MOVE_AIM[where]*qt
    if where == 'forward':
        position += complex(qt, aim*qt)
print(aim)

party_2 = int(position.real * position.imag)
print_solutions(party_1, party_2)
