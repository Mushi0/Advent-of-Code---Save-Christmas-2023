import sys
import time

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT, 'r') as f:
        my_map = f.read().splitlines()

    start_pos = (0, 1)
    end_pos = (len(my_map) - 1, len(my_map[0]) - 2)

    # found out that all the forks have slopes at each path (coincidence? no)
    # can be used to track the direction and break the loop

    def walk(this_pos, visited):
        # while no fork in the road
        step_count = 1
        while sum([1 for dir in dirs if my_map[this_pos[0] + dir[0]][this_pos[1] + dir[1]] in '^v<>']) <= 2:
            step_count += 1
            have_valid_dir = False
            for dir in dirs:
                next_pos = (this_pos[0] + dir[0], this_pos[1] + dir[1])

                if next_pos == end_pos:
                    return [step_count]
                if (my_map[next_pos[0]][next_pos[1]] == '#' or 
                    next_pos in visited):
                    continue

                visited.add(next_pos)
                this_pos = next_pos
                have_valid_dir = True
                break
            
            if not have_valid_dir:
                return [0]

        # fork in the road
        nb_steps_list = []
        have_valid_dir = False
        for dir in dirs:
            next_pos = (this_pos[0] + dir[0], this_pos[1] + dir[1])

            if next_pos == end_pos:
                return [step_count]
            if (my_map[next_pos[0]][next_pos[1]] == '#' or 
                next_pos in visited):
                continue

            visited.add(next_pos)
            nb_steps_list += [step_count + x for x in walk(next_pos, visited.copy())]
            have_valid_dir = True
        
        if not have_valid_dir:
            return [0]
        
        return nb_steps_list
    
    nb_steps = max(walk(start_pos, {start_pos})) - 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The longest hike is: {nb_steps} steps long')

if __name__ == '__main__':
    main(sys.argv[1])