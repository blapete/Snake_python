from game_config import GameConfig
from game_snake import GameSnake
from game_food import GameFood
import pygame, sys

class GameActions():
    '''
    All the necessary actions to set up the game environment and handle user input.
    '''
    def __init__(self):
        pygame.init()
        self.game_window = pygame.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
        self.font_style = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('python snake game')
        self.game_clock = pygame.time.Clock()
        self.food = GameFood()
        self.snake = GameSnake()
    
    def create_grid_pattern(self):   
        # vertical line
        for x in range(0, GameConfig.WINDOW_WIDTH, GameConfig.CELLSIZE):
                      #     (surface, color, start_pos, end_pos, width)
            pygame.draw.line(self.game_window, GameConfig.DARKGRAY, (x, 0), (x, GameConfig.WINDOW_HEIGHT))
        # horizontal line
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
                      #     (surface, color, start_pos, end_pos, width)
            pygame.draw.line(self.game_window, GameConfig.DARKGRAY, (0, y), (GameConfig.WINDOW_WIDTH, y))