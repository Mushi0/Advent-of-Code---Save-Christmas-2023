import sys
import time

MULTIPLE = 17
TOTAL_CODE = 256

def hash_func(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= MULTIPLE
        current_value %= TOTAL_CODE
    return current_value

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        strings = f.readline().strip().split(',')

    boxes = [{} for _ in range(TOTAL_CODE)]
    total = 0    
    for string in strings:
        if '-' in string:
            label = string[:-1]
            box_id = hash_func(label)
            if label in boxes[box_id].keys():
                del boxes[box_id][label]
        elif '=' in string:
            [label, focal_len] = string.split('=')
            box_id = hash_func(label)
            boxes[box_id][label] = int(focal_len)
    
    for i, box in enumerate(boxes):
        counter = 1
        for _, value in box.items():
            total += (i + 1)*counter*value
            counter += 1

    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The focusing power of the resulting lens configuration is: {int(total)}')

if __name__ == '__main__':
    main(sys.argv[1])