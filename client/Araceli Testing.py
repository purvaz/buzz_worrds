
# This is the homepage
import pygame
import random
import time



# initialize pygame
pygame.init()


clicking = False

isPlay_button = False

isHelp_button = False

isShuffle_button = False

# Change the title, logo
pygame.display.set_caption("BuzzWords")

#create the screen
screen = pygame.display.set_mode((1440,810))

# Image.png 32 x 32 pixel size
icon = pygame.image.load('../client/Media/Bee.png').convert_alpha()
pygame.display.set_icon(icon)

# create a shuffle image (<a href="https://www.flaticon.com/free-icons/random" title="random icons">Random icons created by Uniconlabs - Flaticon</a>)
shuffle = pygame.image.load('../client/Media/shuffle.png').convert_alpha()
shuffleRect = shuffle.get_rect(topleft = (1150, 650))


# create the bee for the help message (<a href="https://www.flaticon.com/free-icons/bee" title="bee icons">Bee icons created by Rohim - Flaticon</a>)
bee = pygame.image.load('../client/Media/help_bee.png').convert_alpha()
beeRect = bee.get_rect(topleft = (300, 500))

# create help message
help_bee = pygame.image.load('../client/Media/help_bee.png').convert_alpha()
help_button = help_bee.get_rect(topleft = (1200, 300))

# create the play button
black = (0, 0, 0)
yellow = (253, 218, 13)
white = (255, 255, 255)
lilac = (190, 170, 210)

font =  pygame.font.Font('../client/Font/LexendDeca-VariableFont_wght.ttf', 75)
play = font.render('Play', True, black, yellow)
playRect = play.get_rect(topleft = (1225, 150))



# create a background
background = pygame.image.load("../client/Media/Buzzwords_background.jpg").convert_alpha()
background_rect = background.get_rect(topleft = (0, 50))

def home_screen():
    scaled_bee = pygame.transform.scale(help_bee, (200, 175))
    scaled_background = pygame.transform.scale(background, (1440, 810))
    screen.blit(scaled_background, (0, 0))
    screen.blit(scaled_bee, help_button)
    screen.blit(play, playRect)


test_letter_list = ['F', 'A', 'T', 'I', 'G', 'U', 'E'] # just used to test the code

def start(letter_list):
    random.shuffle(letter_list)
    display_letters(letter_list)
    print(letter_list)



def play_screen():
    global clicking, isPlay_button, isHelp_button, isShuffle_button
    scaled_background = pygame.transform.scale(background, (1440, 810))
    screen.blit(scaled_background, (0, 0))
    screen.blit(shuffle, shuffleRect)
    #clicking = False


    if clicking and isPlay_button:
        start(test_letter_list)
        isPlay_button = False
        clicking = False
        isShuffle_button = False



def display_letters(letter_list):
    pos1 = (900, 290)
    letter1 = letter_list[0]
    pos2 = (900, 155)
    letter2 = letter_list[1]
    pos3 = (1020, 223)
    letter3 = letter_list[2]
    pos4 = (1020, 358)
    letter4 = letter_list[3]
    pos5 = (900, 425)
    letter5 = letter_list[4]
    pos6 = (780, 223)
    letter6 = letter_list[5]
    pos7 = (780, 358)
    letter7 = letter_list[6]

    first_letter = font.render(letter1, True, black, yellow)
    letter1_Rect = first_letter.get_rect(center=(pos1))
    second_letter = font.render(letter2, True, black, lilac)
    letter2_Rect = second_letter.get_rect(center=(pos2))
    third_letter = font.render(letter3, True, black, lilac)
    letter3_Rect = third_letter.get_rect(center=(pos3))
    fourth_letter = font.render(letter4, True, black, lilac)
    letter4_Rect = fourth_letter.get_rect(center=(pos4))
    fifth_letter = font.render(letter5, True, black, lilac)
    letter5_Rect = fifth_letter.get_rect(center=(pos5))
    sixth_letter = font.render(letter6, True, black, lilac)
    letter6_Rect = sixth_letter.get_rect(center=(pos6))
    seventh_letter = font.render(letter7, True, black, lilac)
    letter7_Rect = seventh_letter.get_rect(center=(pos7))

    screen.blit(first_letter, letter1_Rect)
    screen.blit(second_letter, letter2_Rect)
    screen.blit(third_letter, letter3_Rect)
    screen.blit(fourth_letter, letter4_Rect)
    screen.blit(fifth_letter, letter5_Rect)
    screen.blit(sixth_letter, letter6_Rect)
    screen.blit(seventh_letter, letter7_Rect)
    pygame.display.flip()
    #time.sleep(10)


def help_screen():
    font = pygame.font.Font('../client/Font/LexendDeca-VariableFont_wght.ttf', 20)
    display_surface = pygame.display.set_mode((1440, 810))
    scaled_background = pygame.transform.scale(background, (1440, 810))
    screen.blit(scaled_background, (0, 0))
    screen.blit(play, playRect)

    help_message1 = font.render('Directions:', True, 'Black')
    help_message2 = font.render('* Words MUST contain at least 4 letters.', True, 'Black')
    help_message3 = font.render('* Words MUST use the letter in the center.', True, 'Black')
    help_message4 = font.render('* Letters can be used more than once.', True, 'Black')
    help_message5 = font.render('Scoring:', True, 'Black')
    help_message6 = font.render('* 4 letter words are worth 1 point.', True, 'Black')
    help_message7 = font.render('* Longer words earn 1 point per letter.', True, 'Black')
    help_message8 = font.render('* If you use all the letters in the hive,', True, 'Black')
    help_message9 = font.render('   you earn an extra 7 points.', True, 'Black')
    help_message10 = font.render('Click on PLAY to play the game.', True, 'Black')


    help_window1 = help_message1.get_rect(topleft = (125, 90))      #(topleft = (160, 220))
    help_window2 = help_message2.get_rect(topleft = (150, 115))
    help_window3 = help_message3.get_rect(topleft = (150, 140))
    help_window4 = help_message4.get_rect(topleft = (150, 165))
    help_window5 = help_message5.get_rect(topleft = (125, 215))
    help_window6 = help_message6.get_rect(topleft = (150, 240))
    help_window7 = help_message7.get_rect(topleft = (150, 265))
    help_window8 = help_message8.get_rect(topleft = (150, 290))
    help_window9 = help_message9.get_rect(topleft = (150, 315))
    help_window10 = help_message10.get_rect(topleft=(125, 365))

    display_surface.blit(help_message1, help_window1)
    display_surface.blit(help_message2, help_window2)
    display_surface.blit(help_message3, help_window3)
    display_surface.blit(help_message4, help_window4)
    display_surface.blit(help_message5, help_window5)
    display_surface.blit(help_message6, help_window6)
    display_surface.blit(help_message7, help_window7)
    display_surface.blit(help_message8, help_window8)
    display_surface.blit(help_message9, help_window9)
    display_surface.blit(help_message10, help_window10)


def shuffleScreen(letter_list):
    global clicking, isPlay_button, isHelp_button, isShuffle_button
    clicking = False
    spliced_list = letter_list[1:]
    random.shuffle(spliced_list)
    shuffled_list = list(letter_list[0]) + spliced_list
    scaled_background = pygame.transform.scale(background, (1440, 810))
    screen.blit(scaled_background, (0, 0))
    screen.blit(shuffle, shuffleRect)
    display_letters(shuffled_list)



    if clicking and isShuffle_button:
        #start()
        isShuffle_button = False
        isPlay_button = False
        clicking = False


# Game loop
home_screen()
while True:



    mouse_pos = pygame.mouse.get_pos()
    if clicking and isHelp_button:
        help_screen()

    if clicking and (not isHelp_button and not isPlay_button and not isShuffle_button):
        clicking = False

    if clicking and isPlay_button:
        #clicking, isPlay_button = play_screen(clicking, isPlay_button)
        play_screen()


    if clicking and isShuffle_button:
        shuffleScreen(test_letter_list)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
                if playRect.collidepoint(mouse_pos):
                    isPlay_button = True
                    isHelp_button = False
                    isShuffle_button = False
                if help_button.collidepoint(mouse_pos):
                    isPlay_button = False
                    isHelp_button = True
                    isShuffle_button = False
                if shuffleRect.collidepoint(mouse_pos):
                    isPlay_button = False
                    isHelp_button = False
                    isShuffle_button = True
            else:
                clicking = False





    pygame.display.update()