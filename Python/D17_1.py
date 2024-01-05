import sys
import time
import numpy as np
import heapq

DIRECTIONS = [[-1,0],[0,1],[1,0],[0,-1]]

def get_smallest_heatloss(heat_loss_map):
    m, n = heat_loss_map.shape
    
    Q = [(0, 0, 0, -1, 0)]
    visited = {}

    while Q:
        # min heaps always keep increasing order (heappush() does that)
        # so each time starts from the least heatloss node, 
        # and the least x, y, ... (heappop() does that)
        heatloss, x, y, dir, dir_repeat = heapq.heappop(Q)
        if (x, y, dir, dir_repeat) in visited:
            continue
        visited[(x, y, dir, dir_repeat)] = heatloss

        for i, (dx, dy) in enumerate(DIRECTIONS):
            new_x = x + dx
            new_y = y + dy
            new_dir = i
            new_dir_repeat = (1 if new_dir != dir else dir_repeat + 1)
        
            reverse = ((new_dir + 2)%4 == dir)

            valid = (new_dir_repeat <= 3)

            if 0 <= new_x < m and 0 <= new_y < n and not reverse and valid:
                new_heatloss = heatloss + heat_loss_map[new_x][new_y]
                if not (new_x, new_y, new_dir, new_dir_repeat) in visited:
                    heapq.heappush(Q, 
                        (new_heatloss, new_x, new_y, new_dir, new_dir_repeat))
    
    smallest_heatloss = np.inf
    for (x, y, dir, dir_repeat), heatloss in visited.items():
        if x == m - 1 and y == n - 1 and smallest_heatloss > heatloss:
            smallest_heatloss = heatloss
    
    return smallest_heatloss

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        heat_loss_map = np.array([list(map(int, list(row))) 
                                  for row in f.read().splitlines()])

    smallest_heat_loss = get_smallest_heatloss(heat_loss_map)

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The least heat loss it can incur is: {smallest_heat_loss}')

if __name__ == '__main__':
    main(sys.argv[1])