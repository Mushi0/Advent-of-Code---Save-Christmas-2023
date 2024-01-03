import sys
import time

# define the direction: 
def beam(beam_coord, direction, map):
    if (beam_coord[0] < len(map) and 
           beam_coord[1] < len(map[0]) and 
           beam_coord[0] >= 0 and
           beam_coord[1] >= 0):
        if direction == 'right':
            i = beam_coord[1]
            while map[beam_coord[0]][i] in '.-#':
                if map[beam_coord[0]][i] == '.':
                    map[beam_coord[0]][i] = '#'
                i += 1
                if i == len(map[0]):
                    return map
            if map[beam_coord[0]][i] == '\\':
                return beam((beam_coord[0] + 1, i), 'down', map)
            elif map[beam_coord[0]][i] == '/':
                return beam((beam_coord[0] - 1, i), 'up', map)
            elif map[beam_coord[0]][i] == '|':
                map_1 = beam((beam_coord[0] - 1, i), 'up', map)
                map_2 = beam((beam_coord[0] + 1, i), 'down', map)
                for i, line in map_1:
                    for j, c in line:
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
        
        elif direction == 'left':
            i = beam_coord[1]
            while map[beam_coord[0]][i] in '.-#':
                if map[beam_coord[0]][i] == '.':
                    map[beam_coord[0]][i] = '#'
                i -= 1
                if i == -1:
                    return map
            if map[beam_coord[0]][i] == '\\':
                return beam((beam_coord[0] - 1, i), 'up', map)
            elif map[beam_coord[0]][i] == '/':
                return beam((beam_coord[0] + 1, i), 'down', map)
            elif map[beam_coord[0]][i] == '|':
                map_1 = beam((beam_coord[0] - 1, i), 'up', map)
                map_2 = beam((beam_coord[0] + 1, i), 'down', map)
                for i, line in map_1:
                    for j, c in line:
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
        
        elif direction == 'up':
            i = beam_coord[0]
            while map[i][beam_coord[1]] in '.|#':
                if map[i][beam_coord[1]] == '.':
                    map[i][beam_coord[1]] = '#'
                i -= 1
                if i == -1:
                    return map
            if map[i][beam_coord[1]] == '\\':
                return beam((i, beam_coord[1] - 1), 'left', map)
            elif map[i][beam_coord[1]] == '/':
                return beam((i, beam_coord[1] + 1), 'right', map)
            elif map[i][beam_coord[1]] == '-':
                map_1 = beam((i, beam_coord[1] - 1), 'left', map)
                map_2 = beam((i, beam_coord[1] + 1), 'right', map)
                for i, line in map_1:
                    for j, c in line:
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
        
        elif direction == 'down':
            i = beam_coord[0]
            while map[i][beam_coord[1]] in '.|#':
                if map[i][beam_coord[1]] == '.':
                    map[i][beam_coord[1]] = '#'
                i += 1
                if i == len(map):
                    return map
            if map[i][beam_coord[1]] == '\\':
                return beam((i, beam_coord[1] + 1), 'right', map)
            elif map[i][beam_coord[1]] == '/':
                return beam((i, beam_coord[1] - 1), 'left', map)
            elif map[i][beam_coord[1]] == '-':
                map_1 = beam((i, beam_coord[1] - 1), 'left', map)
                map_2 = beam((i, beam_coord[1] + 1), 'right', map)
                for i, line in map_1:
                    for j, c in line:
                        if c == '#':
                            map_2[i][j] = '#'
                return map_2
    
    for line in map:
        for c in line:
            print(c, end='')
        print()
    return map

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        map = []
        for line in f:
            map.append(list(line.strip()))
    
    map = beam((0, 0), 'right', map)    
    total_tiles = sum(line.count('#') for line in map)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of tiles end up being energized is: {total_tiles}')

if __name__ == '__main__':
    main(sys.argv[1])