from random import randint
from game_config import GameConfig

class GameFood():
  def __init__(self):
    self.setNewLocation()
  
  def setNewLocation(self):
      print(f'cell width: {GameConfig.CELLWIDTH}, cell height: {GameConfig.CELLHEIGHT}')
      self.x = randint(0, GameConfig.CELLWIDTH - 1)
      self.y = randint(0, GameConfig.CELLHEIGHT - 1)



def main():
    food = GameFood()
    print(food.x, food.y)


if __name__ == '__main__':
    main()