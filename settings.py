import pygame
import sys

# set default display screen dimensions
WINDOW_HEIGHT = 576
WINDOW_WIDTH = 704
CELL_HEIGHT, CELL_WIDTH = (64, 64)

# set columns choice section default coordinates
COLUMNS_CHOICE = []
for i in range(2, 9):
    COLUMNS_CHOICE.append((CELL_WIDTH * i, CELL_HEIGHT))


# upload as surface icon image for the display screen
ICON_IMAGE = pygame.image.load("./assets/connect-four.png")

# set default framerate
FRAMERATE = 60

# set default coin color
COIN_COLOR_ONE = 'red'
COIN_COLOR_TWO = 'yellow'

