
import pygame

from utils.Game import Point

SIZE = 40
COIN = "C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/dogecoin.png"
BOMB = "C:/Users/hagsh/OneDrive/Desktop/Self Studies/ML/ml project/images/bomb.png"
COIN_VALUE = 10
BOMB_VALUE = 5
BOMB_DAMAGE = 50


class Item:
    def __init__(self, topleft: Point, value: int, display: pygame.Surface, image) -> None:
        self.display = display
        self.topleft = topleft
        self.value = value
        self.rect = pygame.Rect(self.topleft.x, 
                                self.topleft.y,
                                SIZE,
                                SIZE)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (SIZE, SIZE))
        
    def get_value(self):
        return self.value
    
    def render(self):
        self.display.blit(self.image, self.topleft)

class Target(Item):
    def __init__(self, topleft: Point, value: int, damage: int, display: pygame.Surface, image) -> None:
        super().__init__(topleft, value, display, image)
        self.damage = damage
        
    def get_damage(self):
        return self.damage