import os
import pygame
from ..parameters import display
from ..resource_path import resource_path, PATH

pygame.font.init()

font_type = resource_path(os.path.join('resourses', 'font', 'PingPong.ttf'))

def print_text(message, x, y, font_color = (255, 255, 255), font_type = font_type, font_size = 30):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, font_color)
    display.blit(text, (x, y))
