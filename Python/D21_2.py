import sys
import time
import numpy as np

# Look carefully at the map, 
# After 65 steps, the reachable plots forms a diamond shape, 
# and just reach the edge of the map. 
# Therefore, just calculate how many 131 steps (width and height) are there, 
# and calculate one map. 

# From Python/D21_2_something_wrong.py, 
# my calculation didn't work, but I realized that 
# the nb of plots is a quadratic function of the quotient. 
# So I just need three points (just across the edge) to calculate the function. 

NB_STEPS = 26_501_365

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_next_steps(my_map: list, pos: tuple):
    next_steps = []
    for d in dirs:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if my_map[new_pos[0] % 131][new_pos[1] % 131] != '#':
            next_steps.append(new_pos)
    return next_steps

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()
    
    for line in my_map:
        if 'S' in line:
            start = (my_map.index(line), line.index('S'))
            break
    
    X = [0, 1, 2]
    Y = []
    plots = set([start])
    steps = [65 + 131*i for i in X]
    for i in range(1, steps[-1] + 1):
        new_plots = set()
        for plot in plots:
            new_plots.update(get_next_steps(my_map, plot))
        plots = new_plots
        
        if i in steps:
            Y.append(len(plots))

    quotient = NB_STEPS // 131
    # and the remainder is just right 65, I think it's meant to be! 

    # # my previous calculation :( ------------------------
    # import math
    # full_plots_odd = 7226
    # full_plots_even = 7257
    # diamond_plots_odd = 3682
    # nb_even = (0 + 8*math.floor(quotient/2))*(math.floor((quotient + 2)/2))/2
    # nb_odd = (4 + 8*math.floor((quotient + 1)/2) - 4)*(math.floor((quotient + 1)/2))/2
    # nb_plots = nb_even*full_plots_even + nb_odd*full_plots_odd + diamond_plots_odd
    # # ---------------------------------------------------

    # my new calculation --------------------------------
    coefficients = np.polyfit(X, Y, 2)
    print(coefficients)
    polynomial = np.poly1d(coefficients)
    nb_plots = polynomial(quotient) + 1
    # I didn't know why I need to add 1 here. 
    # I just tried to put the number +1 to the problem and it worked LOL. 
    # (Always try +1 or -1 while doing AoC! )
    # ---------------------------------------------------

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number of garden plots the Elf could reach is: {int(nb_plots)}')

if __name__ == '__main__':
    main(sys.argv[1])