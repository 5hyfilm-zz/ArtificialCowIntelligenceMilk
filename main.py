"""Import Libraries"""
import pygame
import random

pygame.init()

display_width = 1080
display_height = 720

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
RED_text = pygame.image.load('./circle/RED_circle.png')
GREEN_text = pygame.image.load('./circle/GREEN_circle.png')
BLUE_text = pygame.image.load('./circle/BLUE_circle.png')
ORANGE_text = pygame.image.load('./circle/ORANGE_circle.png')
YELLOW_text = pygame.image.load('./circle/YELLOW_circle.png')
VIOLET_text = pygame.image.load('./circle/VIOLET_circle.png')

################################################################################

"""move_COLOR"""
move_X = 0
move_Y = 90
text_Y = 500

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
        screen.blit(RED_circle, (x, y))

def GREEN_text_move(x, y):
        screen.blit(GREEN_circle, (x, y))

def BLUE_text_move(x, y):
        screen.blit(BLUE_circle, (x, y))

def ORANGE_text_move(x, y):
        screen.blit(ORANGE_circle, (x, y))

def YELLOW_text_move(x, y):
        screen.blit(YELLOW_circle, (x, y))

def VIOLET_text_move(x, y):
        screen.blit(VIOLET_circle, (x, y))

################################################################################

run = True

while run:
    screen.fill((0, 0, 0))
    move_X += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    """USING FUNCTION"""

    """CIRCLE"""
    #POSITIVE
    YELLOW_circle_move(move_X+2530, move_Y)
    RED_circle_move(move_X+2310, move_Y)
    VIOLET_circle_move(move_X+2100, move_Y)
    ORANGE_circle_move(move_X+1890, move_Y)
    RED_circle_move(move_X+1680, move_Y)
    GREEN_circle_move(move_X+1470, move_Y)
    VIOLET_circle_move(move_X+1260, move_Y)
    GREEN_circle_move(move_X+1050, move_Y)
    BLUE_circle_move(move_X+840, move_Y)
    VIOLET_circle_move(move_X+630, move_Y)
    BLUE_circle_move(move_X+420, move_Y)
    YELLOW_circle_move(move_X+210, move_Y)

    #ZERO
    RED_circle_move(move_X, move_Y)

    #NEGATIVE
    GREEN_circle_move(move_X-210, move_Y)
    ORANGE_circle_move(move_X-420, move_Y)
    GREEN_circle_move(move_X-630, move_Y)
    BLUE_circle_move(move_X-840, move_Y)
    ORANGE_circle_move(move_X-1050, move_Y)
    RED_circle_move(move_X-1260, move_Y)
    YELLOW_circle_move(move_X-1470, move_Y)
    VIOLET_circle_move(move_X-1680, move_Y)
    RED_circle_move(move_X-1890, move_Y)
    ORANGE_circle_move(move_X-2100, move_Y)
    GREEN_circle_move(move_X-2310, move_Y)
    YELLOW_circle_move(move_X-2530, move_Y)
    RED_circle_move(move_X, move_Y)

    """TEXT"""
    #POSITIVE
    YELLOW_text_move(move_X-2530, text_Y)
    RED_text_move(move_X-2310, text_Y)
    VIOLET_text_move(move_X-2100, text_Y)
    ORANGE_text_move(move_X-1890, text_Y)
    RED_text_move(move_X-1680, text_Y)
    GREEN_text_move(move_X-1470, text_Y)
    VIOLET_text_move(move_X-1260, text_Y)
    GREEN_text_move(move_X-1050, text_Y)
    BLUE_text_move(move_X-840, text_Y)
    VIOLET_text_move(move_X-630, text_Y)
    BLUE_text_move(move_X-420, text_Y)
    YELLOW_text_move(move_X-210, text_Y)

    #ZERO
    RED_text_move(move_X, move_Y)

    #NEGATIVE
    GREEN_text_move(move_X-210, text_Y)
    ORANGE_text_move(move_X-420, text_Y)
    GREEN_text_move(move_X-630, text_Y)
    BLUE_text_move(move_X-840, text_Y)
    ORANGE_text_move(move_X-1050, text_Y)
    RED_text_move(move_X-1260, text_Y)
    YELLOW_text_move(move_X-1470, text_Y)
    VIOLET_text_move(move_X-1680, text_Y)
    RED_text_move(move_X-1890, text_Y)
    ORANGE_text_move(move_X-2100, text_Y)
    GREEN_text_move(move_X-2310, text_Y)
    YELLOW_text_move(move_X-2530, text_Y)
    RED_text_move(move_X, text_Y)
    pygame.display.update()

pygame.quit()
quit()
