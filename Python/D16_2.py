import sys
import time
from tqdm import tqdm
import copy

def beam(beam_coord, direction, map, visited = None, visited_morrors = None):
    if visited is None:
        visited = set()
    if visited_morrors is None:
        visited_morrors = set()
    if (beam_coord, direction) in visited:
        return visited, visited_morrors, map
    if (beam_coord[0] < len(map) and 
           beam_coord[1] < len(map[0]) and 
           beam_coord[0] >= 0 and
           beam_coord[1] >= 0):
        visited.add((beam_coord, direction))
        if direction == 'right':
            i = beam_coord[1]
            while map[beam_coord[0]][i] in '.-#':
                if map[beam_coord[0]][i] == '.':
                    map[beam_coord[0]][i] = '#'
                elif map[beam_coord[0]][i] == '-':
                    visited_morrors.add((beam_coord[0], i))
                i += 1
                if i == len(map[0]):
                    return visited, visited_morrors, map
            if map[beam_coord[0]][i] == '\\':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] + 1, i), 'down', map, visited, visited_morrors)
            elif map[beam_coord[0]][i] == '/':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] - 1, i), 'up', map, visited, visited_morrors)
            elif map[beam_coord[0]][i] == '|':
                visited_morrors.add((beam_coord[0], i))
                visited_1, visited_morrors_1, map_1 = beam((beam_coord[0] - 1, i), 'up', map, visited, visited_morrors)
                visited_2, visited_morrors_2, map_2 = beam((beam_coord[0] + 1, i), 'down', map, visited, visited_morrors)
                visited = visited_1.union(visited_2)
                visited_morrors = visited_morrors_1.union(visited_morrors_2)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return visited, visited_morrors, map_2
        
        elif direction == 'left':
            i = beam_coord[1]
            while map[beam_coord[0]][i] in '.-#':
                if map[beam_coord[0]][i] == '.':
                    map[beam_coord[0]][i] = '#'
                elif map[beam_coord[0]][i] == '-':
                    visited_morrors.add((beam_coord[0], i))
                i -= 1
                if i == -1:
                    return visited, visited_morrors, map
            if map[beam_coord[0]][i] == '\\':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] - 1, i), 'up', map, visited, visited_morrors)
            elif map[beam_coord[0]][i] == '/':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] + 1, i), 'down', map, visited, visited_morrors)
            elif map[beam_coord[0]][i] == '|':
                visited_morrors.add((beam_coord[0], i))
                visited_1, visited_morrors_1, map_1 = beam((beam_coord[0] - 1, i), 'up', map, visited, visited_morrors)
                visited_2, visited_morrors_2, map_2 = beam((beam_coord[0] + 1, i), 'down', map, visited, visited_morrors)
                visited = visited_1.union(visited_2)
                visited_morrors = visited_morrors_1.union(visited_morrors_2)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return visited, visited_morrors, map_2
        
        elif direction == 'up':
            i = beam_coord[0]
            while map[i][beam_coord[1]] in '.|#':
                if map[i][beam_coord[1]] == '.':
                    map[i][beam_coord[1]] = '#'
                elif map[i][beam_coord[1]] == '|':
                    visited_morrors.add((i, beam_coord[1]))
                i -= 1
                if i == -1:
                    return visited, visited_morrors, map
            if map[i][beam_coord[1]] == '\\':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] - 1), 'left', map, visited, visited_morrors)
            elif map[i][beam_coord[1]] == '/':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] + 1), 'right', map, visited, visited_morrors)
            elif map[i][beam_coord[1]] == '-':
                visited_morrors.add((i, beam_coord[1]))
                visited_1, visited_morrors_1, map_1 = beam((i, beam_coord[1] - 1), 'left', map, visited, visited_morrors)
                visited_2, visited_morrors_2, map_2 = beam((i, beam_coord[1] + 1), 'right', map, visited, visited_morrors)
                visited = visited_1.union(visited_2)
                visited_morrors = visited_morrors_1.union(visited_morrors_2)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return visited, visited_morrors, map_2
        
        elif direction == 'down':
            i = beam_coord[0]
            while map[i][beam_coord[1]] in '.|#':
                if map[i][beam_coord[1]] == '.':
                    map[i][beam_coord[1]] = '#'
                elif map[i][beam_coord[1]] == '|':
                    visited_morrors.add((i, beam_coord[1]))
                i += 1
                if i == len(map):
                    return visited, visited_morrors, map
            if map[i][beam_coord[1]] == '\\':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] + 1), 'right', map, visited, visited_morrors)
            elif map[i][beam_coord[1]] == '/':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] - 1), 'left', map, visited, visited_morrors)
            elif map[i][beam_coord[1]] == '-':
                visited_morrors.add((i, beam_coord[1]))
                visited_1, visited_morrors_1, map_1 = beam((i, beam_coord[1] - 1), 'left', map, visited, visited_morrors)
                visited_2, visited_morrors_2, map_2 = beam((i, beam_coord[1] + 1), 'right', map, visited, visited_morrors)
                visited = visited_1.union(visited_2)
                visited_morrors = visited_morrors_1.union(visited_morrors_2)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return visited, visited_morrors, map_2
    
    return visited, visited_morrors, map

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        original_map = []
        for line in f:
            original_map.append(list(line.strip()))
    
    max_total_tiles = 0
    len_map = len(original_map)
    len_line = len(original_map[0])
    for i in tqdm(range(len_map)):
        map = copy.deepcopy(original_map)
        _, visited_morrors, map = beam((i, 0), 'right', map)
        total_tiles = sum(line.count('#') for line in map) + len(visited_morrors)
        if total_tiles > max_total_tiles:
            max_total_tiles = total_tiles
        
        map = copy.deepcopy(original_map)
        _, visited_morrors, map = beam((i, len_line - 1), 'left', map)
        total_tiles = sum(line.count('#') for line in map) + len(visited_morrors)
        if total_tiles > max_total_tiles:
            max_total_tiles = total_tiles
    
    for j in tqdm(range(len_line)):
        print(j)
        map = copy.deepcopy(original_map)
        _, visited_morrors, map = beam((0, j), 'down', map)
        total_tiles = sum(line.count('#') for line in map) + len(visited_morrors)
        if total_tiles > max_total_tiles:
            max_total_tiles = total_tiles
        map = copy.deepcopy(original_map)
        _, visited_morrors, map = beam((len_map - 1, j), 'up', map)
        total_tiles = sum(line.count('#') for line in map) + len(visited_morrors)
        if total_tiles > max_total_tiles:
            max_total_tiles = total_tiles

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The maximum number of tiles end up being energized is: {max_total_tiles}')

if __name__ == '__main__':
    main(sys.argv[1])