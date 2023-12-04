import sys
import re

def main(DATA_INPUT):
    total = 0
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            [_, winningnb_and_card] = my_str.split(':')
            [winningnb, card] = winningnb_and_card.split('|')
            winningnb = winningnb.split()
            card = card.split()
            nb_of_winning = sum(number in winningnb for number in card)
            if not nb_of_winning == 0:
                total += pow(2, nb_of_winning - 1)
            my_str = f.readline()
    print(total)

if __name__ == '__main__':
    main(sys.argv[1])