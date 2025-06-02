import pygame
import random
from config import RED, SNAKE_BLOCK, SCREEN_WIDTH, SCREEN_HEIGHT

class Apple:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(0, SCREEN_WIDTH, SNAKE_BLOCK)
        y = random.randrange(0, SCREEN_HEIGHT, SNAKE_BLOCK)
        return [x, y]

    def draw(self, win):
        pygame.draw.rect(win, RED, [self.position[0], self.position[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def relocate(self):
        self.position = self.random_position()