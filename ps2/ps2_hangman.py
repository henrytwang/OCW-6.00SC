# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
import itertools

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word = choose_word(wordlist)
word_letter_list = list(word)
displayed_word = list(itertools.repeat("_", len(word)))
guess_count = 8
letters = list(string.ascii_lowercase)


def print_greeting():
    print "Welcome to the game!"
    print "I am thinking of a word that is %s letters long." % (len(word))
    print "The word is %s" % word
    print "---------"


def print_status():
    print "You have %s guesses left." % (guess_count)
    print "Available letters: " + "".join(letters)
    print "The word so far: %s" % ("".join(displayed_word))


def remove_found_letter(letter):
    letters.remove(letter)

print_greeting()
while guess_count > 0:
    print_status()
    letter = raw_input("Please type a letter: ")
    if letter in word_letter_list:
        print "Great guess!"
        letter_indices = [i for i, x in enumerate(word_letter_list) if x == letter]
        for index in letter_indices:
            displayed_word[index] = letter
        if "_" not in displayed_word:
            print "You win! :)"
            break
        remove_found_letter(letter)
    elif letter in letters:
        print "Sorry!"
        guess_count -= 1
        if guess_count == 0:
            print "You lost! :("
            break
        remove_found_letter(letter)
    else: 
        print "You already guessed that letter."

