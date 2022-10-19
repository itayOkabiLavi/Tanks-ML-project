
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

BULLET_PIXELS_PT = 10

class Tank:
    def __init__(self, id, color,
                 size: int, position: Point, angle,
                 turret_size: int, shoot_range: int,
                 game) -> None:
        self.game = game
        self.id = id
        
        self.set_dimentions(size, angle)
        self.set_position(position)
        self.set_game_properties(color)

        self.turret = Turret(turret_size, self.center, angle, self.color, self.game.display)
        self.turret.rotate_along(angle)
        
        self.range = shoot_range

        
    def set_game_properties(self, color):
        self.max_pixels_pt = 1000 / self.height
        self.max_degrees_pt = 10
        self.color = color
        self.score = 0
        self.armor = 100
        
        
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
            self.angle = self.angle % 360
            self.rad_angle = np.deg2rad(self.angle)
            self.body = pygame.transform.rotate(self.image, self.angle)
            
            self.turret.rotate_along(d)
        else:
            raise TankError("Tank {}\tAngle isn't in [0,1] : {}"
                            .format(self.id, power))
        
        
    def rotate_turret(self, power, to_right=True):
        self.turret.rotate(power, to_right)
    
    
    def shoot(self):
        # print("shooting")
        self.game.bullets.append(
            Bullet(self, self.color, self.turret.height // 10, self.turret.angle, self.center, self.game)
        )
    
    
    def get_center(self):
        return self.center
    
        
    def render(self):
        pygame.draw.circle(self.game.display, self.color, self.center, self.range + 2.5, width=5)
        
        self.rect = self.body.get_rect(center=self.image.get_rect(topleft=self.topleft).center)
        # pygame.draw.rect(display, DARK_GREEN, self.rect)
        self.game.display.blit(self.body, self.rect)
        
        self.turret.render()


class Turret():
    def __init__(self, size, position: Point, angle, color, display) -> None:
        self.display = display
        
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
            self.angle = self.angle % 360
            self.rad_angle = np.deg2rad(self.angle)
            self.body = pygame.transform.rotate(self.image, self.angle)
            
        else:
            raise TurretError("Turret\tAngle isn't in [0,1] : {}"
                            .format(power))
    
    def render(self):
        self.rect = self.body.get_rect(center=self.image.get_rect(topleft=self.topleft).center)
        self.display.blit(self.body, self.rect)



class Bullet:
    def __init__(self, parent: Tank, color, diameter, angle, start_position:Point, game) -> None:
        self.game = game
        self.parent = parent
        
        self.color = color
        self.size = diameter
        self.set_position(start_position)
        self.distance = self.parent.range
        self.steps_remained = self.distance // BULLET_PIXELS_PT
        
        self.rad_angle = np.deg2rad(angle)
        self.x_step = BULLET_PIXELS_PT * np.sin(self.rad_angle)
        self.y_step = BULLET_PIXELS_PT * np.cos(self.rad_angle)
        
        # print("created bullet at {}.".format(start_position))
        
        
    def set_position(self, center):
        self.center = center
        self.topleft = Point(
            self.center.x - (self.size // 2),
            self.center.y - (self.size // 2)
        )
        self.rect = pygame.Rect(self.topleft, (self.size, self.size))
    
    def move(self):
        if self.steps_remained > 0:
            new_x = self.center.x - self.x_step
            new_y = self.center.y - self.y_step
            self.set_position(Point(new_x, new_y))
            # print(new_x, new_y)
            self.steps_remained -= 1
        else:
            self.destroy_self()
            
    def destroy_self(self):
        self.game.bullets.remove(self)
    
    def get_parent(self):
        return self.parent
    
    def render(self):
        pygame.draw.rect(self.game.display, self.color, self.rect)
        pygame.draw.circle(self.game.display, self.color, self.center, self.size // 2)
        
        

class TankError(Exception):
    pass

class TurretError(Exception):
    pass