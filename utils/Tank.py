
import pygame
import numpy as np
from enum import Enum
from utils.Game import Point

class Direction(Enum):
    DOWN = 0
    RIGHT = 90
    UP = 180
    LEFT = 270

class Tank:
    def __init__(self, height, width, position: Point, color) -> None:
        self.h = height
        self.w = width
        
        self.speed = (1.0 / (self.w * self.h)) * 5000
        
        self.set_position(position)
        self.color = color
        
        self.score = 0
        
    def set_position(self, position: Point):
        self.center = position
        self.pos = Point(
            position.x - (self.w // 2),
            position.y - (self.h // 2)
        )
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.w, self.h)
        
    def move(self, direction: int):
        rad = np.deg2rad(direction)
        x_step = int(np.sin(rad)) * self.speed
        y_step = int(np.cos(rad)) * self.speed
        self.set_position(Point(
            self.center.x + x_step,
            self.center.y + y_step
        ))
    
    def get_center(self):
        return self.center
        
    def render(self, display):
        pygame.draw.rect(display, self.color, self.rect)