#!/usr/local/bin/python3
import collections 
import sys

import lib_poker as util 


def get_winer_same_combination(hand_1, hand_2, combination_type):
    '''Find the winner between two sets of cards of the same combination_type.
    ''' 
    
    all_cards_1 = util.order_cards_by_value([c for c in hand_1])
    all_cards_2 = util.order_cards_by_value([c for c in hand_2])
    
    winner = -1
    # both hands contain high cards
    if combination_type == 1: 
        winner = util.get_winner_in_high_card(all_cards_1, all_cards_2)
        #print_winner_message(winner)
        
    # both hands contain pair
    elif combination_type == 2:
        winner = util.get_winner_in_pairs(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain two pairs
    elif combination_type == 3:
        winner = util.get_winner_in_two_pairs(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain triples
    elif combination_type == 4:
        winner = util.get_winner_in_triples(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain full house
    elif combination_type == 5:
        winner = util.get_winner_in_full_house(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain four of a kind
    elif combination_type == 6:
        winner = util.get_winner_in_four_a_kind(all_cards_1, all_cards_2)
        #print_winner_message(winner)
    
    # either of the hands may contain invalid card as an input
    else:
        winner = -1

    return(winner)
        

def who_wins(hand_1, hand_2):
    ''' Determine the winner of the two hands 
     input: cards in the first hand and the second hand 
     -- determine combination type
     -- check the valuable combination
     -- in case of hard, check the higher card 
     '''
    
    if len(hand_1) != 5 or len(hand_2) != 5 or \
            not set(hand_1).issubset(util.CARD_SET) or \
            not set(hand_2).issubset(util.CARD_SET):
        return(-1)

    hand_1_type = util.check_card_combination_type(hand_1)
    hand_2_type = util.check_card_combination_type(hand_2)
    
    winner = -1
    
    # hands contain illegal combination of cards 
    if hand_1_type not in range(1,7) or hand_1_type not in range(1, 7):
        return(-1)

    # case 1: simple scenario - the hands contain different combination type. 
    if hand_1_type > hand_2_type:
        #print_winner_message(1)
        winner = 1
    elif hand_1_type < hand_2_type:
        #print_winner_message(2)
        winner = 2
    else: 
        # similar combination type
        winner = get_winer_same_combination(hand_1, hand_2, hand_1_type)    

    return(winner)


if __name__ == '__main__':
    '''Main function
    '''

    # check for user inputs
    if len(sys.argv) < 3:
        sys.exit('Please insert cards in hand_1 and hand_2')
    
    hand_1 = sys.argv[1].upper()
    hand_2 = sys.argv[2].upper()
       
    # Check if a hand contains five cards.
    if len(hand_1) != 5:
            sys.exit('The first hand must contain 5 cards. Please try again.')
    
    if len(hand_2) != 5:
        sys.exit('The second hand must contain 5 cards. Please try again.')
    
    #print('First hand: {} \nSecond hand: {}'.format(hand_1, hand_2))
    
    # Check if a hand contains invalid cards. 
    if  not set(hand_1).issubset(util.CARD_SET):
        sys.exit('The fist hand contain invalid cards')

    if  not set(hand_2).issubset(util.CARD_SET):
        sys.exit('The second hand contain invalid cards')

    winner = who_wins(hand_1, hand_2)

    util.print_winner_message(winner)


