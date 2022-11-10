
# This is the homepage
import pygame

# initialize pygame
pygame.init()

# Change the title, logo
pygame.display.set_caption("BuzzWords")

# Image.png 32 x 32 pixel size
icon = pygame.image.load("C:/Users/Araceli Ramirez/Documents/buzz_worrds/client/venv/Bee.png")
pygame.display.set_icon(icon)

#create the screen
screen = pygame.display.set_mode((1440,810))

# create a background
background = pygame.image.load('C:/Users/Araceli Ramirez/Documents/buzz_worrds/client/venv/Buzzwords_background_-_version_A.png')
background_rect = background.get_rect(topleft = (0,50))


# Game loop
while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    pygame.display.update()