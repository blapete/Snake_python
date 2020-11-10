from game_config import GameConfig
from game_snake import GameSnake
from game_food import GameFood
import pygame, sys

class GameActions():
  def __init__(self):
    pygame.init()
    self.screen_dimensions = pygame.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
    self.font_style = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('python snake game')
    self.game_clock = pygame.time.Clock()
    self.food = GameFood()
    self.snake = GameSnake()
    
