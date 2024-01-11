import sys
import time

NB_STEPS = 64

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_next_steps(my_map: list, pos: tuple):
    next_steps = []
    for d in dirs:
        if my_map[pos[0] + d[0]][pos[1] + d[1]] != '#':
            next_steps.append((pos[0] + d[0], pos[1] + d[1]))
    return next_steps

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()
    
    for line in my_map:
        if 'S' in line:
            start = (my_map.index(line), line.index('S'))
            break
    
    diamond_plots = 0
    for i, line in enumerate(my_map):
        for j, char in enumerate(line):
            horizontal_dist = abs(i - start[0])
            vertical_dist = abs(j - start[1])
            if (char not in '#S' and 
                horizontal_dist + vertical_dist <= NB_STEPS and 
                (horizontal_dist + vertical_dist) % 2 == (NB_STEPS % 2) and 
                (not (my_map[i - 1][j] == '#' and my_map[i + 1][j] == '#' and 
                      my_map[i][j - 1] == '#' and my_map[i][j + 1] == '#'))):
                diamond_plots += 1

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of garden plots the Elf could reach is: {diamond_plots}')

if __name__ == '__main__':
    main(sys.argv[1])