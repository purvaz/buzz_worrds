import pygame
import random
import sys  # using sys to import python modules outside of client folder

sys.path.append("../server")  # importing pathway to server
import buzzWords as bw  # modules created by Kris.
import wordSets

# create game window
pygame.init()
screen = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("BuzzWords")
icon = pygame.image.load("../client/Media/Bee.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

pangrams = wordSets.filteredPangrams
pangram = random.choice(pangrams)  # chooses random pangram
scrambled_pangram = bw.randomizePangram(pangram)
possible_words = bw.findWords(scrambled_pangram, wordSets.totalSet, 60)
percentiles = bw.percentile(possible_words)

'''Remove next 5 lines after testing complete.
'''
print(f"Pangram is: {pangram}")
print(f"Shuffled pangram is {scrambled_pangram}")
print(f"Possible words build from this pangram are: {possible_words}")
print(f"Number of possible words is: {len(possible_words)}")
print(f"Percentile Categories are: f{percentiles}")

my_buzzwords = bw.createEmptyList(len(possible_words))  # reset list to empty to be fed from backend


# font setup
def font(font_size):
    defined_font = pygame.font.Font("../client/Font/LexendDeca-VariableFont_wght.ttf", font_size)
    return defined_font


def wrapping_centered_text(wordbubble_message, screen):
    # first, split the text into words
    words = wordbubble_message.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            wc_font = pygame.font.Font("../client/Font/LexendDeca-VariableFont_wght.ttf", 24)
            fw, fh = wc_font.size(' '.join(line_words + words[:1]))
            # max allowed width of rect =140
            if fw > 140:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # render the wrapped lines of text
    # render each line below the last, so need to keep track of
    # cumulative height of the lines rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = wc_font.size(line)
        # text_x = orig x + halfway across bubble
        text_x = 1060
        text_y = 145
        tx = text_x - fw / 2
        ty = text_y + y_offset
        font_surface = wc_font.render(line, True, "Black")
        screen.blit(font_surface, (tx, ty))
        y_offset += fh
    pygame.display.flip()


# scoring
score = 0  # initial score
guessed_words = []
expertise = "Beginner"  # initial expertise level.
score_font = font(60)
score_string = str(score)
if score >= 100:
    score_location = (93, 580)
elif 10 <= score < 100:
    score_location = (103, 580)
else:
    score_location = (113, 580)

# guessing
guess_font = font(75)
max_guess_length = 13
guess_input = ''
# note to self: pygame.Rect(x,y,w,h)
guess_box = pygame.Rect(335, 665, 625, 70)
guess_box_color = (238, 238, 238)

# bee word bubble
wordbubble_font = font(24)
# note to self: pygame.Rect(x,y,w,h)
wordbubble_box = pygame.Rect(992, 145, 140, 90)
wordbubble_box_color = (255, 255, 255)
message = ""
instructions_prompt = "Need instructions? Click on me."

# My BuzzWords list
mbw_box = pygame.Rect(100, 100, 485, 285)
mbw_box_color = (238, 238, 238)
mbw_font = pygame.font.Font("../client/Font/LexendDeca-VariableFont_wght.ttf", 16)

# surfaces
background = pygame.image.load("../client/Media/Buzzwords_background.jpg")
scaled_background = pygame.transform.scale(background, (1440, 810))
score_text = score_font.render(score_string, True, 'Black')
wordbubble_text = wordbubble_font.render(message, True, 'Black')

# initially place bee
bee_x = 1100
bee_y = 200


# rotate bee
def rotate_bee(angle):
    global bee_250
    global bee_x
    global bee_y
    rotated_image = pygame.transform.rotate(bee_250, angle)
    return rotated_image


# resize & angle bee images
bee = pygame.image.load("../client/Media/Bee.png")
default_bee_size = (250, 178)
bee_250 = pygame.transform.scale(bee, default_bee_size)
resting_angle = 15
starting_bee = rotate_bee(resting_angle)
wordbubble_bee = pygame.image.load("../client/Media/wordbubble bee.png")
wordbubble_bee_250 = pygame.transform.scale(wordbubble_bee, (396, 279))
# wordbubble_bee_location = (bee_x-135.65,bee_y-71.85)
wbx = 964.35
wby = 128.15
wordbubble_bee_location = (wbx, wby)


def my_buzzwords_list_displayed():
    mbw_y = 103
    mbw_length = len(my_buzzwords)
    if mbw_length < 0:
        wordbubble_pop_up(instructions_prompt)
        # 2000 = 2 sec wait
        pygame.time.delay(2000)
    elif 0 < mbw_length <= 14:
        for i in range(0, mbw_length):
            mbw_x = 100
            mbw = mbw_font.render(my_buzzwords[i], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
    elif 15 <= mbw_length <= 29:
        for i in range(0, 15):
            mbw_x = 100
            mbw = mbw_font.render(my_buzzwords[i], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
        for j in range(15, mbw_length):
            mbw_x = 221.25
            mbw = mbw_font.render(my_buzzwords[j], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
    elif 30 <= mbw_length <= 44:
        for i in range(0, 15):
            mbw_x = 100
            mbw = mbw_font.render(my_buzzwords[i], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
        for j in range(15, 30):
            mbw_x = 221.25
            mbw = mbw_font.render(my_buzzwords[j], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
        for k in range(30, mbw_length):
            mbw_x = 342.5
            mbw = mbw_font.render(my_buzzwords[k], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
    elif 45 <= mbw_length <= 60:
        for i in range(0, 15):
            mbw_x = 100
            mbw = mbw_font.render(my_buzzwords[i], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
        for j in range(15, 30):
            mbw_x = 221.25
            mbw = mbw_font.render(my_buzzwords[j], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
        for k in range(30, 45):
            mbw_x = 342.5
            mbw = mbw_font.render(my_buzzwords[k], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18
        mbw_y = 103
        for m in range(45, mbw_length):
            mbw_x = 463.75
            mbw = mbw_font.render(my_buzzwords[m], True, "Black")
            screen.blit(mbw, (mbw_x, mbw_y))
            mbw_y += 18


def correct_answer():
    for i in range(resting_angle, (360 + resting_angle)):
        screen.blit(scaled_background, (0, 0))
        screen.blit(score_text, score_location)
        screen.blit(rotate_bee(i), (bee_x, bee_y))
        pygame.time.delay(10)
        pygame.display.flip()
    praise = ["Wow!",
              "Great!",
              "Well done!",
              "I knew you could do it!",
              "I’m proud of you!",
              "Looking good!",
              "You’re on top of it!",
              "Now you’re flying!",
              "You’re catching on!",
              "Good job!",
              "Dynamite!",
              "Nothing can stop you now!",
              "Spectacular!",
              "You’ve figured it out!",
              "Bingo!",
              "Terrific!",
              "You’re sensational!",
              "Super job!",
              "Awesome!",
              "I’m proud of you!",
              "Amazing!",
              "Way to go!",
              "Outstanding!",
              "Good!",
              "Remarkable!",
              "Superstar!",
              "Bravo!",
              "Hooray for you!",
              "That’s incredible!",
              "Remarkable job!",
              "Great discovery!",
              "Magnificent!",
              "Super work!",
              "Super!",
              "Excellent!",
              "Neat!",
              "Fantastic!",
              "Nice work!",
              "Hip hip hooray!",
              "Marvelous!",
              "Phenomenal!",
              "That's creative!"]
    praise_length = len(praise) - 1
    chosen_index = int(random.randint(0, praise_length))
    selected_praise = praise[chosen_index]
    return selected_praise


def wrong_answer(message="That's not in my list. Try again!"):
    global bee_x
    global bee_y
    for j in range(4):
        for i in range(1090, 1110, 10):
            buzz_x = i
            buzz_y = bee_y
            screen.blit(scaled_background, (0, 0))
            screen.blit(score_text, score_location)
            screen.blit(starting_bee, (buzz_x, buzz_y))
            pygame.time.delay(12)
            pygame.display.flip()
    wordbubble_pop_up(message)
    # 1500 = 1.5 sec wait
    pygame.time.wait(1500)
    pygame.display.flip()


def wordbubble_pop_up(wordbubble_message):
    screen.blit(scaled_background, (0, 0))
    screen.blit(score_text, score_location)
    screen.blit(wordbubble_bee_250, wordbubble_bee_location)
    wrapping_centered_text(wordbubble_message, screen)
    pygame.display.flip()


running = True
while running:
    screen.blit(scaled_background, (0, 0))
    screen.blit(starting_bee, (bee_x, bee_y))
    screen.blit(score_text, score_location)
    my_buzzwords_list_displayed()

    # event checking loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # quit when pressing escape
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if event.key == pygame.K_ESCAPE:
                guess_input = ""
            elif event.key == pygame.K_RETURN:
                '''
                Adding code from back end here
                '''
                if bw.validate(guess_input.upper(), scrambled_pangram, guessed_words, wordSets.totalSet):
                    guessed_words.append(guess_input.upper())
                    print(f"guessed words are: {guessed_words}")
                    selected_praise = correct_answer()
                    wordbubble_pop_up(selected_praise)
                    pygame.time.delay(2000)
                    index = len(guessed_words) - 1
                    my_buzzwords[index] = f"{my_buzzwords[index]} {guess_input.upper()}"
                    increase = bw.score(guess_input.upper())
                    # insert message about score increase?
                    # Jessica, updated score needs to be on screen.
                    score += increase
                    print(f"Score is {score}")
                    # message about expertise status?
                    expertise = bw.expertise(percentiles, score)

                else:

                    if len(guess_input) < 4:
                        wrong_answer("Word must be at least 4 letters long.")

                    elif guess_input.upper() in guessed_words:
                        wrong_answer("You already guessed that word")

                    elif guess_input.upper() not in wordSets.totalSet:
                        wrong_answer("That is not a word in my Word List.")

                    elif scrambled_pangram[0].upper() not in guess_input.upper():
                        wrong_answer(f'You did not use the required letter "{scrambled_pangram[0]}"!')

                    # checks if the guessed word uses only the letters in the pangram.
                    else:
                        for i in range(1, len(guess_input)):
                            letter = guess_input[i]
                            if letter not in scrambled_pangram:
                                wrong_answer(f'"{letter}" is not a possible letter choice!')

                guess_input = ""
                '''
                End adding code
                '''
                # Jess' Code
                # selected_praise = correct_answer()
                # wordbubble_pop_up(selected_praise)
                # # 2000 = 2 sec wait
                # pygame.time.delay(2000)
                # my_buzzwords.append(guess_input)
                # guess_input = ""

            elif event.key == pygame.K_TAB:
                wordbubble_pop_up(instructions_prompt)
                # 2000 = 2 sec wait
                pygame.time.delay(2000)
                guess_input = ""
            elif event.key == pygame.K_SPACE:
                wrong_answer()
                guess_input = ""
            elif event.key == pygame.K_BACKSPACE:
                guess_input = guess_input[:-1]
            else:
                if len(guess_input) < max_guess_length:
                    guess_input += event.unicode

        display_guess = guess_font.render(guess_input, True, 'Black')
        screen.blit(display_guess, (guess_box.x + 10, guess_box.y + 10))
        guess_box.w = max(100, display_guess.get_width() + 10)

        # always have at the end
        pygame.display.flip()
        clock.tick(60)
