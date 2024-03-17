from settings import *

class Coin():
    def __init__(self, color="red"):
        self.color = color
        self.coin_surface = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        self.coin_surface.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.coin_surface, color=self.color, center=(CELL_WIDTH / 2, CELL_HEIGHT / 2), radius=20)
    
    def render(self):
        return self.coin_surface