"""Import Libraries"""
import pygame
import random

pygame.init()

display_width = 1080
display_height = 720

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('ArtificialCowIntelligenceMilk')

################################################################################

""""STAGE"""
FRAME = pygame.image.load('./stage/frame.png')

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

pause = False
################################################################################

"""COLOE_CODE"""
black_code = (0, 0, 0)
whit_code = (255, 255, 255)

dark_red = (200, 0, 0)
dark_green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

################################################################################

"""Intro"""

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == 'play':
            #     gameplay()
            # elif action == 'quit':
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurface, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurface, textRect)

def quit_game():
    pygame.quit()
    quit()

def unpaused():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(whit_code)
        largeText = pygame.font.Font('freesansbold.ttf',65)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button('CONTINUED', 150, 450, 100, 50, dark_green, bright_green, unpaused)
        button('QUIT', 550, 450, 100, 50, dark_red, bright_red, quit_game)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(whit_code)
        largeText = pygame.font.Font('freesansbold.ttf',65)
        TextSurf, TextRect = text_objects("Artificial Cow Intelligence Milk", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button('START', 150, 450, 100, 50, dark_green, bright_green, gameplay)
        button('QUIT', 550, 450, 100, 50, dark_red, bright_red, quit_game)

        pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, black_code)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

"""STAGE"""
def frame(x, y):
    screen.blit(FRAME, (x, y))

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

def gameplay():
    global pause
    move_X = 0
    move_Y = 90
    move_Text = 0
    text_Y = 660

    run = True

    while run:
        screen.fill(whit_code)
        move_X += 5
        move_Text -= 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()

        """USING FUNCTION"""

        """STAGE"""
        frame(500, -50)

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

        #ZERO
        RED_text_move(move_Text, text_Y)

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

        pygame.display.update()

game_intro()
gameplay()
pygame.quit()
quit()
