
from santas_little_helpers import *
from collections import defaultdict
data = get_input('inputs/08.txt')
#data = get_input('inputs/08-ex.txt')
signals = [[signal for signal in line.split('|')[0].split()] for line in data]

def decypher(patterns):
    DIGIT_SIZE = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
    }
    SIZE_DIGIT = defaultdict(set)
    for digit, size in DIGIT_SIZE.items():
        SIZE_DIGIT[size].add(digit)
    # create dict
    unknown = defaultdict(set)
    for pattern in patterns:
        unknown[len(pattern)].add(pattern)
    translate = dict()
    # find easy ones
    for size, patterns in unknown.items():
        if len(patterns) == 1:
            digit = SIZE_DIGIT[size].pop()
            translate[digit] = unknown[size].pop()
    # find 3
    for candidate in unknown[DIGIT_SIZE[3]]:
        if all(c in list(candidate) for c in translate[1]):
            translate[3] = candidate
            unknown[DIGIT_SIZE[3]].remove(candidate)
            break
    # find 6
    for candidate in unknown[DIGIT_SIZE[6]]:
        if not all(c in list(candidate) for c in translate[7]):
            translate[6] = candidate
            unknown[DIGIT_SIZE[6]].remove(candidate)
            break
    

  
    # find 9
    for candidate in unknown[DIGIT_SIZE[9]]:
        if all(c in candidate for c in translate[4]):
            translate[9] = candidate
            unknown[DIGIT_SIZE[9]].remove(candidate)
            break
    # find 0
    translate[0] = unknown[DIGIT_SIZE[0]].pop()

    # find 5
    for candidate in unknown[DIGIT_SIZE[5]]:
        if all(c in translate[6] for c in list(candidate)):
            translate[5] = candidate
            unknown[DIGIT_SIZE[5]].remove(candidate)
            break
    # find 2
    translate[2] = unknown[DIGIT_SIZE[2]].pop()

    final = dict()
    for digit, code in translate.items():
        codes = ''.join(c for c in sorted(code))
        final[codes] = digit

    return final

easy_data = [line.split('|')[1].split() for line in data]

party_2 = 0
for patterns, digits in zip(signals, easy_data):
    solution = ''
    for code in digits:
        scode = ''.join(c for c in sorted(code))
        solution += str(decypher(patterns)[scode])
    #print(solution)
    party_2 += int(solution)

print(party_2)
quit()
solution = ''
for code in easy_data[0]:
    print(code)
    scode = ''.join(c for c in sorted(code))
    solution += str(decypher(signals[0])[scode])

print(solution)

quit()
    

easy_data = [line.split('|')[1] for line in data]
counter = 0
for line in easy_data:
    for digit in line.split():
        if len(digit) == 2:
            counter += 1
        if len(digit) == 4:
            counter += 1
        if len(digit) == 3:
            counter += 1
        if len(digit) == 7:
            counter += 1

party_1 = counter
print_solutions(party_1)

segments = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

digits_vs_signal_length = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

def count_easy_digits():
    counter = 0
    for line in easy_data:
        for digit in line.split():
            code = ''.join(c for c in sorted(digit))
            print(digit, code, line)
            num = segments[code]
            if num in (1, 4, 7, 8):
                counter += 1

            
    return counter

print(count_easy_digits())