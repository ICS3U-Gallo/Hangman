import pygame
from pygame.locals import *
import random


def draw_btns(BUTTONS):
    for button,letter in BUTTONS:
        btn_text = btn_font.render(letter, True, (0, 0, 0))
        btn_text_rect = btn_text.get_rect(center=(button.x + SIZE//2, button.y + SIZE//2))
        pygame.draw.rect(screen, (0, 0, 0), button, 2)
        screen.blit(btn_text, btn_text_rect)


def guess():
    display_word = ''

    for letter in WORD:
        if letter in GUESSED:
            display_word += (letter)
        else:
            display_word += "_ "

    text = letter_font.render(display_word, True, (0, 0, 0))
    screen.blit(text, (400, 200))


pygame.init()
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANG THE MAN")

game_ended = False


# Images
imagee = []
hangman_stat = 0

for i in range(1, 8):
    image = pygame.image.load(f"images/hangman{i}.png")
    imagee.append(image)


# Buttons
ROWS = 2
COLUMS = 13
GAP = 20
SIZE = 40
BOXES = []

for row in range(ROWS):
    for col in range(COLUMS):
        x = ((GAP * col) + GAP) + (SIZE * col)
        y = ((GAP * row) + GAP) + (SIZE * row) + 330
        box = pygame.Rect(x,y,SIZE,SIZE)
        BOXES.append(box)

A = 65
BUTTONS = []

for ind, box in enumerate(BOXES):
    letter = chr(A+ind)
    button = ([box, letter])
    BUTTONS.append(button)

# Fonts
letter_font = pygame.font.SysFont('Comic Sans', 40)
btn_font = pygame.font.SysFont('Comic Sans', 20)
game_font = pygame.font.SysFont('Comic Sans', 40)

# Word
WORD = ['GALLO','APPEND','LIST','BLIT','REMOVE','PRINT','LOOP']
x = random.choice(WORD)
WORD = x
print(x)
GUESSED = []


# Title
title = "Welcome to Hangman!"
text_title = game_font.render(title, True, (0, 0, 0))
text_title_rect = text_title.get_rect(center=(WIDTH//2,text_title.get_height()//2+10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
        if event.type == MOUSEBUTTONDOWN:
            clicked_pos = event.pos
            for button, letter in BUTTONS:
                if button.collidepoint(clicked_pos):
                    GUESSED.append(letter)
                    if letter not in WORD:
                        hangman_stat += 1
                    if hangman_stat == 6:
                        game_over = True


    screen.fill((255, 255, 255))
    screen.blit(imagee[hangman_stat], (150,100))
    screen.blit(text_title, text_title_rect)
    draw_btns(BUTTONS)
    guess()

    win = True

    for letter in WORD:
        if letter not in GUESSED:
            win = False

    if win:
        screen.fill((255, 255, 255))
        game_ended = True
        display_text = 'Congrats you win!'
    else:
        display_text = 'L bozo try again'

    pygame.display.update()

    if game_ended:
        screen.fill((255, 255, 255))
        game_over_text = game_font.render(display_text, True, (0, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2))
        screen.blit(game_over_text, game_over_text_rect)

        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()