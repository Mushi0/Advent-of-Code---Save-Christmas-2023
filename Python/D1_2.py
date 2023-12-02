import sys
import re

words_to_num = {'one': 'o1ne', 
                'two': 't2wo', 
                'three': 't3hree', 
                'four': 'f4our', 
                'five': 'f5ive', 
                'six': 's6ix', 
                'seven': 's7even', 
                'eight': 'e8ight', 
                'nine': 'n9ine'}

def main(DATA_INPUT):
    total = 0
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            for key, value in words_to_num.items():
                my_str = my_str.replace(key, value)
            my_number_list = re.findall(r'\d', my_str)
            total += int(my_number_list[0] + my_number_list[-1])
            my_str = f.readline()
    print(total)

if __name__ == '__main__':
    main(sys.argv[1])