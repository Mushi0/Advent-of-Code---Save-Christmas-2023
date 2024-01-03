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
            
            # horizontal fix
            for i in range(len(map) - 1):
                if sum(sum(1 for a, b in zip(map[i - j], map[i + 1 + j]) if a != b) 
                       for j in range(min(i, len(map) - i - 2) + 1)) == 0:
                    total += (i + 1)*100
                    break

            # vertical fix
            for i in range(len(map[0]) - 1):
                if sum(sum(1 for a, b in zip(row[i - j], row[i + 1 + j]) if a != b) 
                       for row in map 
                       for j in range(min(i, len(map[0]) - i - 2) + 1)) == 0:
                    total += (i + 1)
                    break

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The number I got from my notes is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])