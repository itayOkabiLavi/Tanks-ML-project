
from algorithms.BattleLogger import BattleLogger
from Tank import Tank
from algorithms.Bullet import Bullet

# defines the "physical" dimentions of the game. not dealing with frames and time.
class Environment:
    
    def __init__(self, gameId:int, maxx:int, maxy:int, minx=0, miny=0) -> None:
        self.MAXX = maxx
        self.MAXY = maxy
        self.MINX = minx
        self.MINY = miny
        self.tanks = []
        self.bullets = []
        self.run = True
        
        self.gameId = gameId
        self.logger = BattleLogger(gameId)
        
        # ARRAY OF BOARD? to make collision easier
    
    def add_tank(self, tank:Tank):
        self.logger.add_tank(tank)
        self.tanks.append(tank)
        
    def add_bullet(self, bullet:Bullet):
        self.bullets.append(bullet)
        # NO NEED FOR LOGGER. it will be notified as the bullet moves.
        # logger doesn't need to know about bullets at all.
        
    def one_round(self):
        for tank in self.tanks:
            tank.move()
        for bullet in self.bullets:
            bullet.move()