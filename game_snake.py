from random import randint
from game_config import GameConfig

class GameSnake():
  UP = 'up'
  DOWN = 'down'
  LEFT = 'left'
  RIGHT = 'right'
  HEAD = 0

  def __init__(self):
    self.direction = self.RIGHT
    self.x = random.randint(5, GameConfig.CELLWIDTH - 15)
    self.y = random.randint(5, GameConfig.CELLHEIGHT - 6)
    self.snake_coordinates = [{'x': self.x, 'y': self.y}, {'x': self.x - 1, 'y': self.y}, {'x': self.x - 2, 'y': self.y}]

  def update_snake(self, food):
      if self.snake_coordinates[self.HEAD]['x'] == food.x and self.snake_coordinates[self.HEAD]['y'] == food.y:
        # move food to random cell
          if GameConfig.FPS <= 14:
             GameConfig.FPS += 1
          food.setNewLocation()
      else:
        # remove tail cell
          del self.snake_coordinates[-1]  

        # add new cell
      if self.direction == self.UP:
          new_cell = {'x': self.snake_coordinates[self.HEAD]['x'], 'y': self.snake_coordinates[self.HEAD]['y'] - 1}
      elif self.direction == self.DOWN:
          new_cell = {'x': self.snake_coordinates[self.HEAD]['x'], 'y': self.snake_coordinates[self.HEAD]['y'] + 1}
      elif self.direction == self.LEFT:
          new_cell = {'x': self.snake_coordinates[self.HEAD]['x'] - 1, 'y': self.snake_coordinates[self.HEAD]['y']}
      elif self.direction == self.RIGHT:
          new_cell = {'x': self.snake_coordinates[self.HEAD]['x'] + 1, 'y': self.snake_coordinates[self.HEAD]['y']}
      self.snake_coordinates.insert(0, new_cell)