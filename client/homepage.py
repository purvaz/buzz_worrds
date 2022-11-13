
# This is the homepage
import pygame

# initialize pygame
pygame.init()

# Change the title, logo
pygame.display.set_caption("BuzzWords")

#create the screen
screen = pygame.display.set_mode((1440,810))

# Image.png 32 x 32 pixel size
icon = pygame.image.load("C:/Users/Araceli Ramirez/Documents/buzz_worrds/client/venv/Bee.png").convert_alpha()
pygame.display.set_icon(icon)



# create the bee for the help message
bee = pygame.image.load('C:/Users/Araceli Ramirez/Documents/buzz_worrds/client/venv/help_bee.png').convert_alpha()
help_button = bee.get_rect(topleft = (1260, 220))


# create a background
background = pygame.image.load('C:/Users/Araceli Ramirez/Documents/buzz_worrds/client/venv/Buzzwords_background_-_version_A.png').convert_alpha()
background_rect = background.get_rect(topleft = (0, 50))
#help_button.fill('Yellow', background_rect)


# Game loop
while True:
    scaled_bee = pygame.transform.scale(bee, (150, 125))
    scaled_background = pygame.transform.scale(background, (1440, 810))
    screen.blit(scaled_background, (0, 0))
    #screen.blit(scaled_bee, (100, 200))
    screen.blit(scaled_bee, help_button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.mouse.get_pressed():
            pos = pygame.mouse.get_pos()
            if button.collidepoint(pos):
                help_message = font.render('Create a word with 4-7 letters /n using any combination of the letters in the pandgram. /n You must use the letter in the center.',True, 'Purple')
                help_window2 = help_message.get_rect(topleft=(160, 220))
                scaled_bee = pygame.transform.scale(bee, (50, 50))
                scaled_background = pygame.transform.scale(background, (1440, 810))
                screen.blit(scaled_background, (0, 0))
                screen.blit(scaled_bee, (100, 200))
                screen.blit(help_message, help_window2)




    pygame.display.update()