from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
    This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    best_word = None
    best_word_score = 0
    for word_size in range(1, len(hand) + 1):
        permutations = get_perms(hand, word_size)
        for possible_word in permutations:
            word_is_valid = is_valid_word(possible_word, hand, word_list)
            word_score = get_word_score(possible_word, len(possible_word))
            if word_is_valid and word_score > best_word_score:
                best_word = possible_word
                best_word_score = word_score
    return best_word


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    score = 0
    display_hand(hand)
    chosen_word = comp_choose_word(hand, word_list)
    print "chosen word is ", chosen_word
    score += get_word_score(chosen_word, len(hand))
    while chosen_word:
        hand = update_hand(hand, chosen_word)
        display_hand(hand)
        chosen_word = comp_choose_word(hand, word_list)
        print "chosen word is ", chosen_word
    print "The computer's score is ", score
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    hand = {}
    backup = {}
    while True:
        first_choice = raw_input("Input 'n' for a random hand, 'r' to replay your last hand, or 'e' to exit.")
        if first_choice is 'e':
            exit()
        second_choice = raw_input("Input 'u' to play as yourself or 'c' to let the computer play.")
        if first_choice is 'n':
            hand = deal_hand(7)
            backup = deepcopy(hand)
            if second_choice is 'u':
                play_hand(hand, word_list)
            elif second_choice is 'c':
                comp_play_hand(hand, word_list)
        elif first_choice is 'r':
            if second_choice is 'u':
                play_hand(deepcopy(backup), word_list)
            elif second_choice is 'c':
                comp_play_hand(deepcopy(backup), word_list)
        else:
            continue


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    # play_game(word_list)
    play_game(word_list)

