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
    
    def column_is_full(self, chosen_column):
        if len(GAME_BOARD[chosen_column]) == 6:
            return True
        else:
            return False
    
    def has_winner(self):
        for i in range(len(GAME_BOARD)):
            if len(GAME_BOARD[i]) > 0:
                for j in range(len(GAME_BOARD[i])):
                    WINNER_BOARD[i][j] = GAME_BOARD[i][j]
                    
        sample_1 = [1, 1, 1, 1]
        sample_2 = [-1, -1, -1, -1]
        array = np.array(WINNER_BOARD)
        flipped_array = np.fliplr(array)
        has_winner = False
        for i in range(1):
            # check columns for possible winner
            for i in range(7):
                if list(array[i, 0:4]) == sample_1 or list(array[i, 1:5]) == sample_1 or list(array[i, 2:]) == sample_1:
                    has_winner = True
                elif list(array[i, 0:4]) == sample_2 or list(array[i, 1:5]) == sample_2 or list(array[i, 2:]) == sample_2:
                    has_winner = True
            # check rows for possible winner
            flipped_visual_board = []
            for cell in range(6):
                row = []
                for col in WINNER_BOARD:
                    row.append(col[cell])
                flipped_visual_board.append(row)
            for row in flipped_visual_board:
                if row[0:4] == sample_1 or row[1:5] == sample_1 or row[2:6] == sample_1 or row[3:] == sample_1 or \
                    row[0:4] == sample_2 or row[1:5] == sample_2 or row[2:6] == sample_2 or row[3:] == sample_2:
                    has_winner = True
            # check diagonals for possible winner
            if list(np.diag(array))[0:4] == sample_1 or list(np.diag(array))[1:5] == sample_1 or list(np.diag(array))[2:] == sample_1 or \
               list(np.diag(array, k=1))[0:4] == sample_1 or list(np.diag(array, k=1))[1:5] == sample_1 or list(np.diag(array, k=2)) == sample_1 or \
               list(np.diag(array, k=-1))[0:4] == sample_1 or list(np.diag(array, k=-1))[1:5] == sample_1  or list(np.diag(array, k=-1))[2:] == sample_1 or \
               list(np.diag(array, k=-2))[0:4] == sample_1 or list(np.diag(array, k=-2))[1:5] == sample_1 or list(np.diag(array, k=-3)) == sample_1 or \
               list(np.diag(flipped_array))[0:4] == sample_1 or list(np.diag(flipped_array))[1:5] == sample_1 or list(np.diag(flipped_array))[2:] == sample_1 or \
               list(np.diag(flipped_array, k=1))[0:4] == sample_1 or list(np.diag(flipped_array, k=1))[1:5] == sample_1 or list(np.diag(flipped_array, k=2)) == sample_1 or \
               list(np.diag(flipped_array, k=-1))[0:4] == sample_1 or list(np.diag(flipped_array, k=-1))[1:5] == sample_1  or list(np.diag(flipped_array, k=-1))[2:] == sample_1 or \
               list(np.diag(flipped_array, k=-2))[0:4] == sample_1 or list(np.diag(flipped_array, k=-2))[1:5] == sample_1 or list(np.diag(flipped_array, k=-3)) == sample_1:
                   has_winner = True
            elif list(np.diag(array))[0:4] == sample_2 or list(np.diag(array))[1:5] == sample_2 or list(np.diag(array))[2:] == sample_2 or \
                 list(np.diag(array, k=1))[0:4] == sample_2 or list(np.diag(array, k=1))[1:5] == sample_2 or list(np.diag(array, k=2)) == sample_2 or \
                 list(np.diag(array, k=-1))[0:4] == sample_2 or list(np.diag(array, k=-1))[1:5] == sample_2  or list(np.diag(array, k=-1))[2:] == sample_2 or \
                 list(np.diag(array, k=-2))[0:4] == sample_2 or list(np.diag(array, k=-2))[1:5] == sample_2 or list(np.diag(array, k=-3)) == sample_2 or \
                 list(np.diag(flipped_array))[0:4] == sample_2 or list(np.diag(flipped_array))[1:5] == sample_2 or list(np.diag(flipped_array))[2:] == sample_2 or \
                 list(np.diag(flipped_array, k=1))[0:4] == sample_2 or list(np.diag(flipped_array, k=1))[1:5] == sample_2 or list(np.diag(flipped_array, k=2)) == sample_2 or \
                 list(np.diag(flipped_array, k=-1))[0:4] == sample_2 or list(np.diag(flipped_array, k=-1))[1:5] == sample_2  or list(np.diag(flipped_array, k=-1))[2:] == sample_2 or \
                 list(np.diag(flipped_array, k=-2))[0:4] == sample_2 or list(np.diag(flipped_array, k=-2))[1:5] == sample_2 or list(np.diag(flipped_array, k=-3)) == sample_2:
                    has_winner = True
        return has_winner
        
    def intro(self):
        set_mode = ''
        intro = True
        while intro:
            # intro text object
            intro_text = Text(CELL_WIDTH * 9, CELL_HEIGHT * 2, BG_COLOR, "CONNECT FOUR!", "black", "Prequel Demo Shadow Italic", 62)
            self.display_surface.blit(intro_text.render(), (CELL_WIDTH, CELL_HEIGHT))
            
            # instruction text object
            instructions_line_one = Text(CELL_WIDTH * 7, CELL_HEIGHT, BG_COLOR, "Use LEFT and RIGHT arrow keys to choose column", "black", "Arial", 20)
            self.display_surface.blit(instructions_line_one.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 3))
            instructions_line_two = Text(CELL_WIDTH * 7, CELL_HEIGHT, BG_COLOR, "and DOWN arrow key to confirm choice.", "black", "Arial", 20)
            self.display_surface.blit(instructions_line_two.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 4))
            
            # play vs computer button object
            vs_computer_btn = Button(CELL_WIDTH * 4, CELL_HEIGHT * 2, "deepskyblue4", "PLAY VS COMPUTER", "white", "Prequel Demo Shadow Italic", 22)
            self.display_surface.blit(vs_computer_btn.render(), (CELL_WIDTH, CELL_HEIGHT * 5))
            
            # play vs player 2 button object
            vs_player_btn = Button(CELL_WIDTH * 4, CELL_HEIGHT * 2, "deepskyblue4", "PLAY VS PLAYER 2", "white", "Prequel Demo Shadow Italic", 22)
            self.display_surface.blit(vs_player_btn.render(), (CELL_WIDTH * 6, CELL_HEIGHT * 5))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            x, y = pygame.mouse.get_pos()
            if (x >= CELL_WIDTH and x <= CELL_WIDTH * 5) and (y >= CELL_HEIGHT * 5 and y <= CELL_HEIGHT * 7):
                vs_computer_btn.btn_color = "green3"
                vs_computer_btn.text_color = "black"
                self.display_surface.blit(vs_computer_btn.render(), (CELL_WIDTH, CELL_HEIGHT * 5))
            elif (x >= CELL_WIDTH * 6 and x <= CELL_WIDTH * 10) and (y >= CELL_HEIGHT * 5 and y <= CELL_HEIGHT * 7):
                vs_player_btn.btn_color = "green3"
                vs_player_btn.text_color = "black"
                self.display_surface.blit(vs_player_btn.render(), (CELL_WIDTH * 6, CELL_HEIGHT * 5))
            
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if (x >= CELL_WIDTH and x <= CELL_WIDTH * 5) and (y >= CELL_HEIGHT * 5 and y <= CELL_HEIGHT * 7):
                    set_mode = "vs_computer"
                    intro = False
                elif (x >= CELL_WIDTH * 6 and x <= CELL_WIDTH * 10) and (y >= CELL_HEIGHT * 5 and y <= CELL_HEIGHT * 7):
                    set_mode = "vs_player"
                    intro = False
                    
            pygame.display.update()
            self.clock.tick(FRAMERATE)
        return set_mode
    
    def run(self, set_mode):
        # mode set to 2 players
        if set_mode == 'vs_player':
            i = 0
            player = 1
            column = 0
            while True:
                self.display_surface.fill(BG_COLOR)
                self.draw_board()
                self.draw_coin()
                self.has_winner()
                if player == 1:
                    self.display_surface.blit(self.p1.coin.render(), COLUMNS_CHOICE[i])
                elif player == -1:
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
                            if not self.column_is_full(column) and player == 1:
                                GAME_BOARD[column].append(player)
                                player *= -1
                            elif not self.column_is_full(column) and player == -1:
                                GAME_BOARD[column].append(player)
                                player *= -1
                            else:
                                player = player
                pygame.display.update()
                self.clock.tick(FRAMERATE)
        
        