# Day 12: Passage Pathing
from santas_little_helpers import *


def get_adjacent_vertices(edges, current):
    return {point for edge in edges for point in edge if current in edge and current != point}

def find_all_paths(edges, start, end, part2=False):
    def find_all_subpaths(start, end, path):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in get_adjacent_vertices(edges,start):
            if not part2:
                # allow visiting small caves only once
                if not (node in allowed_only_once and node in path):
                    paths.extend(find_all_subpaths(node, end, path))
            else:
                # allow visiting just one of the small caves twice
                lowers = [l for l in path if l.islower()]
                if len(lowers) - len(set(lowers)) <= 1 and not (node in allowed_only_once and path.count(node) == 2) and node != 'start':
                        paths.extend(find_all_subpaths(node, end, path))
        return paths
    return find_all_subpaths(start, end, [])


edges = [set(line.split('-')) for line in get_input('inputs/12.txt')]
allowed_only_once = {point for edge in edges for point in edge if not point.isupper()}

solutions = (len(find_all_paths(edges, 'start', 'end', is_part_2)) for is_part_2 in (False, True))

print_solutions(*solutions)
