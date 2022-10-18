import pygame
from collections import namedtuple

# colors
DARK_GREEN = (5, 150, 5)
DARK_GRAY = (50, 50, 50)

# performance
GAME_SPEED = 40

Point = namedtuple('Point', 'x, y')


class Game:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.start_pygame()
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        
    def start_pygame(self):
        pygame.init()
    
        
    def end_pygame(self):
        pygame.quit()
        quit()
    
        
    def play_round(self):
        pass
    
    
    def render_display(self):
        pass
    