import math
from Bullet import Bullet

MAX_SIZE = 13
MIN_SIZE = 2
SPD_FACTOR = 14

MAX_HP = 100

UPPER_TUR_SIZE = 100
LOWER_TUR_SIZE = 1

MAX_Y = 200
MAX_X = 400
MIN_Y = 0
MIN_X = 0

class Tank:
    _details: dict
    _id: int
    _hp: int
    _moral: int
    
    _xpos: int
    _ypos: int
    _xstep: float
    _ystep: float
    _angle: float
    
    _size: float
    _step: float
    _color_rot: float
    
    _tursize: float
    _tur_angle: float
    _tur_rot_step: float
    
    def __init__(self, details:dict) -> None:
        self._id = details['_id']
        # body
        self._xpos = details['xpos']
        self._ypos = details['ypos']
        self._size = details['size']
        
        if self._size < MIN_SIZE or self._size > MAX_SIZE:
            raise ValueError("Tank size must be in range [{},{}]. ({})"
                             .format(MIN_SIZE, MAX_SIZE, str(self._id)))
        
        self._step = 7 * (1 - (self._size / SPD_FACTOR))
        self.set_angle(details['rot'])
                
        # turret
        self._tursize = details['tursize']
        trs = (1 - (self._tursize / SPD_FACTOR))
        self._tur_rot_step = 15 * trs * trs
        self._tur_angle = details['tur_rot']
        self._color_rot = details['color_rot']
        
        # total details
        self.details = details
    
    def forwards(self):
        # TODO: if < MIN or > MAX kill (or damage severly enough) tank
        self._xpos += self._xstep
        self._ypos += self._ystep
        return self.turn_log()
    
    def backwards(self):
        self._xpos -= self._xstep
        self._ypos -= self._ystep
        return self.turn_log()
    
    def rotate(self, left:bool=False):
        if left:
            self.set_angle(self._angle - self._step)
        else:
            self.set_angle(self._angle + self._step)
        return self.turn_log()
    
    def rotate_turret(self, left:bool=False):
        if left:
            self._tur_angle -= self._tur_rot_step
        else:
            self._tur_angle += self._tur_rot_step
        return self.turn_log()
    
    def shoot(self, add_to_env, bullet_id):
        bullet = Bullet(
            bullet_id,
            self._xpos,
            self._ypos,
            self._angle + self._tur_angle,
            self._tursize
            )
        add_to_env(bullet)
        return bullet.creation_log()
    
    def got_hit(self):
        pass
    
    def set_angle(self, angle:float):
        self._angle = angle
        self._ystep = self._step * math.cos(math.radians(angle))
        self._xstep = self._step * math.sin(math.radians(angle))
        # print(self._angle, self._step, self._xstep, self._ystep)
    
    def turn_log(self):
        return [
            self._id,
            float(format(self._xpos, '.3f')),
            float(format(self._ypos, '.3f')),
            float(format(self._angle, '.3f')),
            float(format(self._tur_angle, '.3f'))
        ]
    
    def get_details(self):
        return self.details
    
    def __repr__(self) -> str:
        return self.__str__()    
        
    def __str__(self) -> str:
        return str(self.details).replace("'", '"')
    
    def move(self)->str:
        # make decision here
        return ""

def get_tank_dict(_id, xpos, ypos, size, rot, color_rot, tursize, tur_rot):
        return {
            '_id': _id,
            'xpos': xpos,
            'ypos': ypos,
            'size': size,
            'rot': rot,
            'color_rot': color_rot,
            'tursize': tursize,
            'tur_rot': tur_rot
        }
        
class TankAction:
    pass