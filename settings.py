import pygame
import sys
import numpy as np

# set default display screen dimensions
WINDOW_HEIGHT = 576
WINDOW_WIDTH = 704
CELL_HEIGHT, CELL_WIDTH = (64, 64)

# set columns choice section default coordinates
COLUMNS_CHOICE = []
for i in range(2, 9):
    COLUMNS_CHOICE.append((CELL_WIDTH * i, CELL_HEIGHT))

# set default board
GAME_BOARD = [[] for i in range(7)]

# set default check for winner board
WINNER_BOARD = [[" " for i in range(6)] for i in range(7)]

# set default coordinates
COORDINATES = [[(CELL_WIDTH*2, CELL_HEIGHT*7), (CELL_WIDTH*2, CELL_HEIGHT*6), (CELL_WIDTH*2, CELL_HEIGHT*5), (CELL_WIDTH*2, CELL_HEIGHT*4), (CELL_WIDTH*2, CELL_HEIGHT*3), (CELL_WIDTH*2, CELL_HEIGHT*2)], [(CELL_WIDTH*3, CELL_HEIGHT*7), (CELL_WIDTH*3, CELL_HEIGHT*6), (CELL_WIDTH*3, CELL_HEIGHT*5), (CELL_WIDTH*3, CELL_HEIGHT*4), (CELL_WIDTH*3, CELL_HEIGHT*3), (CELL_WIDTH*3, CELL_HEIGHT*2)], [(CELL_WIDTH*4, CELL_HEIGHT*7), (CELL_WIDTH*4, CELL_HEIGHT*6), (CELL_WIDTH*4, CELL_HEIGHT*5), (CELL_WIDTH*4, CELL_HEIGHT*4), (CELL_WIDTH*4, CELL_HEIGHT*3), (CELL_WIDTH*4, CELL_HEIGHT*2)], [(CELL_WIDTH*5, CELL_HEIGHT*7), (CELL_WIDTH*5, CELL_HEIGHT*6), (CELL_WIDTH*5, CELL_HEIGHT*5), (CELL_WIDTH*5, CELL_HEIGHT*4), (CELL_WIDTH*5, CELL_HEIGHT*3), (CELL_WIDTH*5, CELL_HEIGHT*2)], [(CELL_WIDTH*6, CELL_HEIGHT*7), (CELL_WIDTH*6, CELL_HEIGHT*6), (CELL_WIDTH*6, CELL_HEIGHT*5), (CELL_WIDTH*6, CELL_HEIGHT*4), (CELL_WIDTH*6, CELL_HEIGHT*3), (CELL_WIDTH*6, CELL_HEIGHT*2)], [(CELL_WIDTH*7, CELL_HEIGHT*7), (CELL_WIDTH*7, CELL_HEIGHT*6), (CELL_WIDTH*7, CELL_HEIGHT*5), (CELL_WIDTH*7, CELL_HEIGHT*4), (CELL_WIDTH*7, CELL_HEIGHT*3), (CELL_WIDTH*7, CELL_HEIGHT*2)], [(CELL_WIDTH*8, CELL_HEIGHT*7), (CELL_WIDTH*8, CELL_HEIGHT*6), (CELL_WIDTH*8, CELL_HEIGHT*5), (CELL_WIDTH*8, CELL_HEIGHT*4), (CELL_WIDTH*8, CELL_HEIGHT*3), (CELL_WIDTH*8, CELL_HEIGHT*2)]]

# upload as surface icon image for the display screen
ICON_IMAGE = pygame.image.load("./assets/connect-four.png")

# set default framerate
FRAMERATE = 60

# set default coin color
COIN_COLOR_ONE = 'red'
COIN_COLOR_TWO = 'yellow'

# set default background color
BG_COLOR = 'deepskyblue3'

# usefull objects
class Button(object):
    def __init__(self, width, height, btn_color, text, text_color, font, font_size):
        self.width = width
        self.height = height
        self.btn_color = btn_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size = font_size   
         
    def render(self):  
        button_block = pygame.Surface((self.width, self.height))  
        button_block.fill(self.btn_color)
        font_to_use = pygame.font.SysFont(self.font, self.font_size)
        text_to_render = font_to_use.render(self.text, True, self.text_color)
        text_surface = text_to_render.get_rect()
        text_surface.center = (self.width / 2, self.height / 2)
        button_block.blit(text_to_render, text_surface)
        return button_block

class Text(object):
    def __init__(self, width, height, box_color, text, text_color, font, font_size):
        self.width = width
        self.height = height
        self.box_color = box_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size = font_size
        
    def render(self):
        text_block = pygame.Surface((self.width, self.height))
        text_block.fill(self.box_color)
        font = pygame.font.SysFont(self.font, self.font_size)
        text = font.render(self.text, True, self.text_color)
        text_surface = text.get_rect()
        text_surface.center = (self.width / 2, self.height / 2)
        text_block.blit(text, text_surface)
        return text_block