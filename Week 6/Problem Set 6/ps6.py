import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def decrypt_story():
    """
    Returns: the joke in decrypted plaintext.
    """
    # Obtains the message and creates a CiphertextMessage object.
    message = CiphertextMessage(get_story_string())
    
    # Decrypts the message using the method in the CiphertextMessage class.
    return message.decrypt_message()

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Creates a dictionary that maps each letter via a shift.
        cipher = {}
        
        # These strings contains the lowercase and uppercase letters.
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        
        '''
        For each letter in lowercase, the letter is mapped in the dictionary
        to the index of the letter plus the shift modulo 26, which means that
        if the shift brings the index over 26, then modulo 26 will start it
        from the beginning of the lowercase string.
        '''
        for letter in lowercase:
            cipher[letter] = lowercase[(lowercase.index(letter) + shift) % 26]
        
        '''
        For each letter in uppercase, the letter is mapped in the dictionary
        to the index of the letter plus the shift modulo 26. This is neat
        because if the resulting index is greater than 26, then modulo 26 will
        find the remainder and start searching through the list again.
        '''
        for letter in uppercase:
            cipher[letter] = uppercase[(uppercase.index(letter) + shift) % 26]
        
        # Returns the dictionary containing the cipher.
        return cipher

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # Creates a new ciphertext to build the message in.
        cipher_text = ''
        
        # Creates a cipher using the shift given by the user.
        cipher_dict = self.build_shift_dict(shift)
        
        # For each character, the following checks occur.
        for char in self.message_text:
            # If the character is in the cipher, then it is replaced by a
            # different of the character in the cipher dictionary.
            if char in cipher_dict:
                cipher_text += cipher_dict[char]
            # If it is not in the cipher, then it is simply added to the
            # ciphertext.
            else:
                cipher_text += char
        
        # Returns the ciphertext.
        return cipher_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        # Initializes all attributes from the Message initialization.
        Message.__init__(self, text)
        
        # Initializes the shift attribute.
        self.shift = shift
        
        # Initializes the encryption dictionary of cipher attribute.
        self.encrypting_dict = self.build_shift_dict(shift)
        
        # Initializes the encrypted message attribute.
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        # Returns the shift in letters that was entered.
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        # Returns a copy of the cipher dictionary.
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        # Returns the encrypted message text.
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # Updates the shift variable to the new shift that was entered.
        self.shift = shift
        
        # Updates the encryption dictionary to a new dictionary created from
        # the updated shift.
        self.encrypting_dict = self.build_shift_dict(shift)
        
        # Updates the message by using the new cipher to encrypt the message.
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # Initializes all attributes from the Message initialization. 
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Variable to count the number of correct words in the message.
        count = 0
        
        # Variable to store the maximum number of correct words in any message.
        max_count = 0
        
        # Variable to store the best shift value.
        best_shift = None
        
        # Goes through every value from 0 - 25 to apply a shift.
        for shift in range(26):
            # Applies a shift on the message to obtained the (hopefully)
            # plaintext message.
            new_message = self.apply_shift(shift)
            
            # For every word in the message, it checks if it is a word.
            for word in new_message.split():
                # If the word is an actual word, then count is incremented by 1.
                if is_word(WORDLIST_FILENAME, word) == True:
                    count += 1
            
            # To end, if count is greater than max_count, then both max_count
            # and best_shift are updated to the current best cipher.
            if count > max_count:
                max_count = count
                best_shift = shift
        
        # Returns a tuple containing the best_shift and the encrypted message
        # that the best_shift would apply on the encrypted message to obtain
        # the plaintext message.
        return (best_shift, self.apply_shift(best_shift))
            

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print 'Expected Output:', (24, 'hello')
print 'Actual Output:', ciphertext.decrypt_message()