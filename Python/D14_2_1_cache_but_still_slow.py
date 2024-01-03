import sys
import time
from tqdm import tqdm
from functools import lru_cache

NB_CYCLES = 1000000000
# NB_CYCLES = 3

def transpose_map(my_map: tuple) -> tuple:
    return tuple([tuple(row)[::-1] for row in zip(*my_map)])

@lru_cache(maxsize = None)
def roll(my_map: tuple) -> tuple:
    for line_index, line in enumerate(my_map):
        rolling_rocks = 0
        for i, c in enumerate(line):
            if c == 'O':
                rolling_rocks += 1
                new_line = my_map[line_index][:i] + ('.',) + my_map[line_index][i + 1:]
                my_map = my_map[:line_index] + (new_line,) + my_map[line_index + 1:]
            elif c == '#':
                for j in range(rolling_rocks):
                    new_line = my_map[line_index][:i - j - 1] + ('O',) + my_map[line_index][i - j:]
                    my_map = my_map[:line_index] + (new_line,) + my_map[line_index + 1:]
                rolling_rocks = 0
        
        if rolling_rocks:
            for j in range(rolling_rocks):
                new_line = my_map[line_index][:i - j] + ('O',) + my_map[line_index][i - j + 1:]
                my_map = my_map[:line_index] + (new_line,) + my_map[line_index + 1:]
    
    return my_map

def main(DATA_INPUT):
    start_time = time.time()

    total_load = 0
    my_map = []
    with open(DATA_INPUT) as f:
        my_map = [line.strip() for line in f]
    my_map = tuple(tuple(row) for row in my_map)
    
    for _ in tqdm(range(NB_CYCLES*4)):
        my_map = transpose_map(my_map)
        my_map = roll(my_map)

    # plot-----------------------------------------------
    for line in my_map:
        print("".join(line))
    # end plot-------------------------------------------
    
    my_map = transpose_map(my_map)
    for line in my_map:
        total_load += sum((i + 1) for i, c in enumerate(line) if c == 'O')

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total load on the north support beams is: {int(total_load)}')

if __name__ == '__main__':
    main(sys.argv[1])