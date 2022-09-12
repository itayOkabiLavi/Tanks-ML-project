import math
from sre_constants import RANGE

SPEED = 1
RANGE = 40

MAX_POWER = 9
MIN_POWER = 5
class Bullet:
    def __init__(self,
                 id,
                 xpos:float,
                 ypos:float,
                 angle:float,
                 power:float,
                 speed:float=SPEED,
                 range:float=RANGE,
                 color_rot:float=0) -> None:
        self._id = id
        self._xpos = xpos
        self._ypos = ypos
        
        self._frames = range // speed
        self._xstep = speed * math.sin(math.radians(angle)) 
        self._ystep = speed * math.cos(math.radians(angle))
        
        self._color = color_rot
        self._power = power
        self._size = MAX_POWER
    
    def creation_log(self):
        return [
            "b",
            self._id,
            self._xpos,
            self._ypos,
            self._size,
            self._color
        ]
    
    def turn_log(self):
        return [
            self._id,
            self._xpos,
            self._ypos,
            '',
            '',
        ]
    
    def move(self):
        if self._frames:
            self._xpos += self._xstep
            self._ypos += self._ystep
            self._frames -= 1
        return self.turn_log()