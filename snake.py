import pygame
from config import GREEN, SNAKE_BLOCK, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    def __init__(self):
        self.body = [[300, 200]]
        self.direction = "RIGHT"
        self.grow_flag = False

    def move(self):
        head = self.body[-1].copy()

        if self.direction == "RIGHT":
            head[0] = (head[0] + SNAKE_BLOCK) % SCREEN_WIDTH
        elif self.direction == "LEFT":
            head[0] = (head[0] - SNAKE_BLOCK) % SCREEN_WIDTH
        elif self.direction == "UP":
            head[1] = (head[1] - SNAKE_BLOCK) % SCREEN_HEIGHT
        elif self.direction == "DOWN":
            head[1] = (head[1] + SNAKE_BLOCK) % SCREEN_HEIGHT

        self.body.append(head)

        if not self.grow_flag:
            self.body.pop(0)
        else:
            self.grow_flag = False

    def change_direction(self, direction):
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposites.get(self.direction):
            self.direction = direction

    def grow(self):
        self.grow_flag = True

    def draw(self, win):
        for part in self.body:
            pygame.draw.rect(win, GREEN, [part[0], part[1], SNAKE_BLOCK, SNAKE_BLOCK])

    def check_collision(self):
        head = self.body[-1]
        return head in self.body[:-1]

    def get_head_position(self):
        return self.body[-1]