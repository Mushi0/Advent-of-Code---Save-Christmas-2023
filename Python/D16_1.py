import sys
import time

visited_morrors = set()

def beam(beam_coord, direction, map, visited = set()):
    if (beam_coord, direction) in visited:
        return map
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
                    return map
            if map[beam_coord[0]][i] == '\\':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] + 1, i), 'down', map, visited)
            elif map[beam_coord[0]][i] == '/':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] - 1, i), 'up', map, visited)
            elif map[beam_coord[0]][i] == '|':
                visited_morrors.add((beam_coord[0], i))
                map_1 = beam((beam_coord[0] - 1, i), 'up', map, visited)
                map_2 = beam((beam_coord[0] + 1, i), 'down', map, visited)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
        
        elif direction == 'left':
            i = beam_coord[1]
            while map[beam_coord[0]][i] in '.-#':
                if map[beam_coord[0]][i] == '.':
                    map[beam_coord[0]][i] = '#'
                elif map[beam_coord[0]][i] == '-':
                    visited_morrors.add((beam_coord[0], i))
                i -= 1
                if i == -1:
                    return map
            if map[beam_coord[0]][i] == '\\':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] - 1, i), 'up', map, visited)
            elif map[beam_coord[0]][i] == '/':
                visited_morrors.add((beam_coord[0], i))
                return beam((beam_coord[0] + 1, i), 'down', map, visited)
            elif map[beam_coord[0]][i] == '|':
                visited_morrors.add((beam_coord[0], i))
                map_1 = beam((beam_coord[0] - 1, i), 'up', map, visited)
                map_2 = beam((beam_coord[0] + 1, i), 'down', map, visited)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
        
        elif direction == 'up':
            i = beam_coord[0]
            while map[i][beam_coord[1]] in '.|#':
                if map[i][beam_coord[1]] == '.':
                    map[i][beam_coord[1]] = '#'
                elif map[i][beam_coord[1]] == '|':
                    visited_morrors.add((i, beam_coord[1]))
                i -= 1
                if i == -1:
                    return map
            if map[i][beam_coord[1]] == '\\':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] - 1), 'left', map, visited)
            elif map[i][beam_coord[1]] == '/':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] + 1), 'right', map, visited)
            elif map[i][beam_coord[1]] == '-':
                visited_morrors.add((i, beam_coord[1]))
                map_1 = beam((i, beam_coord[1] - 1), 'left', map, visited)
                map_2 = beam((i, beam_coord[1] + 1), 'right', map, visited)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
        
        elif direction == 'down':
            i = beam_coord[0]
            while map[i][beam_coord[1]] in '.|#':
                if map[i][beam_coord[1]] == '.':
                    map[i][beam_coord[1]] = '#'
                elif map[i][beam_coord[1]] == '|':
                    visited_morrors.add((i, beam_coord[1]))
                i += 1
                if i == len(map):
                    return map
            if map[i][beam_coord[1]] == '\\':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] + 1), 'right', map, visited)
            elif map[i][beam_coord[1]] == '/':
                visited_morrors.add((i, beam_coord[1]))
                return beam((i, beam_coord[1] - 1), 'left', map, visited)
            elif map[i][beam_coord[1]] == '-':
                visited_morrors.add((i, beam_coord[1]))
                map_1 = beam((i, beam_coord[1] - 1), 'left', map, visited)
                map_2 = beam((i, beam_coord[1] + 1), 'right', map, visited)
                for i, line in enumerate(map_1):
                    for j, c in enumerate(line):
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
    
    return map

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        map = []
        for line in f:
            map.append(list(line.strip()))
    
    map = beam((0, 0), 'right', map)
    
    # # plot-----------------------------------------------
    # for i, line in enumerate(map):
    #     for j, c in enumerate(line):
    #         if c in '\\/|-' and (i, j) in visited_morrors:
    #             print('#', end='')
    #         else:
    #             print(c, end='')
    #     print()
    # # end plot-------------------------------------------
    
    total_tiles = sum(line.count('#') for line in map) + len(visited_morrors)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of tiles end up being energized is: {total_tiles}')

if __name__ == '__main__':
    main(sys.argv[1])