from ps4a import *
import time

#
# Problem #6: Computer chooses a word
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maximum = 0
    
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    
    # For each word in the wordList
    for word in wordList:
        
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            
            # Find out how much making that word is worth
            wordValue = getWordScore(word, n)
            
            # If the score for that word is higher than your best score
            if wordValue > maximum:
                
                # Update your best score, and best word accordingly
                maximum = wordValue
                bestWord = word

    # Return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score.
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        
        # Display the hand.
        print "Current Hand:",
        displayHand(hand)
        
        # Ask computer for input.
        word = compChooseWord(hand, wordList, n)
        
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop).
            break
            
        # Otherwise (the input is not None):
        else:                
            # Tell the computer how many points the word earned, and the updated total score, in one line followed by a blank line.
            scoreTemp = getWordScore(word, n)
            score += scoreTemp
            print('"' + str(word) + '"' + " earned " + str(scoreTemp) + " points. Total: " + str(score))
            print
            
            # Update the hand.
            hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score.
    if word == None:
        print("Total score: " + str(score))
    elif calculateHandlen(hand) == 0:
        print("Total score: " + str(score))
    
#
# Problem #8: Playing a game
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # Creates a variable hand to verify that a hand variable has been made.
    hand = {}
    
    # This code runs until e is entered - the program is exited.
    while True:
        
        # Gets the response from the user and checks it through if statements.
        response1 = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
        # If the user entered n, it means that a new game must be created and played through.
        if response1 == "n":
            
            # Gets the response from the user and checks it through if statements.
            response2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
            hand = dealHand(HAND_SIZE)
            
            # If the user entered u, it means that the user will play.
            if response2 == "u":
                playHand(hand, wordList, HAND_SIZE)
            
            # If the user entered c, it means that the computer will play.
            elif response2 == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
            
            # If the user entered any other letter, then it is an invalid input.
            else:
                print "Invalid command."
        
        # If the user entered r, it means that the previous hand will be played, only if a hand was played before.
        elif response1 == "r":
            
            # This checks if the hand has already been created.
            if hand:
                
                # Gets the response from the user and checks it through if statements.
                response2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                
                # If the user entered u, it means that the user will play.
                if response2 == "u":
                    playHand(hand, wordList, HAND_SIZE)
            
                # If the user entered c, it means that the computer will play.
                elif response2 == "c":
                    compPlayHand(hand, wordList, HAND_SIZE)
                
                # If the user entered any other letter, then it is an invalid input.
                else:
                    print "Invalid command."
            
            # If the hand has not been created and filled yet, it tells the user to first play a hand.
            else:
                print "You have not played a hand yet. Please play a new hand first!"
        
        # If the user entered e, it means that the program will be exited.
        elif response1 == "e":
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


