#### Spelling Bee ####
import buzzWords as bw
import pangram
from random import choice
import time
from webster import *
from random import choice

pangrams = bw.startMenu()
pangram = choice(pangrams)  # chooses random pangram
scrambled_pangram = bw.randomizePangram(pangram)
possible_words = bw.findWords(scrambled_pangram, websterList)
percentiles = bw.percentile(possible_words)
print(f"Pangram is: {pangram}")
print(f"Possible words build from this pangram are: {possible_words}")
print(f"Percentile Categories are: f{percentiles}")

score = 0
expertise = "Beginner"
game_over = False
guess_words = []

while not game_over:
    print(f"'\nThe current pangram is: {scrambled_pangram}.") #STRING.split()
    word = input("What word would you like to guess?").upper()  #STRING
    if bw.validate(word, scrambled_pangram, guess_words, websterList):
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
