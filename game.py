from settings import *

# creating a class that contains all the game's functionalities
class Game():
    def __init__(self, player_one, player_two):
        pygame.init()
        self.p1 = player_one
        self.p2 = player_two
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.fill('ghostwhite')
        self.window_label = pygame.display.set_caption('CONNECT FOUR!')
        self.window_icon = pygame.display.set_icon(ICON_IMAGE)
        self.clock = pygame.time.Clock()
        
    def draw_grid(self):
        # draw base
        pygame.draw.rect(self.display_surface, color="azure4", rect=(0, WINDOW_HEIGHT-CELL_HEIGHT, WINDOW_WIDTH, CELL_HEIGHT))
        
        # draw columns
        for i in range(2, 9, 2):
            pygame.draw.rect(self.display_surface, color="azure3", rect=(CELL_WIDTH * i, CELL_HEIGHT * 2, CELL_WIDTH, CELL_HEIGHT * 6))
        
    def run(self):
        while True:
            self.draw_grid()
            self.display_surface.blit(self.p1.coin.render(), COLUMNS_CHOICE[6])
            
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)
