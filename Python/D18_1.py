import sys
import time
import heapq

dir_map = {'R': (0, 1), 
           'L': (0, -1), 
           'U': (-1, 0), 
           'D': (1, 0)}

def get_last_edge(coord, edges):
    last_edge = [0, 0]
    if (coord[0] - 1, coord[1]) in edges:
        last_edge[0] = 1
    if (coord[0] + 1, coord[1]) in edges:
        last_edge[1] = 1
    return last_edge

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        dig_plan = [line.split() for line in f.read().splitlines()]
    
    edge = []
    current_location = (0, 0)
    for [dir, step, _] in dig_plan:
        for _ in range(int(step)):
            current_location = (current_location[0] + dir_map[dir][0],  
                                 current_location[1] + dir_map[dir][1])
            heapq.heappush(edge, current_location)
    
    # min_x = min(coord[0] for coord in edge)
    # max_x = max(coord[0] for coord in edge)
    # min_y = min(coord[1] for coord in edge)
    # max_y = max(coord[1] for coord in edge)
    # my_map = [['.' for _ in range(min_y, max_y + 1)] for _ in range(min_x, max_x + 1)]
    
    lava_vol = 1
    new_location = heapq.heappop(edge)
    while edge:
        current_location = new_location
        current_line = current_location[0]
        new_location = heapq.heappop(edge)
        lava_vol += 1
        # my_map[current_location[0] - min_x][current_location[1] - min_y] = '#'
        inside = False
        continues = False
        while edge and new_location[0] == current_line:
            if not continues:
                last_edge = get_last_edge(current_location, edge)
            if new_location[1] == current_location[1] + 1:
                continues = True
                lava_vol += 1
                # my_map[new_location[0] - min_x][new_location[1] - min_y] = '#'
            else:
                current_edge = get_last_edge(current_location, edge)
                
                if ((not continues) or 
                    (last_edge != current_edge)):
                    inside = not inside

                if inside:
                    lava_vol += (new_location[1] - current_location[1])
                    # for i in range(current_location[1] + 1, new_location[1] + 1):
                    #     my_map[current_location[0] - min_x][i - min_y] = '#'
                else:
                    lava_vol += 1
                    # my_map[new_location[0] - min_x][new_location[1] - min_y] = '#'
                continues = False
            
            current_location = new_location
            new_location = heapq.heappop(edge)
    
    # my_map[new_location[0] - min_x][new_location[1] - min_y] = '#'
            
    # with open('map.txt', 'w') as f:
    #     for line in my_map:
    #         f.write(''.join(line) + '\n')
    # # lava_vol = sum(sum(1 for c in line if c == '#') for line in my_map)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'It could hold: {lava_vol} cubic meters of lava')

if __name__ == '__main__':
    main(sys.argv[1])