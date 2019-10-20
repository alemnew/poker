#!/usr/local/bin/python3
import collections 
import sys


CARD_SET = list('23456789TJQKA')

CARD_VALUE = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 
        'J':11, 'Q':12, 'K':13, 'A':14}

WINNER_MSG = {0: 'It\'s a tie!',
              1: 'First hand wins!',
              2: 'Second hand wins!',
              -1: 'Game Error'
             }

def character_frequency(the_string):
    # Count the frequency of characters in a string.
    
    frequency = {}
    for i in set(the_string):
        frequency[i] = the_string.count(i)
    
    return frequency 

def get_keys_by_value(dictionary, value_to_find):
    # Find key(s) in a dictionary for a given value
    
    list_of_keys = list()
    list_of_items = dictionary.items()
    for item  in list_of_items:
        if item[1] == value_to_find:
            list_of_keys.append(item[0])
        
    return(list_of_keys)

def print_winner_message(winner):
    ''' Prints winner message. 
    input: winner
    '''
    # print('{}: {}'.format(winner, WINNER_MSG[winner]))
    print(WINNER_MSG[winner])


def remove_all_from_list(the_list, e_list):
    ''' Remove all occurrence of an element from a list. 
    input: the list and the list of elements to remove.
    return: the list that does not have e_list removed.
    '''
    for e in e_list:
        while e in the_list:
            the_list.remove(e)

    return(the_list)


def get_repeated_card(cards, count):
    ''' Find the repeated card from the list of cards.
    input: the list of cards and the number of counts that show the repetition
    return: a list contain a card count times
    '''
    cards_with_repetition = collections.defaultdict(int)
    for c in cards:
        cards_with_repetition[c] += 1
    
    # get the value that has a count number of repetitions. 
    card_repeated_count_times = get_keys_by_value(cards_with_repetition, count)
    
    return(card_repeated_count_times)
    

def is_four_of_a_kind(hand):
    ''' Check if a given cards combination in a hand is four of a kind '''

    all_cards = [f for f in hand]

    # create a unique set of cards
    unique_cards = set(all_cards)

    # if there are more than 2 unique cards, it's not four of a kind
    return(True if len(unique_cards) == 2 and \
            all(all_cards.count(f) == 4 or all_cards.count(f) == 1 \
                for f in unique_cards) else False)


def is_full_house(hand):
    ''' Check if a given cards combination in a hand is a full house '''

    # all_cards = [f for f in hand]

    return(True if len(set(hand)) == 2 and  \
        all(values > 1 for values in list(character_frequency(hand).values())) 
        else False)


def is_triples(hand):
    ''' Check if a given cards combination in a hand is triples '''

    all_cards = [f for f in hand]
    unique_cards = set(all_cards)

    # if len(unique_cards) == 3:
    #     for c in unique_cards:
    #         if all_cards.count(c) == 3:
    #             return(True)
    # return(False)

    return(True if (len(unique_cards) == 3) and \
        all(values != 2 for values in list(character_frequency(hand).values())) 
              else False)


def is_two_pairs(hand):
    ''' Check if a given cards combination in a hand is a two-pairs''' 

    all_cards = [f for f in hand]
    unique_cards = set(all_cards)

    return(True if len(unique_cards) == 3 and \
                  all(all_cards.count(c) < 3 for c in unique_cards) else False)


def is_pair(hand):
    ''' Check if a given cards combination in a hand is a pair'''
    
    return(True if len(set(hand)) == 4 else False)

def is_high_card(hand):
    ''' Check if a given cards combination in a hand is a high-card '''

    return(True if len(set(hand)) == 5 else False)

def check_card_combination_type(hand):
    '''Checks the cards combination type within a hand.
     input: a combination of cards that a hand contains. 
     return values: 
        1: high cards
        2: pair 
        3: two pairs
        4: triples 
        5: full house
        6: four of a kind 
        -1: not a possible card combination 
     '''
    
    if is_four_of_a_kind(hand):
        #print('{} is four of a kind'.format(hand))
        return(6)
    elif is_full_house(hand):
        #print('{} is a full house'.format(hand))
        return(5)
    elif is_triples(hand):
        #print('{} is a triples'.format(hand))
        return(4)
    elif is_two_pairs(hand):
        #print('{} is two pairs'.format(hand))
        return(3)
    elif is_pair(hand):
        #print('{} is pair'.format(hand))
        return(2)
    elif is_high_card(hand):
        #print('High card'.format(hand))
        return(1)
    else: 
        return(-1)

def get_valuable_card(cards):
    ''' Get the most valuable card in a card set
     input: list of cards
     return: a card
     '''
    
    all_cards = [c for c in cards]
    valuable_card = ''
    for card in set(all_cards):
        if not valuable_card: 
            valuable_card = card
        elif CARD_VALUE[card] >= CARD_VALUE[valuable_card]:
            valuable_card = card

    return(valuable_card)

def order_cards_by_value(cards):
    ''' Order a set of cards by value in descending order. 
    input: list of cards
    return: list of ordered cards (high to low)
    '''
 
    all_cards = [c for c in cards]
    ordered_cards = []

    while all_cards:
        valuable_card = get_valuable_card(all_cards)
        ordered_cards.append(valuable_card)
        all_cards.remove(valuable_card)

    return(ordered_cards)

def get_winner_in_high_card(all_cards_1, all_cards_2):
    ''' Find the winner from high card combination.
    input: lists of high to low ordered cards
    return: the winner player.
        0: it is a tie
        1: first hand wins 
        2: second hand wins
        -1: fail
    '''
    
    enum_cards_1 = dict(enumerate(all_cards_1))
    enum_cards_2 = dict(enumerate(all_cards_2))
    
    winner = -1 # set a no winning case 
    for k in enum_cards_1.keys():
        if CARD_VALUE[enum_cards_1[k]] == CARD_VALUE[enum_cards_2[k]]:
            winner = 0
        elif CARD_VALUE[enum_cards_1[k]] > CARD_VALUE[enum_cards_2[k]]:
            return(1)
        elif CARD_VALUE[enum_cards_1[k]] < CARD_VALUE[enum_cards_2[k]]:
            return(2)

    return(winner)

def get_winner_in_pairs(all_cards_1, all_cards_2):
    ''' Find the winner from a pairs combination.
    input: lists of cards
    return: the winner player.
        0: it is a tie
        1: first hand wins 
        2: second hand wins
        -1: fail
    '''
    
    hand_1_pair = get_repeated_card(all_cards_1, 2)[0]
    hand_2_pair = get_repeated_card(all_cards_2, 2)[0]
    
    if CARD_VALUE[hand_1_pair] > CARD_VALUE[hand_2_pair]:
        return(1)
    elif CARD_VALUE[hand_1_pair] < CARD_VALUE[hand_2_pair]:
        return(2)
    else:
        # remove the pairs and consider the remaining cards as a high card combination 
        cards_1_pair_remv = remove_all_from_list(all_cards_1, [hand_1_pair])
        cards_2_pair_remv = remove_all_from_list(all_cards_2, [hand_2_pair])

        winner = get_winner_in_high_card(cards_1_pair_remv, cards_2_pair_remv)
    
        return(winner)


def get_winner_in_two_pairs(all_cards_1, all_cards_2):
    ''' Find the winner in a two pairs combination
    '''

    hand_1_pairs = get_repeated_card(all_cards_1, 2)
    hand_2_pairs = get_repeated_card(all_cards_2, 2)
    
    # order the pairs cards in ascending order
    hand_1_pairs_ordered = order_cards_by_value(hand_1_pairs)
    hand_2_pairs_ordered = order_cards_by_value(hand_2_pairs)
    
    # Compare the two pairs at each hand 
    for card in hand_1_pairs_ordered:
        if card in hand_2_pairs_ordered:
            continue
        elif CARD_VALUE[card] > CARD_VALUE[hand_2_pairs_ordered[0]]:
            return(1)
        elif CARD_VALUE[card] < CARD_VALUE[hand_2_pairs_ordered[0]]:
            return(2)


    # remove the two pairs and consider the remaining card at each hand 
    # as a high card combination 
    cards_1_pairs_remv = remove_all_from_list(all_cards_1, hand_1_pairs)
    cards_2_pairs_remv = remove_all_from_list(all_cards_2, hand_2_pairs)
    
    # TO DO: can be doable with simple card value comparison. 
    winner = get_winner_in_high_card(cards_1_pairs_remv, cards_2_pairs_remv)
    return(winner)


def get_winner_in_triples(all_cards_1, all_cards_2):
    ''' Find the winner in a triples combination
    '''
    
    hand_1_triples = get_repeated_card(all_cards_1, 3)
    hand_2_triples = get_repeated_card(all_cards_2, 3)
    
    # compare the triples first
    if CARD_VALUE[hand_1_triples[0]] > CARD_VALUE[hand_2_triples[0]]:
        return(1)
    elif CARD_VALUE[hand_1_triples[0]] < CARD_VALUE[hand_2_triples[0]]:
        return(2)
    else:
        # remove the triples and consider the remaining card as a high card 
        # combination 
        cards_1_triples_remv = remove_all_from_list(all_cards_1, hand_1_triples)
        cards_2_triples_remv = remove_all_from_list(all_cards_2, hand_2_triples)
        
        winner = get_winner_in_high_card(cards_1_triples_remv, cards_2_triples_remv)
        return(winner)

def get_winner_in_full_house(all_cards_1, all_cards_2):
    ''' Find the winner in a full house  combination
    '''
    
    hand_1_triples = get_repeated_card(all_cards_1, 3)
    hand_2_triples = get_repeated_card(all_cards_2, 3)

    hand_1_pairs = get_repeated_card(all_cards_1, 2)
    hand_2_pairs = get_repeated_card(all_cards_2, 2)
    
    # first compare the triples
    if CARD_VALUE[hand_1_triples[0]] > CARD_VALUE[hand_2_triples[0]]:
        return(1)
    elif CARD_VALUE[hand_1_triples[0]] < CARD_VALUE[hand_2_triples[0]]:
        return(2)

    # second compare the pairs if the triples are similar 
    if CARD_VALUE[hand_1_pairs[0]] > CARD_VALUE[hand_2_pairs[0]]:
        return(1)
    elif CARD_VALUE[hand_1_pairs[0]] < CARD_VALUE[hand_2_pairs[0]]:
        return(2)
    else:
        return(0)

    return(-1)

def get_winner_in_four_a_kind(all_cards_1, all_cards_2):
    ''' Find the winner in a four of a kind combination
    '''
    
    hand_1_fours = get_repeated_card(all_cards_1, 4)
    hand_2_fours = get_repeated_card(all_cards_2, 4)
    
    # first compare the repeated four cards at each hand
    if CARD_VALUE[hand_1_fours[0]] > CARD_VALUE[hand_2_fours[0]]:
        return(1)
    elif CARD_VALUE[hand_1_fours[0]] < CARD_VALUE[hand_2_fours[0]]:
        return(2)

    # second compare the single card at each hand 
    cards_1_fours_remv = remove_all_from_list(all_cards_1, hand_1_fours)
    cards_2_fours_remv = remove_all_from_list(all_cards_2, hand_2_fours)
    
    if CARD_VALUE[hand_1_fours_remv[0]] > CARD_VALUE[hand_2_fours_remv[0]]:
        return(1)
    elif CARD_VALUE[hand_1_fours_remv[0]] < CARD_VALUE[hand_2_fours_remv[0]]:
        return(2)
    else:
        return(0)
    
    return(-1)


def get_winer_same_combination(hand_1, hand_2, combination_type):
    '''Find the winner 
    ''' 
    
    all_cards_1 = order_cards_by_value([c for c in hand_1])
    all_cards_2 = order_cards_by_value([c for c in hand_2])
    
    winner = -1
    # both hands contain high cards
    if combination_type == 1: 
        winner = get_winner_in_high_card(all_cards_1, all_cards_2)
        #print_winner_message(winner)
        
    # both hands contain pair
    elif combination_type == 2:
        winner = get_winner_in_pairs(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain two pairs
    elif combination_type == 3:
        winner = get_winner_in_two_pairs(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain triples
    elif combination_type == 4:
        winner = get_winner_in_triples(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain full house
    elif combination_type == 5:
        winner = get_winner_in_full_house(all_cards_1, all_cards_2)
        #print_winner_message(winner)

    # both hands contain four of a kind
    elif combination_type == 6:
        winner = get_winner_in_four_a_kind(all_cards_1, all_cards_2)
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
            not set(hand_1).issubset(CARD_SET) or \
            not set(hand_2).issubset(CARD_SET):
        return(-1)

    hand_1_type = check_card_combination_type(hand_1)
    hand_2_type = check_card_combination_type(hand_2)
    
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
    if  not set(hand_1).issubset(CARD_SET):
        sys.exit('The fist hand contain invalid cards')

    if  not set(hand_2).issubset(CARD_SET):
        sys.exit('The second hand contain invalid cards')

    winner = who_wins(hand_1, hand_2)

    print_winner_message(winner)


