from settings import *

# creating a class that contains all the game's functionalities
class Game():
    def __init__(self, player_one, player_two):
        pygame.init()
        self.p1 = player_one
        self.p2 = player_two
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.fill(BG_COLOR)
        self.window_label = pygame.display.set_caption('CONNECT FOUR!')
        self.window_icon = pygame.display.set_icon(ICON_IMAGE)
        self.clock = pygame.time.Clock()
        
    def draw_board(self):        
        pygame.draw.rect(self.display_surface, color="blue3", rect=(CELL_WIDTH * 2, CELL_HEIGHT * 2, CELL_WIDTH * 7, CELL_HEIGHT * 6))
        circle_surface = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        circle_surface.set_colorkey((0, 0, 0))
        pygame.draw.circle(circle_surface, color=BG_COLOR, center=(CELL_WIDTH / 2, CELL_HEIGHT / 2), radius=20)
        for i in range(len(COORDINATES)):
            for j in range(len(COORDINATES[i])):
                self.display_surface.blit(circle_surface, COORDINATES[i][j])
    
    def draw_coin(self):
        for i in range(len(GAME_BOARD)):
            if len(GAME_BOARD[i]) > 0:
                for j in range(len(GAME_BOARD[i])):
                    if GAME_BOARD[i][j] == 1:
                        self.display_surface.blit(self.p1.coin.render(), COORDINATES[i][j])
                    elif GAME_BOARD[i][j] == -1:
                        self.display_surface.blit(self.p2.coin.render(), COORDINATES[i][j])
    
    def check_winner(self):
        for i in range(len(GAME_BOARD)):
            if len(GAME_BOARD[i]) > 0:
                for j in range(len(GAME_BOARD[i])):
                    WINNER_BOARD[i][j] = GAME_BOARD[i][j]
        
        
    def run(self):
        i = 0
        turn = 1
        column = 0
        while True:
            self.display_surface.fill(BG_COLOR)
            self.draw_board()
            self.draw_coin()
            self.check_winner()
            if turn == 1:
                self.display_surface.blit(self.p1.coin.render(), COLUMNS_CHOICE[i])
            elif turn == -1:
                self.display_surface.blit(self.p2.coin.render(), COLUMNS_CHOICE[i])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if i == 0:
                            i = 7
                        i -= 1
                    elif event.key == pygame.K_RIGHT:
                        if i == 6:
                            i = -1
                        i += 1
                    if event.key == pygame.K_DOWN:
                        column = i
                        if turn == 1:
                            GAME_BOARD[column].append(turn)
                            turn *= -1
                        elif turn == -1:
                            GAME_BOARD[column].append(turn)
                            turn *= -1
            print(WINNER_BOARD)  
            pygame.display.update()
            self.clock.tick(FRAMERATE)
