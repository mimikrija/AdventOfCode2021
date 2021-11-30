def get_input(file_name, separator='\n'):
    """ Reads in data present in `file_name` separated by `separator` string. """
    with open(file_name) as input_file:
        input_data = input_file.read().split(separator)
    return input_data

def print_solutions(part_1, part_2 = None):
    print(f'Part 1 solution is: {part_1}')
    if part_2:
        print(f'Part 2 solution is: {part_2}')

def add_wrap(num_1, num_2, limit, start=0):
    " Returns sum of `num_1` and `num_2` wrapped around to `start` they go over `limit`"
    return start + (num_1 + num_2)%(limit+1)
