from turtle import pos
import pygame

from utils.Game import Point

SIZE = 10
COLOR = (200, 200, 0)
PRICE = 10

class Item:
    def __init__(self, position: Point) -> None:
        self.pos = position
        self.rect = pygame.Rect(position.x - SIZE // 2, 
                                position.y - SIZE // 2,
                                SIZE,
                                SIZE)
        
    def render(self, display):
        pygame.draw.rect(display, COLOR, self.rect)
        
    def price(self):
        return PRICE