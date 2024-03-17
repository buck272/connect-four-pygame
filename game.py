from settings import *

# creating a class that contains all the game's functionalities
class Game():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.fill('ghostwhite')
        self.window_label = pygame.display.set_caption('CONNECT FOUR!')
        self.window_icon = pygame.display.set_icon(ICON_IMAGE)
        self.clock = pygame.time.Clock()
        
    def draw_grid(self):
        # draw base
        pygame.draw.rect(self.display_surface, color="azure4", rect=(0, WINDOW_HEIGHT-CELL_HEIGHT, WINDOW_WIDTH, CELL_HEIGHT))
        
        # draw columns
        columns_container = pygame.Surface((CELL_WIDTH * 7, CELL_HEIGHT * 6))
        
        
    def run(self):
        while True:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)
