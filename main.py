"""Import Libraries"""
import pygame
import random

pygame.init()

display_width = 1280
display_height = 1080

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ArtificialCowIntelligenceMilk')

"""COLOR_IMG"""
RED_circle = pygame.image.load('./circle/RED_circle.png')
GREEN_circle = pygame.image.load('./circle/GREEN_circle.png')
BLUE_circle = pygame.image.load('./circle/BLUE_circle.png')
ORANGE_circle = pygame.image.load('./circle/ORANGE_circle.png')
YELLOW_circle = pygame.image.load('./circle/YELLOW_circle.png')
VIOLET_circle = pygame.image.load('./circle/VIOLET_circle.png')

"""COLOR_TEXT"""
RED_text = pygame.image.load('./text/RED_text.png')
GREEN_text = pygame.image.load('./text/GREEN_text.png')
BLUE_text = pygame.image.load('./text/BLUE_text.png')
ORANGE_text = pygame.image.load('./text/ORANGE_text.png')
YELLOW_text = pygame.image.load('./text/YELLOW_text.png')
VIOLET_text = pygame.image.load('./text/VIOLET_text.png')

################################################################################

"""move_COLOR"""
move_X = 0
move_Y = 90
text_Y = 660
move_Text = 0

"""CIRCLE"""
def RED_circle_move(x, y):
        screen.blit(RED_circle, (x, y))

def GREEN_circle_move(x, y):
        screen.blit(GREEN_circle, (x, y))

def BLUE_circle_move(x, y):
        screen.blit(BLUE_circle, (x, y))

def ORANGE_circle_move(x, y):
        screen.blit(ORANGE_circle, (x, y))

def YELLOW_circle_move(x, y):
        screen.blit(YELLOW_circle, (x, y))

def VIOLET_circle_move(x, y):
        screen.blit(VIOLET_circle, (x, y))

"""TEXT"""
def RED_text_move(x, y):
        screen.blit(RED_text, (x, y))

def GREEN_text_move(x, y):
        screen.blit(GREEN_text, (x, y))

def BLUE_text_move(x, y):
        screen.blit(BLUE_text, (x, y))

def ORANGE_text_move(x, y):
        screen.blit(ORANGE_text, (x, y))

def YELLOW_text_move(x, y):
        screen.blit(YELLOW_text, (x, y))

def VIOLET_text_move(x, y):
        screen.blit(VIOLET_text, (x, y))

################################################################################

run = True

while run:
    screen.fill((0, 0, 0))
    move_X += 5
    move_Text -= 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    """USING FUNCTION"""

    """CIRCLE"""
    #POSITIVE
    YELLOW_circle_move(move_X+2700, move_Y)
    RED_circle_move(move_X+2475, move_Y)
    VIOLET_circle_move(move_X+2250, move_Y)
    ORANGE_circle_move(move_X+2025, move_Y)
    RED_circle_move(move_X+1800, move_Y)
    GREEN_circle_move(move_X+1575, move_Y)
    VIOLET_circle_move(move_X+1350, move_Y)
    GREEN_circle_move(move_X+1125, move_Y)
    BLUE_circle_move(move_X+900, move_Y)
    VIOLET_circle_move(move_X+675, move_Y)
    BLUE_circle_move(move_X+450, move_Y)
    YELLOW_circle_move(move_X+225, move_Y)

    #ZERO
    RED_circle_move(move_X, move_Y)

    #NEGATIVE
    GREEN_circle_move(move_X-225, move_Y)
    ORANGE_circle_move(move_X-450, move_Y)
    GREEN_circle_move(move_X-675, move_Y)
    BLUE_circle_move(move_X-900, move_Y)
    ORANGE_circle_move(move_X-1125, move_Y)
    RED_circle_move(move_X-1350, move_Y)
    YELLOW_circle_move(move_X-1575, move_Y)
    VIOLET_circle_move(move_X-1800, move_Y)
    RED_circle_move(move_X-2025, move_Y)
    ORANGE_circle_move(move_X-2250, move_Y)
    GREEN_circle_move(move_X-2475, move_Y)
    YELLOW_circle_move(move_X-2700, move_Y)
    RED_circle_move(move_X, move_Y)

    """TEXT"""
    #POSITIVE
    YELLOW_text_move(move_Text+2700, text_Y)
    RED_text_move(move_Text+2475, text_Y)
    VIOLET_text_move(move_Text+2250, text_Y)
    ORANGE_text_move(move_Text+2025, text_Y)
    RED_text_move(move_Text+1800, text_Y)
    GREEN_text_move(move_Text+1575, text_Y)
    VIOLET_text_move(move_Text+1350, text_Y)
    GREEN_text_move(move_Text+1125, text_Y)
    BLUE_text_move(move_Text+900, text_Y)
    VIOLET_text_move(move_Text+675, text_Y)
    BLUE_text_move(move_Text+450, text_Y)
    YELLOW_text_move(move_Text+225, text_Y)

    #NEGATIVE
    GREEN_text_move(move_Text-225, text_Y)
    ORANGE_text_move(move_Text-450, text_Y)
    GREEN_text_move(move_Text-675, text_Y)
    BLUE_text_move(move_Text-900, text_Y)
    ORANGE_text_move(move_Text-1125, text_Y)
    RED_text_move(move_Text-1350, text_Y)
    YELLOW_text_move(move_Text-1575, text_Y)
    VIOLET_text_move(move_Text-1800, text_Y)
    RED_text_move(move_Text-2025, text_Y)
    ORANGE_text_move(move_Text-2250, text_Y)
    GREEN_text_move(move_Text-2475, text_Y)
    YELLOW_text_move(move_Text-2700, text_Y)
    RED_text_move(move_Text, text_Y)
    pygame.display.update()

pygame.quit()
quit()
