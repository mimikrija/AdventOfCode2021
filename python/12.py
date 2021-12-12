import itertools
from santas_little_helpers import *
from itertools import combinations

def get_adjacent_vertices(edges, current):
    return {point for edge in edges for point in edge if current in edge and current != point}


edges = [set(line.split('-')) for line in get_input('inputs/12.txt')]
allowed_only_once = {point for edge in edges for point in edge if not point.isupper()} # - {'start', 'end'}

visited = {point: 0 for point in {point for edge in edges for point in edge}}
#print(visited)


def find_all_paths(graph, start, end):
    def find_all_paths_aux(start, end, path):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in get_adjacent_vertices(edges,start): # - allowed_only_once: # set(path):
            if not (node in allowed_only_once and node in path):
                paths.extend(find_all_paths_aux( node, end, path))
        return paths

    #adjlist = [set(graph.neighbors(node)) for node in xrange(graph.vcount())]
    return find_all_paths_aux( start, end, [])

print(len(find_all_paths(edges, 'start', 'end')))
quit()


def depth_first(edges, visited, current='start'):
    if visited[current] == 1 and current in allowed_only_once or current == 'end':
        return
    visited[current] += 1
    print('visit: ', current)
    for vertex in get_adjacent_vertices(edges, current):
        depth_first(edges, visited, vertex)

# for point in visited.keys():
#     print(point, get_adjacent_vertices(edges, point))

depth_first(edges, visited)

quit()
# for pair in combinations(visited.keys(), 2):
#     if set(pair) in edges:
#         print(pair)

def find_paths_from(edges, current, path=[]):
    print('current', current, 'path so far:', path)
    path.append(current)
    if current == 'end':
        print('returning:', path)
        return path
    for neighbor in get_adjacent_vertices(edges, current):
        print('neighbors', neighbor)
        if neighbor not in path:
            subpaths = find_paths_from(edges, neighbor, path)
            print(subpaths)
            for subpath in subpaths:
                path.extend(subpath)
        elif neighbor not in allowed_only_once:
            subpaths = find_paths_from(edges, neighbor, path)
            print(subpaths)
            for subpath in subpaths:
                path.extend(subpath)
    return path


print(find_paths_from(edges, 'start'))