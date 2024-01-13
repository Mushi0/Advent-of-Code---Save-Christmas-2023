import sys
import time

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()

    start_pos = (0, 1)
    end_pos = (len(my_map) - 1, len(my_map[0]) - 2)

    def walk(this_pos, visited):        
        nb_steps_list = []
        for dir in dirs:
            next_pos = (this_pos[0] + dir[0], this_pos[1] + dir[1])
            if next_pos == end_pos:
                return [1]
            if next_pos in visited:
                continue
            if ((dir == (0, 1) and my_map[next_pos[0]][next_pos[1]] in '<^v') or 
                (dir == (1, 0) and my_map[next_pos[0]][next_pos[1]] in '^<>') or 
                (dir == (0, -1) and my_map[next_pos[0]][next_pos[1]] in '>^v') or 
                (dir == (-1, 0) and my_map[next_pos[0]][next_pos[1]] in 'v<>')):
                continue
            if my_map[next_pos[0]][next_pos[1]] == '#':
                continue
            visited.add(next_pos)
            nb_steps_list += [1 + x for x in walk(next_pos, visited.copy())]
        
        return nb_steps_list
    
    nb_steps = max(walk(start_pos, {start_pos}))
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The longest hike is: {nb_steps} steps long')

if __name__ == '__main__':
    main(sys.argv[1])