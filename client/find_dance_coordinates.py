import pygame

# create game window
pygame.init()
screen = pygame.display.set_mode((1440, 810))
clock = pygame.time.Clock()

background = pygame.image.load("../client/Media/Buzzwords_background.jpg")
scaled_background = pygame.transform.scale(background, (1440, 810))

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


# resize & angle bee
bee = pygame.image.load("../client/Media/Bee.png")
default_bee_size = (250, 200)
bee_250 = pygame.transform.scale(bee, default_bee_size)
starting_bee = rotate_bee(45)

# game loop
running = True
while running:
    # set screen color as first/bottom layer
    screen.blit(scaled_background, (0, 0))
    screen.blit(starting_bee, (bee_x, bee_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # quit when pressing escape
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            print(x, y)

        # always have at the end
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(60)
