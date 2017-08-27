# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "D:\School\Online Courses\edX\MIT 6.00.1x\Week 4\Problem Set 4\ProblemSet4\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # Initializes value of result.
    result = 0
    
    # For each letter in word, it searches the letter in the dictionary and adds its value to result.
    for i in range(len(word)):
        result += SCRABBLE_LETTER_VALUES[word[i]]
    
    # It multiplies the score by the length of the word.
    result *= len(word)
    
    # If the word is the size of the hand (n), then the score gets an additional boost.
    if len(word) == n:
        result += 50
    
    # Returns the result.
    return result

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Makes a copy of the original hand of letters.
    newHand = hand.copy()
    
    # For every letter in word, the value of that letter in the newHand reduces by 1.
    for letter in word:
        newHand[letter] -= 1
    
    # It returns the updated hand, with the updated amounts of each letter.
    return newHand

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Creates a temporary version of the hand to mutate internally in the environment.
    handTemp = hand.copy()
    
    # If the word does not exist in the wordList, then it is not a valid word.
    if word not in wordList:
        return False
    
    # This for loop goes through each letter in the word and checks if the letter is in the hand.
    for letter in word:
        
        # If the letter is in the hand, it reduces the associated value by 1.
        if letter in handTemp:
            handTemp[letter] -= 1
            
            # If the new value associated with that letter is less than 0, then it returns False to indicate not enough of that letter.
            if handTemp[letter] < 0:
                return False
        
        # If the letter is not in the hand, it returns False.
        else:
            return False
    
    # If all conditions are passed, then True is returned.
    return True

#
# Problem #4: Playing a hand
#
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # Initializes the hand length at 0.
    length = 0
    
    # For each of the letters in hand, it adds the associated value to length.
    for value in hand.values():
        length += value
    
    # It returns the total number of letters in the hand.
    return length

#
# Problem #4: Playing a hand
#
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score.
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand.
        print "Current Hand: ",
        for letter in hand.keys():
            for i in range(hand[letter]):
                print str(letter) + " ",
        print
        # Ask user for input.
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop).
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line).
                print("Invalid word, please try again.")
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line.
                scoreTemp = getWordScore(word, len(hand))
                score += scoreTemp
                print('"' + str(word) + '"' + " earned " + str(scoreTemp) + " points. Total: " + str(score))
                print
                # Update the hand.
                hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score.
    if word == ".":
        print("Goodbye! Total score: " + str(score))
    elif calculateHandlen(hand) == 0:
        print("Run out of letters. Total score: " + str(score))

#
# Problem #5: Playing a game
# 
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # Creates a variable hand to verify that a hand variable has been made.
    hand = {}
    
    # This code runs until e is entered - the program is exited.
    while True:
        
        # Gets the response from the user and checks it through if statements.
        response = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        # If the user entered n, it means that a new game must be created and played through.
        if response == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        
        # If the user entered r, it means that the previous hand will be played, only if a hand was played before.
        elif response == "r":
            
            # This checks if the hand has already been created.
            if hand:
                playHand(hand, wordList, HAND_SIZE)
            
            # If the hand has not been created and filled yet, it tells the user to first play a hand.
            else:
                print "You have not played a hand yet. Please play a new hand first!"
        
        # If the user entered e, it means that the program will be exited.
        elif response == "e":
            break
        
        # If the user entered any other letter, then it is an invalid input.
        else:
            print "Invalid command."
   
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
