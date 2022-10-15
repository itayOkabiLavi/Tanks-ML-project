
import pygame
import random

from utils.Game import Game, Point
from utils.Game import DARK_GREEN, DARK_GRAY, GAME_SPEED
from utils.Tank import Tank, Direction
from utils.Collectable import Item
from utils.Collectable import SIZE as item_size


SPRITE_SIZE = 20
TANK_H = 60

class TrainingZoneGame(Game):
    def __init__(self, background_image_path, height, width) -> None:
        self.height = height
        self.width = width
        super().__init__(self.width, self.height)
        
        self.background = pygame.image.load(background_image_path)
        pygame.transform.scale(self.background, (self.width, self.height))
        
        print("setting tank.")
        self.tank = Tank("t1", DARK_GREEN, TANK_H, Point(width // 2, height // 2),
                         0, TANK_H)
        self._place_item()
        
        self.keydown_conv = {
            pygame.K_DOWN: (lambda : self.tank.move(1, False)),
            pygame.K_UP: (lambda : self.tank.move(1)),
            pygame.K_LEFT: (lambda : self.tank.rotate(1, False)),
            pygame.K_RIGHT: (lambda : self.tank.rotate(1)),
            pygame.K_a: (lambda : self.tank.rotate_turret(1, False)),
            pygame.K_d: (lambda : self.tank.rotate_turret(1))
        }
        
    def _place_item(self):
        x = random.randint(0 + item_size, self.width - item_size)
        y = random.randint(0 + item_size, self.height - item_size)
        self.item = Item(Point(x, y))
        
    def _render(self):
        self.display.blit(self.background, (0, 0))
        
        self.tank.render(self.display)
        self.item.render(self.display)
        
        pygame.display.flip()
    
    def _action(self, event):
        if event.key in self.keydown_conv:
            self.keydown_conv[event.key]()   
    
    def play_round(self):
        finish = False
        # move tank
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                self._action(event)
        
        # game over?
        if self._fail():
            finish = True
            return finish, self.tank.score
        
        if self.tank.rect.colliderect(self.item.rect):
            self.tank.score += self.item.price()
            self._place_item()
        
        # game not over, render.
        self._render()
        
        self.clock.tick(GAME_SPEED)
        
        return finish, self.tank.score
        
    def _fail(self):
        tank_center = self.tank.center
        return tank_center.x < 0 or tank_center.x > self.width\
            or tank_center.y < 0 or tank_center.y > self.height
        