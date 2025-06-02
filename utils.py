import pygame

def draw_text(win, text, x, y, color):
    font = pygame.font.SysFont("comicsansms", 25)
    surface = font.render(text, True, color)
    win.blit(surface, (x, y))
