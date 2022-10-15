
import pygame
import numpy as np
from enum import Enum
from utils.Game import DARK_GREEN, Point

class Direction(Enum):
    DOWN = 0
    RIGHT = 90
    UP = 180
    LEFT = 270
    
TANK_IMAGE = pygame.image.load("C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/tank-body.png")
TURRET_IMAGE = pygame.image.load("C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/tank-turret.png")
    
TANK_H2W = 1 / 2
TURRET_H2W = 1 / 3

class Tank:
    def __init__(self, id, color,
                 size: int, position: Point, angle,
                 turret_size: int) -> None:
        self.id = id
        
        self.set_dimentions(size, angle)
        self.set_position(position)
        self.set_game_properties(color)

        self.turret = Turret(turret_size, self.center, angle, self.color)
        self.turret.rotate_along(angle)
        
        
    def set_game_properties(self, color):
        self.max_pixels_pt = 1000 / self.height
        self.max_degrees_pt = 10
        self.color = color
        self.score = 0
        
        
    def set_dimentions(self, size, angle):
        self.height = size
        self.width = int(size * TANK_H2W)
        self.angle = angle
        self.rad_angle = np.deg2rad(angle)
        
        self.image = pygame.transform.scale(TANK_IMAGE, (self.width, self.height))
        self.body = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.body.get_rect()
    
    
    def set_position(self, position: Point):
        position = Point(int(position.x), int(position.y))
        self.center = position
        self.topleft = Point(
            position.x - (self.width // 2),
            position.y - (self.height // 2)
        )
    
    
    def move(self, power: float, forward=True):
        if 0 <= power <= 1:
            d = power * self.max_pixels_pt
            x_step = d * np.sin(self.rad_angle)
            y_step = d * np.cos(self.rad_angle)
            if forward:
                new_center = Point(
                    self.center.x - x_step,
                    self.center.y - y_step
                )
            else:
                new_center = Point(
                    self.center.x + x_step,
                    self.center.y + y_step
                )
            self.set_position(new_center)
            self.turret.set_position(new_center)
        else:
            raise TankError("Tank {}\tgas-power isn't in [0,1] : {}"
                            .format(self.id, power))
    
    
    def rotate(self, power: float, to_right=True):
        if 0 <= power <= 1:
            d = power * self.max_degrees_pt
            if to_right:
                d = -1 * d
            self.angle += d
            
            self.rad_angle = np.deg2rad(self.angle)
            self.body = pygame.transform.rotate(self.image, self.angle)
            
            self.turret.rotate_along(d)
        else:
            raise TankError("Tank {}\tAngle isn't in [0,1] : {}"
                            .format(self.id, power))
        
        
    def rotate_turret(self, power, to_right=True):
        self.turret.rotate(power, to_right)
    
    def get_center(self):
        return self.center
        
    def render(self, display: pygame.Surface):
        self.rect = self.body.get_rect(center=self.image.get_rect(topleft=self.topleft).center)
        # pygame.draw.rect(display, DARK_GREEN, self.rect)
        display.blit(self.body, self.rect)
        self.turret.render(display)


class Turret():
    def __init__(self, size, position: Point, angle, color) -> None:
        self.height = size
        self.width = int(self.height * TURRET_H2W)
        self.max_degrees_pt = 10
        self.set_position(position)
        
        self.image = pygame.transform.scale(TURRET_IMAGE, (self.width, self.height))
        self.color = color
        self.angle = 0
        self.rotate_along(angle)
        
        
    def set_position(self, center_position: Point):
        self.center = center_position
        self.topleft = Point(
            center_position.x - (self.width // 2),
            center_position.y - (self.height // 2)
        )
        
    
    def rotate_along(self, add_angle):
        self.angle += add_angle
        self.rad_angle = np.deg2rad(self.angle)
        self.body = pygame.transform.rotate(self.image, self.angle)
    
        
    def rotate(self, power: float, to_right=True):
        if 0 <= power <= 1:
            d = power * self.max_degrees_pt
            if to_right:
                d = -1 * d
            self.angle += d
            self.rad_angle = np.deg2rad(self.angle)
            self.body = pygame.transform.rotate(self.image, self.angle)
            
        else:
            raise TurretError("Turret\tAngle isn't in [0,1] : {}"
                            .format(power))
            
    
    def render(self, display: pygame.Surface):
        self.rect = self.body.get_rect(center=self.image.get_rect(topleft=self.topleft).center)
        display.blit(self.body, self.rect)

class TankError(Exception):
    pass

class TurretError(Exception):
    pass