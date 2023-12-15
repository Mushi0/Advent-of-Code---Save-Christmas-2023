import sys
from tqdm import tqdm
import re
from functools import lru_cache
import time

def check_if_match(record, contiguous_group):
    return (record.count('#' * contiguous_group) == 1)

def count_matches_one_seg(record, contiguous_group):
    if record.count('#') > contiguous_group:
        return 0
    elif '?' in record:
        i = record.index('?')
        return (count_matches_one_seg(record[:i] + '.' + record[i + 1:], contiguous_group) + 
                count_matches_one_seg(record[:i] + '#' + record[i + 1:], contiguous_group))
    else:
        return check_if_match(record, contiguous_group)

@lru_cache(maxsize = None)
def count_matches(record, contiguous_groups):
    len_record = len(record)
    first_group = contiguous_groups[0]
    total = 0
    if len(contiguous_groups) == 1:
        return count_matches_one_seg(record, contiguous_groups[0])
    for i in range(len_record - contiguous_groups[0] - 1):
        if '#' in record[:i]:
            break
        if ((not '.' in record[i:i + first_group]) and 
        ((i == 0) or (not record[i - 1] == '#')) and 
        ((i == len_record - 1) or (not record[i + first_group] == '#'))):
            total += count_matches(record[i + first_group + 1:], contiguous_groups[1:])
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

            record = re.sub('\.\.+', '.', record)
            total += count_matches(record, tuple(contiguous_groups))

            condition_record = f.readline()
            pbar.update(1)
        pbar.close()
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of those counts is: {total}')

if __name__ == '__main__':
    main(sys.argv[1])