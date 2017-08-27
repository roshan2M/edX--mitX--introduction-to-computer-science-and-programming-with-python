import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter
        else:
            result += '_ '
    return result

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result += letter
    return result

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = ''
    guesses = 8
    
    print('Loading word list from file...')
    print('55900 words loaded.')
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    print('-------------')
    
    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print('You have ' + str(guesses) + ' guesses left')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        letter = raw_input('Please guess a letter: ')
        letter = letter.lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        elif (letter not in lettersGuessed) and (letter in secretWord):
            lettersGuessed += letter
            print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed += letter
            guesses -= 1
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
        print('-------------')
    
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')

hangman('else')






