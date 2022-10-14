
import pygame
import random

from utils.Game import Game, Point
from utils.Game import DARK_GREEN, DARK_GRAY, GAME_SPEED
from utils.Tank import Tank, Direction
from utils.Collectable import Item
from utils.Collectable import SIZE as item_size


SPRITE_SIZE = 20
TANK_H = 30
TANK_W = TANK_H // 2

keydown_conv = {
    pygame.K_DOWN: Direction.DOWN.value,
    pygame.K_UP: Direction.UP.value,
    pygame.K_LEFT: Direction.LEFT.value,
    pygame.K_RIGHT: Direction.RIGHT.value
}

class TrainingZoneGame(Game):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
        
        self.tank = Tank(TANK_H, TANK_W, Point(width // 2, height // 2), DARK_GREEN)
        self._place_item()
        
    def _place_item(self):
        x = random.randint(0 + item_size, self.width - item_size)
        y = random.randint(0 + item_size, self.height - item_size)
        self.item = Item(Point(x, y))
        
    def _render(self):
        self.display.fill(DARK_GRAY)
        
        self.tank.render(self.display)
        self.item.render(self.display)
        
        pygame.display.flip()
    
    def play_round(self):
        finish = False
        # move tank
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in keydown_conv:
                    self.tank.move(keydown_conv[event.key])
        
        # game over?
        if self._fail():
            finish = True
            return finish, self.tank.score
        
        if self.tank.rect.colliderect(self.item.rect):
            self.tank.score += 10
            self._place_item()
        
        # game not over, render.
        self._render()
        
        self.clock.tick(GAME_SPEED)
        
        return finish, self.tank.score
        
    def _fail(self):
        tank_center = self.tank.center
        return tank_center.x < 0 or tank_center.x > self.width\
            or tank_center.y < 0 or tank_center.y > self.height
        