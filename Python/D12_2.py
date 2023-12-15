import sys
from tqdm import tqdm
from functools import lru_cache
import time

@lru_cache(maxsize = None)
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

def count_matches_one_seg(record, contiguous_groups):
    if record.count('#') > sum(contiguous_groups):
        return 0
    elif '?' in record:
        i = record.index('?')
        return (count_matches_one_seg(record[:i] + '.' + record[i + 1:], contiguous_groups) + 
                count_matches_one_seg(record[:i] + '#' + record[i + 1:], contiguous_groups))
    else:
        return check_if_match(record, tuple(contiguous_groups))

def count_matches(unknowns_or_damaged, contiguous_groups):
    if len(contiguous_groups) == 0:
        for r in unknowns_or_damaged:
            if '#' in r:
                return 0
        return 1
    if len(unknowns_or_damaged) == 1:
        return count_matches_one_seg(unknowns_or_damaged[0], contiguous_groups)
    
    len_first = len(unknowns_or_damaged[0])
    total = (count_matches_one_seg(unknowns_or_damaged[0], []) * 
            count_matches(unknowns_or_damaged[1:], contiguous_groups))
    k = 0
    count = 0
    while (k < len(contiguous_groups)) and (count <= len_first):
        count += contiguous_groups[k] + 1
        total += (count_matches_one_seg(unknowns_or_damaged[0], contiguous_groups[:k + 1]) * 
                  count_matches(unknowns_or_damaged[1:], contiguous_groups[k + 1:]))
        k += 1
    
    return total

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

            record = '?'.join([record] * 5)
            contiguous_groups = contiguous_groups * 5

            unknowns_or_damaged = record.split('.')
            unknowns_or_damaged = [r for r in unknowns_or_damaged if len(r) != 0]
            total += count_matches(unknowns_or_damaged, contiguous_groups)

            condition_record = f.readline()
            pbar.update(1)
        pbar.close()
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of those counts is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])