from config import Config
from snake import Snake
from apple import Apple
import pygame
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Snake Game')
        self.apple = Apple()
        self.snake = Snake()

    def draw_grid(self):
        # draw vertical lines
        for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGRAY,
                             (x, 0), (x, Config.WINDOW_HEIGHT))
        # draw horizontal lines
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGRAY,
                             (0, y), (Config.WINDOW_WIDTH, y))

    def draw_snake(self):
        for coord in self.snake.snake_coords:
            x = coord['x'] * Config.CELLSIZE
            y = coord['y'] * Config.CELLSIZE
            # make rectangle
            snake_rect = pygame.Rect(
                x, y, Config.CELLSIZE, Config.CELLSIZE)
            pygame.draw.rect(self.screen, Config.DARKGREEN, snake_rect)

            snake_inner_rect = pygame.Rect(
                x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8)
            pygame.draw.rect(self.screen, Config.GREEN, snake_inner_rect)

    # draw apple obj with 20x20 at random pos
    def draw_apple(self):
        x = self.apple.x * Config.CELLSIZE
        y = self.apple.y * Config.CELLSIZE
        apple_rect = pygame.Rect(
            x, y, Config.CELLSIZE, Config.CELLSIZE)
        pygame.draw.rect(self.screen, Config.RED, apple_rect)

    # draw a score at top right
    def draw_score(self, score):
        score_surf = self.BASICFONT.render(
            'Score: %s' % (score), True, Config.WHITE)
        score_rect = score_surf.get_rect()
        score_rect.topleft = (Config.WINDOW_WIDTH - 120, 10)
        self.screen.blit(score_surf, score_rect)

    # helper function
    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        # draw grid, snake, apple, score
        self.draw_grid()
        self.draw_snake()
        self.draw_apple()
        self.draw_score(len(self.snake.snake_coords) - 3)
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def handle_key_events(self, event):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction != self.snake.RIGHT:
            self.snake.direction = self.snake.LEFT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction != self.snake.LEFT:
            self.snake.direction = self.snake.RIGHT
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
            self.snake.direction = self.snake.UP
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != self.snake.UP:
            self.snake.direction = self.snake.DOWN
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()

    def check_key_press(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()

        key_up_event = pygame.event.get(pygame.KEYUP)

        if len(key_up_event) == 0:
            return None
        if key_up_event[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        return key_up_event[0].key

    def reset_game(self):
        del self.snake
        del self.apple
        self.snake = Snake()
        self.apple = Apple()

        return True

    def is_gameover(self):
        if (self.snake.snake_coords[self.snake.HEAD]['x'] == -1 or
            self.snake.snake_coords[self.snake.HEAD]['x'] == Config.CELLWIDTH or
            self.snake.snake_coords[self.snake.HEAD]['y'] == -1 or
                self.snake.snake_coords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
            return self.reset_game()

        for snake_body in self.snake.snake_coords[1:]:
            if snake_body['x'] == self.snake.snake_coords[self.snake.HEAD]['x'] and snake_body['y'] == self.snake.snake_coords[self.snake.HEAD]['y']:
                return self.reset_game()

    def draw_preskey_msg(self):
        press_key_surf = self.BASICFONT.render(
            'Press a key to start over', True, Config.DARKGRAY)
        press_key_rect = press_key_surf.get_rect()
        press_key_rect.midtop = (Config.WINDOW_WIDTH / 2,
                                 Config.WINDOW_HEIGHT - 100)
        self.screen.blit(press_key_surf, press_key_rect)

    # draw "game over" msg in the middle with fontsize 80, at 200px pos
    def display_gameover(self):
        game_over_font = pygame.font.Font('freesansbold.ttf', 80)
        game_over_surf = game_over_font.render(
            'Game Over', True, Config.WHITE, Config.RED)

        game_over_rect = game_over_surf.get_rect()
        game_over_rect.midtop = (Config.WINDOW_WIDTH / 2, 200)
        self.screen.blit(game_over_surf, game_over_rect)

        self.draw_preskey_msg()
        pygame.display.update()
        pygame.time.wait(500)
        # clear out any key presses in the event queue
        self.check_key_press()
        while True:
            if self.check_key_press():
                # clear event queue
                pygame.event.get()
                return

    def show_presskey(self):
        press_Key_surf = self.BASICFONT.render(
            'Press a key to play', True, Config.WHITE)
        press_key_rect = press_Key_surf.get_rect()
        press_key_rect.midtop = (
            Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2)
        self.screen.blit(press_Key_surf, press_key_rect)

    def display_startscreen(self):
        start_font = pygame.font.Font('freesansbold.ttf', 40)
        start_surf = start_font.render(
            'Start Snake Game!', True, Config.WHITE, Config.DARKGRAY)

        start_rect = start_surf.get_rect()
        start_rect.midtop = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 4)
        self.screen.blit(start_surf, start_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
            self.screen.fill(Config.BG_COLOR)
            self.screen.blit(start_surf, start_rect)

            self.show_presskey()

            pygame.display.update()
            self.clock.tick(Config.MENU_FPS)

    def run(self):
        self.display_startscreen()

        while True:
            self.game_loop()
            self.display_gameover()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_events(event)

            self.snake.update(self.apple)
            self.draw()
            if self.is_gameover():
                break
