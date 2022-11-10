
#### Pre-process of data ####

def txt_to_list(txt_file, size=None):
    ''' txt_file, a string representing the pathway and name of a text file
    returns a list of words based on the text file, assuming a line break
    between words.
    example: The text file below

    Bob  123
    Sue 234
    Charlie  456

    returns ['BOB', 'SUE', 'CHARLIE']'''

    file = open(txt_file, "r")  # returns a file object, stores in file.
    # traverses by
    word_list = []
    # traverses with newline as break-off character
    count = 0
    for line in file:
        word = line.split()[0]
        word = word.upper()
        word_list.append(word)
        count += 1
        if count == size:
            break
    file.close()
    return word_list

def txt_to_set(txt_file):
    ''' txt_file, a string representing the pathway and name of a text file
    returns a set of words based on the text file, assuming a line break
    between words.
    example: The text file below

    Bob  123
    Sue 234
    Charlie  456

    returns {'BOB', 'SUE', 'CHARLIE'}'''
    return set(line.strip().upper() for line in open(txt_file, "r"))

def createWebster(dictionary):
    ##########
    # Unused #
    ##########
    '''Takes a dict representing webter's dictionary,  returns list of all words without definitions.'''
    output = open("webster.txt", "w")
    for word in dictionary:
        if "-" not in word and " " not in word:
            output.write(word + "\n")
    output.close()


def filter(word_seq, min=4, max=13):
    """takes in a sequence of strings and integers min and max representing range of desired lengths.Removes Swear words.

    returns set with only words of desired lengths
    standard is 4 and 13 as that is the spelling bee parameter"""
    from better_profanity import profanity
    filtered_list = []
    for word in word_seq:
        # removes words that contain "s"
        if "S" not in word:
            # adds the word if it is the correct length
            # boolean to check if profanity
            profane = profanity.contains_profanity(word)
            if not profane and (len(word) in range(min, max + 1)):
                filtered_list.append(word)

    return set(filtered_list)


def intersection(short_list, long_list):
    ##########
    # Unused #
    ##########
    '''Returns the sorted, unique values that are in both of the lists.'''
    from numpy import array, intersect1d
    short = array(short_list)
    long = array(long_list)
    return intersect1d(short, long).tolist()



def isPangram(word, length=7):
    '''Takes any word, determines if it is a pangram (and hence can be used in spelling bee
        Pangram def: word that uses only 7 distinct characters'''
    repeats = 0
    letter_freq = {}
    for letter in word:
        if letter in letter_freq:
            letter_freq[letter] += 1
            repeats += 1
        else:
            letter_freq[letter] = 1
    if len(word) - repeats == length:
        return True
    return False

def createPangram(seq):
    return set(word for word in seq if isPangram(word))

#### End of methods used to pre-process data



def randomizePangram(pangram):
    """Returns the letters of given pangram in randomized order"""
    from random import shuffle
    letter_list = []
    # this loop ensures no letters are duplicated
    for letter in pangram:
        if letter not in letter_list:
            letter_list.append(letter)
    shuffle(letter_list)
    return "".join(letter_list)  # joins list into string


def print_pangram(pangram):
    string = f'''
        {pangram[1]}
{pangram[2]}                {pangram[3]} 
        {pangram[0]} 
{pangram[4]}                {pangram[5]} 
        {pangram[6]}   
'''
    print(string)

def findWords(pangram, word_list):
    '''
    :param pangram: buzzWord's current pangram
    :param word_list: list of all English words (e.g. webster's dictionary)
    :return: all possible words that can be made with that pangram
    Assumes that the first letter given is the required letter
    returns a list of all possible words'''
    possible_words = []
    for word in word_list:
        if pangram[0] in word:  # checks for required letter
            goodWord = True
            for letter in word:
                if letter not in pangram:
                    goodWord = False
                    break
            if goodWord:
                possible_words.append(word)
    return set(possible_words)

def validate(potential_word, pangram, guessed_words, wordList):
    '''
    :param potential_word: represents a potential word to be guess
    :param pangram: word being currently used in the game
    :param wordList: list of all words (e.g. Webster's dictionary)
    :return: boolean. True if valid word, False other wise.
    '''

    if len(potential_word) < 4:
        print("Word must be at least 4 letters long.")
        return False
    elif potential_word not in wordList:
        print("That is not a word in my Word List.")
        return False
    elif potential_word in guessed_words:
        print("You've already guessed that word.")
        return False
    elif pangram[0] not in potential_word:
        print(f'You did not use the required letter "{pangram[0]}"!')
        return False
    # checks if the guessed word uses only the letters in the pangram.
    for letter in potential_word:
        if letter not in pangram:
            print(f'"{letter}" is not a possible letter choice!')
            return False

    return True

def score(valid_word):
    if len(valid_word) == 4:
        return 1
    elif isPangram(valid_word):
        return len(valid_word) + 7
    return len(valid_word)


def percentile(valid_words):
    '''creates a dictionary that maps point value to expertise category.'''
    # calculates total points possible
    total_points = 0
    for word in valid_words:
        total_points += score(word)
    # ordinal_rank = (Percentile/100) x NumberValues
    percentile_list = [0, 2, 5, 8, 15, 25, 40, 50, 70, 100]
    expertise_categories = ["Beginner", "Good Start", "Moving Up", "Good", "Solid",
                            "Nice", "Great", "Amazing", "Genius", "Queen Bee"]
    d = {}
    for i in range(len(percentile_list)):
        p = percentile_list[i]
        point_percentile = round(p / 100 * total_points)
        d[point_percentile] = expertise_categories[i]
    return d

def expertise(percentiles, score):
    p_list = []
    for percentile in percentiles:
        if percentile == score:
            return percentile
        p_list.append(percentile)

    for i in range(len(p_list)):
        if score < p_list[i]:
            return percentiles[p_list[i-1]]

def startMenu():
    '''startMenu asks the users to choose the size of the words from which the game
    words are created. Returns a list of pangrams (words created with 7 unique letters)
    based on this user input.'''
    import pangram

    question = """Creating a list of game words from the most commonly used words in the English language.
    How large of a word pool would you like?
     1)  1,000 words
     2)  2,000 words
     3)  3,000 words
     4)  5,000 words
     5) 10,000 words
     6) 25,000 words
     7) 50,000 words
     8) 111,111 words
     9) 222,222 words
    10 333,333 words
    >>> """

    '''Inside pangrams.py  >>>
    pangrams = {1: pangrams1, 2: pangrams2, 3: pangrams3, 
                4: pangrams5, 5: pangrams10, 6: pangrams25, 
                7: pangrams50, 8: pangrams111, 9: pangrams222, 
                10:pangrams333}'''

    valid = False
    while not valid:
        try:
            num_words = int(input(question))
            if 1 <= num_words <= 10:
                valid = True
        except ValueError:
            print("Please Enter a choice from above.")

    return pangram.pangrams[num_words]
