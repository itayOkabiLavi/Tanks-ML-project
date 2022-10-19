
import pygame
import random

from utils.Game import Game, Point
from utils.Game import DARK_GREEN, DARK_GRAY, GAME_SPEED
from utils.Tank import Tank, Direction
from utils.Item import BOMB_DAMAGE, BOMB_VALUE, COIN_VALUE, Item, COIN, BOMB, Target
from utils.Item import SIZE as item_size


SPRITE_SIZE = 20
TANK_H = 60
HEIGHT = 500
ZONE_WIDTH = 700
ZONE_IMAGE = "C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/bg-sand.jpg"

STAT_SCREEN_WIDTH = 200

TITLE_SIZE = 20
LINE_SPACE = 5
TITLE_LEFT_MARGIN = 10 + ZONE_WIDTH
TEXT_LEFT_MARGIN = 150 + ZONE_WIDTH


class TrainingZoneGameByHand(Game):
    def __init__(self, background_image_path=ZONE_IMAGE) -> None:
        self.height = HEIGHT
        self.width = ZONE_WIDTH + STAT_SCREEN_WIDTH
        super().__init__(self.width, self.height)
        
        self.zone = pygame.image.load(background_image_path)
        pygame.transform.scale(self.zone, (ZONE_WIDTH, HEIGHT))
        self.stat_screen = pygame.Rect(ZONE_WIDTH, 0, STAT_SCREEN_WIDTH, HEIGHT)
        
        
        print("setting tank.")
        self.tank = Tank("t1", DARK_GREEN, TANK_H, Point(self.width // 2, self.height // 2),
                         0, TANK_H, 100, self)
        
        self.total_bombs = 1
        self.total_coins = 4
        
        self.coins_collected = 0
        self.bombs_destroyed = 0
        self.bombs_activated = 0
        
        self.bombs = []
        self.coins = []
        
        self._place_coins()
        self._place_bombs()
        
        self.bullets = []
        
        self.actions_conv = {
            pygame.K_DOWN: (lambda : self.tank.move(1, False)),
            pygame.K_UP: (lambda : self.tank.move(1)),
            pygame.K_LEFT: (lambda : self.tank.rotate(1, False)),
            pygame.K_RIGHT: (lambda : self.tank.rotate(1)),
            pygame.K_a: (lambda : self.tank.rotate_turret(1, False)),
            pygame.K_d: (lambda : self.tank.rotate_turret(1)),
            pygame.K_SPACE: (lambda : self.tank.shoot())
        }
        
        self.title_font = pygame.font.Font(None, TITLE_SIZE)
        self.text_font = pygame.font.Font(None, int(TITLE_SIZE * 0.75))
        
        
    def _place_coins(self):
        missing = self.total_coins - len(self.coins)
        if missing > 0:
            print("adding {} coins".format(missing))
            for i in range(missing):
                x = random.randint(0 + item_size, ZONE_WIDTH - item_size)
                y = random.randint(0 + item_size, HEIGHT - item_size)
                self.coins.append(Item(Point(x, y), COIN_VALUE, self.display, COIN))
        
    def _place_bombs(self):
        missing = self.total_bombs - len(self.bombs)
        if missing > 0:
            print("adding {} bombs".format(missing))
            for i in range(missing):
                x = random.randint(0 + item_size, ZONE_WIDTH - item_size)
                y = random.randint(0 + item_size, HEIGHT - item_size)
                self.bombs.append(Target(Point(x, y), BOMB_VALUE, BOMB_DAMAGE, self.display, BOMB))
        
    
    # true if a collision should cause failing
    def _tank_collisions(self, tank: Tank):
        temp_list = self.bombs.copy()
        if not self.zone.get_rect().contains(tank.rect):
            return True
        for bomb in temp_list:
            if tank.rect.colliderect(bomb.rect):
                tank.score -= bomb.get_value()
                tank.armor -= bomb.get_damage()
                self.bombs.remove(bomb)
                self.bombs_activated += 1
                if tank.armor <= 0:
                    return True
        self._place_bombs()
        
        temp_list = self.coins.copy()
        for coin in temp_list:
            if tank.rect.colliderect(coin.rect):
                tank.score += coin.get_value()
                self.coins_collected += 1
                self.coins.remove(coin)
        self._place_coins()
        return False
        
    def _render(self):
        self._render_display()
        for bullet in self.bullets:
            bullet.render()
        self.tank.render()
        for coin in self.coins:
            coin.render()
        for bomb in self.bombs:
            bomb.render()
        pygame.display.flip()
    
    
    def _action(self, event):
        if event.key in self.actions_conv:
            self.actions_conv[event.key]()   
    
    
    def _render_display(self) -> int:
        self.display.blit(self.zone, (0, 0))
        pygame.draw.rect(self.display, (10, 0, 0), self.stat_screen)
        
        def _draw_line(title: bytes, value: str ,y_pos):
            title = self.title_font.render(title, True, (255, 255, 255))
            value = self.title_font.render(bytes(value, 'utf-8'), True, (255, 255, 255))
            self.display.blit(title, (TITLE_LEFT_MARGIN, y_pos))
            self.display.blit(value, (TEXT_LEFT_MARGIN, y_pos))    
            y_pos += TITLE_SIZE + LINE_SPACE
            return y_pos
        
        line_pointer = LINE_SPACE
        line_pointer = _draw_line(b"Tank ID:", str(self.tank.id), line_pointer)
        line_pointer = _draw_line(b"Armor:", str(self.tank.armor), line_pointer)
        line_pointer = _draw_line(b"Coins Collected:", str(self.coins_collected), line_pointer)
        line_pointer = _draw_line(b"Bombs Destroyed:", str(self.bombs_destroyed), line_pointer)
        line_pointer = _draw_line(b"Bombs Activated:", str(self.bombs_activated), line_pointer)
        line_pointer = _draw_line(b"Total Score:", str(self.tank.score), line_pointer)
        
        return line_pointer
        
    
    def _bullets_collisions(self):
        temp_bullets = self.bullets.copy()
        for bullet in temp_bullets:
            bullet.move()
            temp_bombs = self.bombs.copy()
            for bomb in temp_bombs:
                if bullet.rect.colliderect(bomb.rect):
                    self.bullets.remove(bullet)
                    self.bombs.remove(bomb)
                    bullet.parent.score += bomb.get_value()
                    self.bombs_destroyed += 1
                    break
    
    
    def play_round(self):
        # move tank
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_pygame()
            if event.type == pygame.KEYDOWN:
                self._action(event)
        
        self._bullets_collisions()
        # game not over, render.
        self._render()
        
        self.clock.tick(GAME_SPEED)
        
        return self._tank_collisions(self.tank), self.tank.score
            
    