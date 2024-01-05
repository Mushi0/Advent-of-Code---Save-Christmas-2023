import sys
import time

SORT_ORDER = {'2': 0, 
            '3': 1, 
            '4': 2, 
            '5': 3, 
            '6': 4, 
            '7': 5, 
            '8': 6, 
            '9': 7, 
            'T': 8, 
            'J': 9, 
            'Q': 10, 
            'K': 11, 
            'A': 12}

LEN_HAND = 5

def new_sort(my_list):
    my_list.sort(key = lambda val: SORT_ORDER[val])

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        my_str = f.readline()
        
        hands = []
        while my_str:
            my_list = my_str.strip().split()
            my_list[1] = int(my_list[1])
            my_list = [list(my_list[0])] + my_list
            new_sort(my_list[0])
            index = 0
            numbers_of_repeat = []
            while index <= LEN_HAND - 1:
                number_of_repeat = 1
                while (index <= LEN_HAND - 2) and (my_list[0][index] == my_list[0][index + 1]):
                    number_of_repeat += 1
                    index += 1
                numbers_of_repeat.append(number_of_repeat)
                index += 1
            numbers_of_repeat.sort(reverse = True)
            my_list.append(tuple(numbers_of_repeat))
            
            if len(hands) == 0:
                hands += [my_list]
            else:
                found = False
                for i, hand in enumerate(hands):
                    if hand[3] == my_list[3]:
                        while (i < len(hands)) and (hands[i][3] == my_list[3]):
                            for j, letter in enumerate(my_list[1]):
                                if SORT_ORDER[letter] < SORT_ORDER[hands[i][1][j]]:
                                    break
                                elif SORT_ORDER[letter] > SORT_ORDER[hands[i][1][j]]:
                                    found = True
                                    break
                            if found:
                                break
                            i += 1
                        found = True
                        break
                    elif hand[3] < my_list[3]:
                        found = True
                        break
                if not found:
                    hands.append(my_list)
                else:
                    hands = hands[:i] + [my_list] + hands[i:]
            
            my_str = f.readline()
    
    total = 0
    for i, hand in enumerate(hands):
        total += (len(hands) - i) * hand[2]
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total winnings are: {total}')

if __name__ == '__main__':
    main(sys.argv[1])