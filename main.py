from settings import *
from player import *
from coin import *
from game import *


if __name__ == '__main__':
    
    # initializing standard objects
    coin_one = Coin(COIN_COLOR_ONE)
    coin_two = Coin(COIN_COLOR_TWO)
    player_one = Player(coin_one)
    player_two = Player(coin_two)
    game = Game(player_one, player_two)
    
    # running the game
    game.intro()
    game.run()
    game.winner_screen()