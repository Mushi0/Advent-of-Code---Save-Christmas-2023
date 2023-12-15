import sys
from tqdm import tqdm
import time

def check_if_match(record, contiguous_groups):
    i = 0
    counts = []
    while i < len(record):
        count = 0
        while i < len(record) and record[i] == '#':
            count += 1
            i += 1
        if count > 0:
            counts.append(count)
        i += 1
    return tuple(counts) == contiguous_groups

def count_matches(record, contiguous_groups):
    if record.count('#') > sum(contiguous_groups):
        return 0
    elif '?' in record:
        i = record.index('?')
        return (count_matches(record[:i] + '.' + record[i + 1:], contiguous_groups) + 
                count_matches(record[:i] + '#' + record[i + 1:], contiguous_groups))
    else:
        return check_if_match(record, tuple(contiguous_groups))

def main(DATA_INPUT):
    start_time = time.time()
    
    total = 0
    with open(DATA_INPUT) as f:
        pbar = tqdm(total = 1000)
        condition_record = f.readline()
        while condition_record:
            [record, contiguous_groups] = condition_record.split()
            contiguous_groups = contiguous_groups.split(',')
            contiguous_groups = [int(i) for i in contiguous_groups]

            total += count_matches(record, contiguous_groups)

            condition_record = f.readline()
            pbar.update(1)
        pbar.close()
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of those counts is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])