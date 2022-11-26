import pygame
import random
import sys

# create game window
pygame.init()
screen = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("BuzzWords")
icon = pygame.image.load("../client/Media/Bee.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


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
        text_y = 140
        tx = text_x - fw / 2
        ty = text_y + y_offset
        font_surface = wc_font.render(line, True, "Black")
        screen.blit(font_surface, (tx, ty))
        y_offset += fh
    pygame.display.flip()


# scoring
score_font = font(60)
score = 15  # will later be fed from backend
score_string = str(score)
if score >= 100:
    score_location = (95, 580)
elif 10 <= score < 100:
    score_location = (103, 580)
elif score < 10:
    score_location = (110, 580)

# guessing
guess_font = font(75)
max_guess_length = 13
guess_input = ''
# guess_location_x = 335
# guess_location_y = 680
# guess_location = (guess_location_x,guess_location_y)
# note to self: pygame.Rect(x,y,w,h)
guess_box = pygame.Rect(335, 677, 625, 95)
guess_box_color = (238, 238, 238)

# bee word bubble
wordbubble_font = font(24)
wordbubble_box = pygame.Rect(992, 145, 140, 90)
wordbubble_box_color = (255, 255, 255)
message = ""
instructions_prompt = "Need instructions? Click on me."

# surfaces
background = pygame.image.load("../client/Media/Buzzwords_background.jpg")
scaled_background = pygame.transform.scale(background, (1440, 810))
score_text = score_font.render(score_string, True, 'Black')
wordbubble_text = wordbubble_font.render(message, True, 'Black')
# display_guess = guess_font.render(guess_input, True, 'Black')

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
# wordbubble_bee_location = (bee_x-135.65,bee_y-76.85)
wbx = 964.35
wby = 123.15
wordbubble_bee_location = (wbx, wby)


def correct_answer_dance():
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
    praise_length = len(praise)
    chosen_index = int(random.randint(0, praise_length))
    selected_praise = praise[chosen_index]
    return selected_praise


def wordbubble_pop_up(wordbubble_message):
    screen.blit(wordbubble_bee_250, wordbubble_bee_location)
    pygame.draw.rect(screen, wordbubble_box_color, wordbubble_box)
    wrapping_centered_text(wordbubble_message, screen)
    pygame.display.flip()


running = True
while running:
    screen.blit(scaled_background, (0, 0))
    screen.blit(starting_bee, (bee_x, bee_y))
    screen.blit(score_text, score_location)

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
                selected_praise = correct_answer_dance()
                wordbubble_pop_up(selected_praise)
                pygame.time.delay(50)
                guess_input = ""
            elif event.key == pygame.K_TAB:
                wordbubble_pop_up(instructions_prompt)
                guess_input = ""
            elif event.key == pygame.K_BACKSPACE:
                guess_input = guess_input[:-1]
            else:
                if len(guess_input) < max_guess_length:
                    guess_input += event.unicode

        pygame.draw.rect(screen, guess_box_color, guess_box)
        display_guess = guess_font.render(guess_input, True, 'Black')
        screen.blit(display_guess, (guess_box.x + 10, guess_box.y + 10))
        guess_box.w = max(100, display_guess.get_width() + 10)

        # always have at the end
        pygame.display.flip()
        clock.tick(60)
