import sys
import time

NB_CYCLES = 1000000000
# NB_CYCLES = 3

def get_key(my_dict, val):
    for key, value in my_dict.items():
        if value == val:
            return key

def transpose_map(my_map: list) -> list:
    return [list(row)[::-1] for row in zip(*my_map)]

def roll(my_map: list) -> list:
    for line_index, line in enumerate(my_map):
        rolling_rocks = 0
        for i, c in enumerate(line):
            if c == 'O':
                rolling_rocks += 1
                my_map[line_index][i] = '.'
            elif c == '#':
                for j in range(rolling_rocks):
                    my_map[line_index][i - j - 1] = 'O'
                rolling_rocks = 0
        
        if rolling_rocks:
            for j in range(rolling_rocks):
                my_map[line_index][i - j] = 'O'
    
    return my_map

def main(DATA_INPUT):
    start_time = time.time()

    total_load = 0
    my_map = []
    with open(DATA_INPUT) as f:
        for line in f:
            my_map.append(line.strip())
    
    map_cycles = {0: my_map}
    cycle = 0
    for _ in range(NB_CYCLES):
        for _ in range(4):
            my_map = transpose_map(my_map)
            my_map = roll(my_map)
        cycle += 1
        if my_map in map_cycles.values():
            break
        map_cycles[cycle] = my_map
    
    cycle_point = get_key(map_cycles, my_map)
    id = (NB_CYCLES - cycle_point) % (cycle - cycle_point) + cycle_point
    my_map = map_cycles[id]

    # plot-----------------------------------------------
    for line in my_map:
        print("".join(line))
    # end plot-------------------------------------------
    
    my_map = transpose_map(my_map)
    for line in my_map:
        total_load += sum((i + 1) for i, c in enumerate(line) if c == 'O')

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total load on the north support beams is: {total_load}')

if __name__ == '__main__':
    main(sys.argv[1])