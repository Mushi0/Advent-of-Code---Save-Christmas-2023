import sys
import time

def main(DATA_INPUT):
    start_time = time.time()
    
    winnings = []
    with open(DATA_INPUT) as f:
        my_str = f.readline()
        while my_str:
            [_, winningnb_and_card] = my_str.split(':')
            [winningnb, card] = winningnb_and_card.split('|')
            winningnb = winningnb.split()
            card = card.split()
            winnings.append(sum(number in winningnb for number in card))
            my_str = f.readline()
    nb_cards = [1]*len(winnings)
    for i in range(len(winnings)):
        nb_cards[i + 1: i + winnings[i] + 1] = map(lambda x: x + nb_cards[i], 
                                                nb_cards[i + 1: i + winnings[i] + 1])
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total number of scratchcards you end up with is: {sum(nb_cards)}')

if __name__ == '__main__':
    main(sys.argv[1])