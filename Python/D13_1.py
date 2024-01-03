import sys
import time

def main(DATA_INPUT):
    start_time = time.time()
    
    total = 0
    with open(DATA_INPUT) as f:
        line = f.readline()
        while line:
            map = []
            while line and line != '\n':
                map.append(line.strip())
                line = f.readline()
            
            line = f.readline()
            
            # horizontal
            for i in range(len(map) - 1):
                if map[i] == map[i + 1]:
                    j = 1
                    mirror = True
                    while i - j >= 0 and i + 1 + j < len(map):
                        if map[i - j] != map[i + 1 + j]:
                            mirror = False
                            break
                        j += 1
                    
                    if mirror:
                        total += (i + 1)*100
                        break
            
            # vertical
            for i in range(len(map[0]) - 1):
                if all(row[i] == row[i + 1] for row in map):
                    j = 1
                    mirror = True
                    while i - j >= 0 and i + 1 + j < len(map[0]):
                        if any(row[i - j] != row[i + 1 + j] for row in map):
                            mirror = False
                            break
                        j += 1
                    
                    if mirror:
                        total += (i + 1)
                        break

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number I got from my notes is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])