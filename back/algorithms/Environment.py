
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
        self.tanks = {}
        self.bullets = {}
        self.run = True
        
        self.gameId = gameId
        self.logger = BattleLogger(gameId)
        
        # ARRAY OF BOARD? to make collision easier
    
    def add_tank(self, tank:Tank):
        self.logger.add_tank(tank)
        if tank._id in self.tanks:
            raise Exception("Tank id {} already exists.".format(tank._id))
        else:
            self.tanks[tank._id] = tank
        
    def add_bullet(self, bullet:Bullet):
        if bullet._id in self.bullets:
            raise Exception("Bullet id {} already exists.".format(bullet._id))
        else:
            self.bullets[bullet._id] = bullet
        
        # NO NEED FOR LOGGER. it will be notified as the bullet moves.
        # logger doesn't need to know about bullets at all.
        
    def remove(self, item_id, type:str):
        if type == 'tank':
            self.tanks[item_id] = None
        if type == 'bullet':
            self.bullets[item_id] = None
        
    def one_round(self):
        for tid in self.tanks:
            self.tanks[tid].move(self)
        for bid in self.bullets:
            self.bullets[bid].move(self)