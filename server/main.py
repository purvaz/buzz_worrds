#### Spelling Bee ####
import buzzWords as bw
import wordSets
from random import choice

'''
This code was used to pre-process data.
It created these sets of strings:
1) smallSet  - high school english vocab. No slang, swears, nothing larger than 6 words
2) extendedSet - has words longer than 6.
3) totalSet - intersection of 1) and 2)
4) filteredPangrams - takes out words smaller than 4 or larger than 13, any words with "S" in them.

smallSet = bw.txt_to_set("small.txt") # set of high school vocabulary
overflowSet = bw.txt_to_set("overflow.txt") # includes words longer than 6 and adverbs, plurals, etc.
totalSet = smallSet | overflowSet # combination of both sets. 25,153 words
print(totalSet)
filteredSet = bw.filter(totalSet) #12,041 words
print(filteredSet)
print(len(totalSet), len(filteredSet))
pangram = bw.createPangram(filteredSet)

'''

'''
will be used to test frequency of word length later. 
'''
# d = {}
# for word in totalSet:
#     if len(word) not in d:
#         d[len(word)] = 1
#     else:
#         d[len(word)] += 1
#
# print(d)

pangrams = wordSets.filteredPangrams
pangram = choice(pangrams)  # chooses random pangram
scrambled_pangram = bw.randomizePangram(pangram)
possible_words = bw.findWords(scrambled_pangram, wordSets.totalSet)
percentiles = bw.percentile(possible_words)
print(f"Pangram is: {pangram}")
print(f"Possible words build from this pangram are: {possible_words}")
print(f"Percentile Categories are: f{percentiles}")

score = 0
expertise = "Beginner"
game_over = False
guess_words = []

while not game_over:
    # print(f"'\nThe current pangram is: {scrambled_pangram}.") #STRING.split()
    bw.print_pangram(scrambled_pangram)
    word = input("What word would you like to guess?").upper()  #STRING
    if bw.validate(word, scrambled_pangram, guess_words, wordSets.totalSet):
        guess_words.append(word)
        increase = bw.score(word)
        print(f"\nNice! Your score increased by {increase} points!") #INT
        score += increase
        print(f"Your Score is: {score}") #INT

        expertise = bw.expertise(percentiles, score)
        print(f"Current Expertise: {expertise}") #STRING

        print("\nGuessed Words:")
        for word in guess_words: #TRAVERSES LIST OF STRINGS
            print(word)
