import pygame

letter_string = "MBDELNO"
Words_list = ['Embolden', 'Emboldened', 'Bellmen', 'Bloom', 'Bloomed', 'Bomb', 'Bombe', 'Bombed', 'Boom', 'Boomed',
              'Deem', 'Deemed', 'Demo', 'Demoed', 'Demon', 'Dome', 'Domed', 'Doom', 'Doomed', 'Embed', 'Embedded',
              'Emblem', 'Emend', 'Emended', 'Lemon', 'Loom', 'Loomed', 'Meddle', 'Meddled', 'Meld', 'Melded', 'Melee',
              'Melon', 'Meme', 'Memo', 'Mend', 'Mended', 'Mobbed', 'Mode', 'Model', 'Modeled',
              'Modem', 'Mold', 'Molded', 'Mole', 'Moll', 'Mondo', 'Mono', 'Mood', 'Mooed', 'Moon', 'Mooned', 'Noblemen',
              'Omen']

# create game window
pygame.init()
screen = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("BuzzWords")
icon = pygame.image.load("/Users/jesspederson/buzz_worrds/client/Media/Bee.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font("/Users/jesspederson/buzz_worrds/client/Font/LexendDeca-VariableFont_wght.ttf", 50)

# font setup
# def font(font_size):
# font = pygame.font.Font("/Users/jesspederson/buzz_worrds/client/Font/LexendDeca-VariableFont_wght.ttf",font_size)

# set-up
background = pygame.image.load("/Users/jesspederson/buzz_worrds/client/Media/Buzzwords_background.jpg")
scaled_background = pygame.transform.scale(background, (1440, 810))
score_text = font.render('88', True, 'Black')

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
bee = pygame.image.load("/Users/jesspederson/buzz_worrds/client/Media/Bee.png")
default_bee_size = (250, 200)
bee_250 = pygame.transform.scale(bee, default_bee_size)
starting_bee = rotate_bee(45)

# bee dance function

# def correct_word ():

running = True
while running:
    # set screen color as first/bottom layer
    screen.blit(scaled_background, (0, 0))
    screen.blit(starting_bee, (bee_x, bee_y))
    screen.blit(score_text, (300, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # quit when pressing escape
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

        # always have at the end
        pygame.display.update()
        clock.tick(60)
