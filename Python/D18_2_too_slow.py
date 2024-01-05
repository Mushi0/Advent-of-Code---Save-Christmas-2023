import sys
import time
import heapq
from tqdm import tqdm

dir_map = {'R': (0, 1), 
           'L': (0, -1), 
           'U': (-1, 0), 
           'D': (1, 0)}

dir_code = {'0': 'R',
            '1': 'D',
            '2': 'L',
            '3': 'U'}

def parse_input(color_str):
    step = int(color_str[2:7], 16)
    dir = dir_code[color_str[7]]
    return dir, step

def get_last_edge(coord, edges):
    last_edge = [0, 0]
    if (coord[0] - 1, coord[1]) in edges:
        last_edge[0] = 1 # from up
    if (coord[0] + 1, coord[1]) in edges:
        last_edge[1] = 1 # from down
    return last_edge

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        dig_plan = [line.split() for line in f.read().splitlines()]
    
    edge = []
    current_location = (0, 0)
    for [_, _, color_str] in dig_plan:
        dir, step = parse_input(color_str)
        for _ in range(int(step)):
            current_location = (current_location[0] + dir_map[dir][0],  
                                 current_location[1] + dir_map[dir][1])
            heapq.heappush(edge, current_location)
    
    min_x = min(coord[0] for coord in edge)
    max_x = max(coord[0] for coord in edge)
    pbar = tqdm(total = max_x - min_x + 1)
    
    lava_vol = 1
    new_location = heapq.heappop(edge)
    while edge:
        current_location = new_location
        current_line = current_location[0]
        new_location = heapq.heappop(edge)
        lava_vol += 1
        inside = False
        continues = False
        while edge and new_location[0] == current_line:
            if not continues:
                last_edge = get_last_edge(current_location, edge)
            if new_location[1] == current_location[1] + 1:
                continues = True
                lava_vol += 1
            else:
                current_edge = get_last_edge(current_location, edge)
                
                if ((not continues) or 
                    (last_edge != current_edge)):
                    inside = not inside

                if inside:
                    lava_vol += (new_location[1] - current_location[1])
                else:
                    lava_vol += 1
                continues = False
            
            current_location = new_location
            new_location = heapq.heappop(edge)
        
        pbar.update(1)
    pbar.close()

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'It could hold: {lava_vol} cubic meters of lava')

if __name__ == '__main__':
    main(sys.argv[1])