#!/usr/bin/env python3
# encoding: utf-8

"""A simplified version of poker game. The program assumes that the cards 
don't have suits and there are no flushes, straights, and straight flushes.
"""

# Copyright (c) 2019 Alemnew Sheferaw Asrese 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import collections 
import sys

import lib_poker as util 


def get_winer_same_combination(hand_1, hand_2, combination_type):
    '''Determine the winner between two sets of cards of the 
    same combination_type.
    return: the winner player.
        0: it is a tie
        1: first hand wins 
        2: second hand wins
        -1: fail
    ''' 
    
    all_cards_1 = util.order_cards_by_value([c for c in hand_1])
    all_cards_2 = util.order_cards_by_value([c for c in hand_2])
    
    winner = -1
    if combination_type == 1:   
        # both hands contain high cards
        winner = util.get_winner_in_high_card(all_cards_1, all_cards_2)
    elif combination_type == 2:
        # both hands contain pair
        winner = util.get_winner_in_pairs(all_cards_1, all_cards_2)
    elif combination_type == 3:
        # both hands contain two pairs
        winner = util.get_winner_in_two_pairs(all_cards_1, all_cards_2)
    elif combination_type == 4:
        # both hands contain triples
        winner = util.get_winner_in_triples(all_cards_1, all_cards_2)
    elif combination_type == 5:
        # both hands contain full house
        winner = util.get_winner_in_full_house(all_cards_1, all_cards_2)
    elif combination_type == 6:
        # both hands contain four of a kind
        winner = util.get_winner_in_four_a_kind(all_cards_1, all_cards_2)  
    else:
        # either of the hands may contain invalid card as an input
        winner = -1

    return(winner)
        

def who_wins(hand_1, hand_2):
    ''' Determine the winner of the two poker hands 
     input: cards in the first hand and the second hand 
     return: the winner player.
        0: it is a tie
        1: first hand wins 
        2: second hand wins
        -1: fail
     '''
    
    # if any of the poker hand does not contain 5 cards, 
    # or illegal characters, retrun error. 
    if len(hand_1) != 5 or len(hand_2) != 5 or \
            not set(hand_1).issubset(util.CARD_SET) or \
            not set(hand_2).issubset(util.CARD_SET):
        return(-1)

    hand_1_type = util.check_card_combination_type(hand_1)
    hand_2_type = util.check_card_combination_type(hand_2)
    
    winner = -1
    
    if hand_1_type > hand_2_type:
        # simple scenario - the hands contain different combination type. 
        winner = 1
    elif hand_1_type < hand_2_type:
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


