import sys
import time

# NB_STEPS = 6
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
    
    plots = set([start])
    for _ in range(NB_STEPS):
        new_plots = set()
        for plot in plots:
            new_plots.update(get_next_steps(my_map, plot))
        plots = new_plots
    
    nb_plots = len(plots)

    # plot --------------------------------------------
    for i, line in enumerate(my_map):
        for j, char in enumerate(list(line)):
            if (i, j) in plots:
                print('O', end = '')
            else:
                print(char, end = '')
        print()
    # --------------------------------------------------

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of garden plots the Elf could reach is: {nb_plots}')

if __name__ == '__main__':
    main(sys.argv[1])