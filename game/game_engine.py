import pygame
from config import *
from snake import Snake
from .apple import Apple
from utils import draw_text

class GameEngine:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.apple = Apple()
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.running = True
        self.score = 0

    def reset(self):
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction("RIGHT")

            self.snake.move()

            head = self.snake.get_head_position()
            #if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
                #self.reset()

            if self.snake.check_collision():
                self.reset()

            if head == self.apple.position:
                self.snake.grow()
                self.apple.relocate()
                self.score += 1
                # Uncomment if sound is available
            pygame.mixer.Sound(EAT_SOUND).play()

            self.win.fill(BLACK)
            self.snake.draw(self.win)
            self.apple.draw(self.win)
            draw_text(self.win, f"Score: {self.score}", 10, 10, WHITE)
            pygame.display.update()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()


