from config import Config
import random


class Snake():
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD = 0

    def __init__(self):
        self.x = random.randint(5, Config.CELLWIDTH - 6)
        self.y = random.randint(5, Config.CELLHEIGHT - 6)
        self.direction = self.RIGHT
        self.snake_coords = [{'x': self.x,     'y': self.y},
                             {'x': self.x - 1, 'y': self.y},
                             {'x': self.x - 2, 'y': self.y}]

    def update(self, apple):
        # check if snake has eaten an apply
        if self.snake_coords[self.HEAD]['x'] == apple.x and self.snake_coords[self.HEAD]['y'] == apple.y:
            apple.set_new_location()
        else:
            # remove snake's tail segment
            del self.snake_coords[-1]

        # move the snake by adding a segment in the direction it is moving
        if self.direction == self.UP:
            new_head = {'x': self.snake_coords[self.HEAD]['x'],
                        'y': self.snake_coords[self.HEAD]['y'] - 1}

        elif self.direction == self.DOWN:
            new_head = {'x': self.snake_coords[self.HEAD]['x'],
                        'y': self.snake_coords[self.HEAD]['y'] + 1}

        elif self.direction == self.LEFT:
            new_head = {'x': self.snake_coords[self.HEAD]['x'] - 1,
                        'y': self.snake_coords[self.HEAD]['y']}

        elif self.direction == self.RIGHT:
            new_head = {'x': self.snake_coords[self.HEAD]['x'] + 1,
                        'y': self.snake_coords[self.HEAD]['y']}

        self.snake_coords.insert(0, new_head)
