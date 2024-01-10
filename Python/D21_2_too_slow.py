import sys
import time
from collections import deque
from tqdm import tqdm

NB_STEPS = 5000
# NB_STEPS = 26501365

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def map_grow(dir):
    global stones
    global plots
    global new_plots
    global map_size
    
    if dir == 'up':
        new_stones = stones.copy()
        for stone in stones:
            new_stones.add((stone[0] + map_size[0], stone[1]))
        stones = new_stones

        queue = plots.copy()
        plots.clear()
        while queue:
            plot = queue.popleft()
            plots.append((plot[0] + map_size[0], plot[1]))
        
        queue = new_plots.copy()
        new_plots.clear()
        while queue:
            plot = queue.popleft()
            new_plots.append((plot[0] + map_size[0], plot[1]))

        map_size[0] *= 2
    elif dir == 'down':
        new_stones = stones.copy()
        for stone in stones:
            new_stones.add((stone[0] + map_size[0], stone[1]))
        stones = new_stones

        map_size[0] *= 2
    elif dir == 'left':
        new_stones = stones.copy()
        for stone in stones:
            new_stones.add((stone[0], stone[1] + map_size[1]))
        stones = new_stones
        
        queue = plots.copy()
        plots.clear()
        while queue:
            plot = queue.popleft()
            plots.append((plot[0], plot[1] + map_size[1]))
        
        queue = new_plots.copy()
        new_plots.clear()
        while queue:
            plot = queue.popleft()
            new_plots.append((plot[0], plot[1] + map_size[1]))

        map_size[1] *= 2
    elif dir == 'right':
        new_stones = stones.copy()
        for stone in stones:
            new_stones.add((stone[0], stone[1] + map_size[1]))
        stones = new_stones
        
        map_size[1] *= 2
    
def get_next_steps(pos: tuple):
    global stones
    global plots
    global new_plots
    global map_size

    old_map_size = map_size.copy()
    next_steps = []
    change_size = []
    for d in dirs:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos[0] < 0:
            map_grow('up')
            change_size.append('up')
        elif new_pos[0] >= map_size[0]:
            map_grow('down')
        elif new_pos[1] < 0:
            map_grow('left')
            change_size.append('left')
        elif new_pos[1] >= map_size[1]:
            map_grow('right')
        
        if new_pos not in stones:
            next_steps.append(new_pos)
    
    # update all nodes if changed map size
    if 'up' in change_size:
        for i, plot in enumerate(next_steps):
            next_steps[i] = (plot[0] + old_map_size[0], plot[1])
    if 'left' in change_size:
        for i, plot in enumerate(next_steps):
            next_steps[i] = (plot[0], plot[1] + old_map_size[1])

    return next_steps

def main(DATA_INPUT):
    global stones
    global plots
    global new_plots
    global map_size

    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()
    
    map_size = [len(my_map), len(my_map[0])]

    stones = set()
    for i, line in enumerate(my_map):
        for j, char in enumerate(line):
            if char == '#':
                stones.add((i, j))
        if 'S' in line:
            start = (i, line.index('S'))
    
    plots = deque([start])
    for _ in tqdm(range(NB_STEPS)):
        new_plots = deque()
        while plots:
            plot = plots.popleft()
            new_plots.extend(get_next_steps(plot))
        plots = deque(set(new_plots))

    nb_plots = len(plots)

    # plot --------------------------------------------
    with open('map.txt', 'w') as f:
        for i in range(map_size[0]):
            line_to_write = ''
            for j in range(map_size[1]):
                if (i, j) in plots:
                    line_to_write += 'O'
                elif (i, j) in stones:
                    line_to_write += '#'
                else:
                    line_to_write += '.'
            f.write(line_to_write + '\n')
    # --------------------------------------------------

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of garden plots the Elf could reach is: {nb_plots}')

if __name__ == '__main__':
    main(sys.argv[1])