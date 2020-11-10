import sys
from game_actions import GameActions

"""
Start Menu:
 - 'press a key to play'
Food:
 - assigned to a random cell
Snake:
 - eats food, grows by one cell
 - food relocates to new random cell
Snake Movement:
 - body trails the head
Score:
 - increases by one per food eaten
Game Over:
 - snake hits wall or itself
 - show start message to play again
"""

def GameStart():
    snake_game = GameActions()
    snake_game.game_run()
    sys.exit()

if __name__ == '__main__':
    GameStart()