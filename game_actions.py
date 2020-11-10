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

    def create_game_snake(self):
        for cell in self.snake.snake_coordinates:
            x = cell['x'] * GameConfig.CELLSIZE
            y = cell['y'] * GameConfig.CELLSIZE
            snake_rectangle = pygame.Rect(x, y, GameConfig.CELLSIZE, GameConfig.CELLSIZE)
            pygame.draw.rect(self.game_window, GameConfig.DARKGREEN, snake_rectangle)
            snake_inner_rectangle = pygame.Rect(x + 4, y + 4, GameConfig.CELLSIZE - 8, GameConfig.CELLSIZE - 8)
            pygame.draw.rect(self.game_window, GameConfig.GREEN, snake_inner_rectangle)

    def create_game_food(self):
        x = self.food.x * GameConfig.CELLSIZE
        y = self.food.y * GameConfig.CELLSIZE
        food_rectangle = pygame.Rect(x, y, GameConfig.CELLSIZE, GameConfig.CELLSIZE)
        pygame.draw.rect(self.game_window, GameConfig.RED, food_rectangle)


    def create_game_score(self, score):
        game_score = self.font_style.render('Score: %s' % (score), True, GameConfig.WHITE)
        game_score_rectangle = game_score.get_rect()
        game_score_rectangle.topleft = (GameConfig.WINDOW_WIDTH - 120, 10)
        self.game_window.blit(game_score, game_score_rectangle)


    def create_game_frame(self, fps=None):
        # print(f'clock is ticking at {fps} frames per second')
        self.game_window.fill(GameConfig.BG_COLOR)
        self.create_grid_pattern()
        self.create_game_snake()
        self.create_game_food()
        self.create_game_score(len(self.snake.snake_coordinates) - 3)
        pygame.display.update()
        self.game_clock.tick(GameConfig.FPS)


    def check_user_key_press(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()
            quit()
        user_key_up = pygame.event.get(pygame.KEYUP)
        if len(user_key_up) == 0:
            return None
        if user_key_up[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        return user_key_up[0].key


    def response_to_key_press(self, key_press):
        if (key_press.key == pygame.K_LEFT or key_press.key == pygame.K_a) and self.snake.direction != self.snake.RIGHT:
            self.snake.direction = self.snake.LEFT
        elif (key_press.key == pygame.K_RIGHT or key_press.key == pygame.K_d) and self.snake.direction != self.snake.LEFT:
            self.snake.direction = self.snake.RIGHT
        elif (key_press.key == pygame.K_UP or key_press.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
            self.snake.direction = self.snake.UP
        elif (key_press.key == pygame.K_DOWN or key_press.key == pygame.K_s) and self.snake.direction != self.snake.UP:
            self.snake.direction = self.snake.DOWN
        elif key_press.key == pygame.K_ESCAPE:
            pygame.quit()


    def game_reset(self):
        del self.food
        del self.snake
        GameConfig.FPS = 8
        self.food = GameFood()
        self.snake = GameSnake()
        return True


    def create_start_message(self, x=0):
        start_message = self.font_style.render('Press any key to play.', True, GameConfig.WHITE)
        start_message_rectangle = start_message.get_rect()
        start_message_rectangle.topleft = (GameConfig.WINDOW_WIDTH - 410, GameConfig.WINDOW_HEIGHT -  (GameConfig.WINDOW_HEIGHT / 2 - x))
        self.game_window.blit(start_message, start_message_rectangle)


    def game_over(self):
        if (self.snake.snake_coordinates[self.snake.HEAD]['x'] == -1 or 
            self.snake.snake_coordinates[self.snake.HEAD]['x'] == GameConfig.CELLWIDTH or
            self.snake.snake_coordinates[self.snake.HEAD]['y'] == -1 or 
            self.snake.snake_coordinates[self.snake.HEAD]['y'] == GameConfig.CELLHEIGHT):
            return self.game_reset()

        for cell in self.snake.snake_coordinates[1:]:
            if (cell['x'] == self.snake.snake_coordinates[self.snake.HEAD]['x'] and
                cell['y'] == self.snake.snake_coordinates[self.snake.HEAD]['y']):
                return self.game_reset()