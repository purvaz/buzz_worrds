import pygame
import csv
import sys

letter_string = "MBDELNO"
Words_list = ['Embolden', 'Emboldened', 'Bellmen', 'Bloom', 'Bloomed', 'Bomb', 'Bombe', 'Bombed', 'Boom', 'Boomed',
              'Deem', 'Deemed', 'Demo', 'Demoed', 'Demon', 'Dome', 'Domed', 'Doom', 'Doomed', 'Embed', 'Embedded',
              'Emblem', 'Emend', 'Emended', 'Lemon', 'Loom', 'Loomed', 'Meddle', 'Meddled', 'Meld', 'Melded', 'Melee',
              'Melon', 'Meme', 'Memo', 'Mend', 'Mended', 'Mobbed', 'Mode', 'Model', 'Modeled',
              'Modem', 'Mold', 'Molded', 'Mole', 'Moll', 'Mondo', 'Mono', 'Mood', 'Mooed', 'Moon', 'Mooned', 'Noblemen',
              'Omen']

#import lists of differences for bee dance
bee_dance_x_change = []
with open('beeDanceXchange.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar="'", skipinitialspace=True)
    for difference in reader:
        bee_dance_x_change.append(difference)

bee_dance_y_change = []
with open('beeDanceYchange.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar="'", skipinitialspace=True)
    for difference in reader:
        bee_dance_y_change.append(difference)

# create game window
pygame.init()
screen = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("BuzzWords")
icon = pygame.image.load("../client/Media/Bee.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# font setup
def font(font_size):
    font = pygame.font.Font("../client/Font/LexendDeca-VariableFont_wght.ttf",font_size)
    return font

#scoring
score_font = font(60)
score = 15 # will later be fed from backend
score_string = str(score)
if score >= 100:
    score_location = (95,580)
elif score >= 10 and score <100:
    score_location = (103,580)
elif score <10:
    score_location = (110,580)
#guessing
guess_font = font(75)
max_guess_length = 13
guess_input = ''
#guess_location_x = 335
#guess_location_y = 680
#guess_location = (guess_location_x,guess_location_y)
    ## note to self: pygame.Rect(x,y,w,h)
guess_box = pygame.Rect(335,677,625,95)
guess_box_color = (238,238,238)

#surfaces
background = pygame.image.load("../client/Media/Buzzwords_background.jpg")
scaled_background = pygame.transform.scale(background, (1440, 810))
score_text = score_font.render(score_string, True, 'Black')
#display_guess = guess_font.render(guess_input, True, 'Black')

# initially place bee
bee_x = 1100
bee_y = 200

# rotate bee
def rotate_bee (angle):
    global bee_250
    global bee_x
    global bee_y
    rotated_image = pygame.transform.rotate(bee_250, angle)
    return rotated_image

# resize & angle bee
bee = pygame.image.load("../client/Media/Bee.png")
default_bee_size = (250, 200)
bee_250 = pygame.transform.scale(bee, default_bee_size)
starting_bee = rotate_bee(45)

running = True
while running:
    screen.blit(scaled_background, (0, 0))
    screen.blit(starting_bee, (bee_x, bee_y))
    screen.blit(score_text, score_location)


    #event checking loop
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
            elif event.key == pygame.K_BACKSPACE:
                guess_input = guess_input[:-1]
            else:
                if len(guess_input) < max_guess_length:
                    guess_input += event.unicode

        pygame.draw.rect(screen,guess_box_color, guess_box)
        display_guess = guess_font.render(guess_input, True, 'Black')
        screen.blit(display_guess, (guess_box.x + 10, guess_box.y + 10))
        guess_box.w = max(100, display_guess.get_width() + 10)

        # always have at the end
        pygame.display.flip()
        clock.tick(60)
