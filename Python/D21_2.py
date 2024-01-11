import sys
import time
import math

# Look carefully at the map, 
# After 65 steps, the reachable plots forms a diamond shape, 
# and just reach the edge of the map. 
# Therefore, just calculate how many 131 steps (width and height) are there, 
# and calculate one map. 

# NB_STEPS = 65*2
# NB_STEPS = 5000
NB_STEPS = 26_501_365

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_next_steps(my_map: list, pos: tuple):
    next_steps = []
    for d in dirs:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if (new_pos[0] < 0 or 
            new_pos[0] >= len(my_map) or 
            new_pos[1] < 0 or 
            new_pos[1] >= len(my_map[0])):
            continue
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
    for i in range(130):
        new_plots = set()
        for plot in plots:
            new_plots.update(get_next_steps(my_map, plot))
        plots = new_plots
        if i == 64:
            diamond_plots_odd = len(plots)
        elif i == 128:
            full_plots_odd = len(plots)
    full_plots_even = len(plots)
    print(full_plots_odd, full_plots_even, diamond_plots_odd)

    quotient = NB_STEPS // 131
    remainder = NB_STEPS % 131 # and here is just right 65, I think it's meant to be!

    # nb_plots = (quotient)*(quotient + 1)*(full_plots_odd + full_plots_even) + diamond_plots_odd
    nb_plots = (0 + 8*math.floor(quotient/2))*(math.floor((quotient + 2)/2))/2*full_plots_even
    nb_plots += (4 + 8*math.floor((quotient + 1)/2) - 4)*(math.floor((quotient + 1)/2))/2*full_plots_odd
    nb_plots += diamond_plots_odd
    print(int(nb_plots))

    # # plot --------------------------------------------
    # for i, line in enumerate(my_map):
    #     for j, char in enumerate(list(line)):
    #         if (i, j) in plots:
    #             print('O', end = '')
    #         else:
    #             print(char, end = '')
    #     print()
    # # --------------------------------------------------

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of garden plots the Elf could reach is: {int(nb_plots)}')

if __name__ == '__main__':
    main(sys.argv[1])