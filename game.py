from settings import *

# creating a class that contains all the game's functionalities
class Game():
    def __init__(self, player_one, player_two):
        pygame.init()
        self.p1 = player_one
        self.p2 = player_two
        self.winner = ''
        self.set_mode = ''
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface.fill(BG_COLOR)
        self.board_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.board_surface.set_colorkey((0, 0, 0))
        self.window_label = pygame.display.set_caption('CONNECT FOUR!')
        self.window_icon = pygame.display.set_icon(ICON_IMAGE)
        self.clock = pygame.time.Clock()
        
        # set default board
        self.game_board = [[] for i in range(7)]
        # set default check for winner board
        self.winner_board = [[" " for i in range(6)] for i in range(7)]
    
    def reset(self):
        self.game_board = [[] for i in range(7)]
        self.winner_board = [[" " for i in range(6)] for i in range(7)]
    
    def draw_board(self):        
        pygame.draw.rect(self.board_surface, color="blue3", rect=(CELL_WIDTH * 2, CELL_HEIGHT * 2, CELL_WIDTH * 7, CELL_HEIGHT * 6))
        circle_surface = pygame.Surface((CELL_WIDTH, CELL_HEIGHT))
        circle_surface.set_colorkey((0, 0, 0))
        pygame.draw.circle(circle_surface, color=BG_COLOR, center=(CELL_WIDTH / 2, CELL_HEIGHT / 2), radius=20)
        for i in range(len(COORDINATES)):
            for j in range(len(COORDINATES[i])):
                self.board_surface.blit(circle_surface, COORDINATES[i][j])
        self.display_surface.blit(self.board_surface, (0, 0))
    
    def draw_coin(self):
        for i in range(len(self.game_board)):
            if len(self.game_board[i]) > 0:
                for j in range(len(self.game_board[i])):
                    if self.game_board[i][j] == 1:
                        self.board_surface.blit(self.p1.coin.render(), COORDINATES[i][j])
                    elif self.game_board[i][j] == -1:
                        self.board_surface.blit(self.p2.coin.render(), COORDINATES[i][j])
        self.display_surface.blit(self.board_surface, (0, 0))
    
    def column_is_full(self, chosen_column):
        if len(self.game_board[chosen_column]) == 6:
            return True
        else:
            return False
    
    def has_winner(self):
        for i in range(len(self.game_board)):
            if len(self.game_board[i]) > 0:
                for j in range(len(self.game_board[i])):
                    self.winner_board[i][j] = self.game_board[i][j]
                    
        sample_1 = ["1", "1", "1", "1"]
        sample_2 = ["-1", "-1", "-1", "-1"]
        array = np.array(self.winner_board)
        list(array[i, 0:4])
        flipped_array = np.fliplr(array)
        has_winner = False
        for i in range(1):
            # check columns for possible winner
            for i in range(7):
                if list(array[i, 0:4]) == sample_1 or list(array[i, 1:5]) == sample_1 or list(array[i, 2:]) == sample_1:
                    has_winner = True
                    self.winner = 'player 1'
                elif list(array[i, 0:4]) == sample_2 or list(array[i, 1:5]) == sample_2 or list(array[i, 2:]) == sample_2:
                    has_winner = True
                    self.winner = 'player 2'
                    
            # check rows for possible winner
            for i in range(6):
                if list(array[0:4, i]) == sample_1 or list(array[1:5, i]) == sample_1 or list(array[2:6, i]) == sample_1 or list(array[3:, i]) == sample_1:
                    has_winner = True
                    self.winner = 'player 1'
                elif list(array[0:4, i]) == sample_2 or list(array[1:5, i]) == sample_2 or list(array[2:6, i]) == sample_2 or list(array[3:, i]) == sample_2:
                    has_winner = True
                    self.winner = 'player 2'
                    
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
                   self.winner = 'player 1'
            elif list(np.diag(array))[0:4] == sample_2 or list(np.diag(array))[1:5] == sample_2 or list(np.diag(array))[2:] == sample_2 or \
                 list(np.diag(array, k=1))[0:4] == sample_2 or list(np.diag(array, k=1))[1:5] == sample_2 or list(np.diag(array, k=2)) == sample_2 or \
                 list(np.diag(array, k=-1))[0:4] == sample_2 or list(np.diag(array, k=-1))[1:5] == sample_2  or list(np.diag(array, k=-1))[2:] == sample_2 or \
                 list(np.diag(array, k=-2))[0:4] == sample_2 or list(np.diag(array, k=-2))[1:5] == sample_2 or list(np.diag(array, k=-3)) == sample_2 or \
                 list(np.diag(flipped_array))[0:4] == sample_2 or list(np.diag(flipped_array))[1:5] == sample_2 or list(np.diag(flipped_array))[2:] == sample_2 or \
                 list(np.diag(flipped_array, k=1))[0:4] == sample_2 or list(np.diag(flipped_array, k=1))[1:5] == sample_2 or list(np.diag(flipped_array, k=2)) == sample_2 or \
                 list(np.diag(flipped_array, k=-1))[0:4] == sample_2 or list(np.diag(flipped_array, k=-1))[1:5] == sample_2  or list(np.diag(flipped_array, k=-1))[2:] == sample_2 or \
                 list(np.diag(flipped_array, k=-2))[0:4] == sample_2 or list(np.diag(flipped_array, k=-2))[1:5] == sample_2 or list(np.diag(flipped_array, k=-3)) == sample_2:
                    has_winner = True
                    self.winner = 'player 2'
        return has_winner
        
    def intro(self):
        intro = True
        while intro:
            # intro text object
            self.display_surface.fill(BG_COLOR)
            intro_text = Text(CELL_WIDTH * 9, CELL_HEIGHT * 2, BG_COLOR, "CONNECT FOUR!", "black", "Prequel Demo Shadow Italic", 62)
            self.display_surface.blit(intro_text.render(), (CELL_WIDTH, CELL_HEIGHT))
            
            # instruction text object
            instructions_line_one = Text(CELL_WIDTH * 7, CELL_HEIGHT, BG_COLOR, "Use LEFT and RIGHT arrow keys to choose column", "black", "Impact", 20)
            self.display_surface.blit(instructions_line_one.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 3))
            instructions_line_two = Text(CELL_WIDTH * 7, CELL_HEIGHT, BG_COLOR, "and DOWN arrow key to confirm choice.", "black", "Impact", 20)
            self.display_surface.blit(instructions_line_two.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 4))
            
            # play vs computer button object
            vs_computer_btn = Button(CELL_WIDTH * 4, CELL_HEIGHT * 2, "deepskyblue4", "PLAY VS COMPUTER", "white", "Impact", 22)
            self.display_surface.blit(vs_computer_btn.render(), (CELL_WIDTH, CELL_HEIGHT * 5))
            
            # play vs player 2 button object
            vs_player_btn = Button(CELL_WIDTH * 4, CELL_HEIGHT * 2, "deepskyblue4", "PLAY VS PLAYER 2", "white", "Impact", 22)
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
                    self.set_mode = "vs_computer"
                    intro = False
                elif (x >= CELL_WIDTH * 6 and x <= CELL_WIDTH * 10) and (y >= CELL_HEIGHT * 5 and y <= CELL_HEIGHT * 7):
                    self.set_mode = "vs_player"
                    intro = False
                    
            pygame.display.update()
            self.clock.tick(FRAMERATE)
            
    def run(self):
        print(self.game_board)
        if self.set_mode == 'vs_player':
            i = 0
            player = 1
            column = 0
            mode_running = True
            while mode_running:
                self.display_surface.fill(BG_COLOR)
                self.draw_board()
                self.draw_coin()
                if self.has_winner():
                    mode_running = False
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
                                self.game_board[column].append(player)
                                player *= -1
                            elif not self.column_is_full(column) and player == -1:
                                self.game_board[column].append(player)
                                player *= -1
                            else:
                                player = player
                pygame.display.update()
                self.clock.tick(FRAMERATE)
                
        if self.set_mode == 'vs_computer':
            i = 0
            player = 1
            column = 0
            mode_running = True
            while mode_running:
                self.display_surface.fill(BG_COLOR)
                self.draw_board()
                self.draw_coin()
                if self.has_winner():
                    mode_running = False
                    break
                if player == 1:
                    self.display_surface.blit(self.p1.coin.render(), COLUMNS_CHOICE[i])
                elif player == -1:
                    self.display_surface.blit(self.p2.coin.render(), COLUMNS_CHOICE[i])
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if player == 1:
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
                                if not self.column_is_full(column) :
                                    self.game_board[column].append(player)
                                    player *= -1
                                else:
                                    player = player
                if player == -1:   
                    column = random.randint(0, 6)         
                    if not self.column_is_full(column):
                        self.game_board[column].append(player)
                        player *= -1
                    else:
                        player = player 
                pygame.display.update()
                self.clock.tick(FRAMERATE)            
            
    def winner_screen(self):
        winner_running = True
        while winner_running:
            winner_text = Text(CELL_WIDTH * 5, CELL_HEIGHT * 1, "deepskyblue4", "", "white", "Impact", 36)
            if self.winner == "player 1":
                winner_text.text = "Player 1 won!"
                self.display_surface.blit(winner_text.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 1))
            elif self.winner == "player 2" and self.set_mode == "vs_player":
                winner_text.text = "Player 2 won!"
                self.display_surface.blit(winner_text.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 1))
            elif self.winner == "player 2" and self.set_mode == "vs_computer":
                winner_text.text = "Computer won!"
                self.display_surface.blit(winner_text.render(), (CELL_WIDTH * 2, CELL_HEIGHT * 1))
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            restart_button = Button(CELL_WIDTH * 2, CELL_HEIGHT, "deepskyblue1", "Restart", "white", "Impact", 24)
            self.display_surface.blit(restart_button.render(), (CELL_WIDTH * 7, CELL_HEIGHT))    
            
            x, y = pygame.mouse.get_pos()
            if (x >= CELL_WIDTH * 7 and x <= CELL_WIDTH *9) and (y >= CELL_HEIGHT and y <= CELL_HEIGHT * 2):
                restart_button.btn_color = "green3"
                self.display_surface.blit(restart_button.render(), (CELL_WIDTH * 7, CELL_HEIGHT))

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if (x >= CELL_WIDTH * 7 and x <= CELL_WIDTH *9) and (y >= CELL_HEIGHT and y <= CELL_HEIGHT * 2):
                    restart = True
                    self.display_surface.fill(BG_COLOR)
                    winner_running = False
                    self.reset()
                    
            pygame.display.update()
            self.clock.tick(FRAMERATE)
        return restart
    
                    