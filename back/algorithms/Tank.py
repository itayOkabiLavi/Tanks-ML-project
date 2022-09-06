import math


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
    _tur_rot: float
    _tur_rot_step: float
    
    def __init__(self, details:dict) -> None:
        self._id = details['_id']
        self._xpos = details['xpos']
        self._ypos = details['ypos']
        
        self._size = details['size']
        self._step = 1 - self._size
        
        self.set_angle(details['rot'])
        
        self._color_rot = details['color_rot']
        self._tursize = details['tursize']
        self._tur_rot = details['tur_rot']
        self.details = details
    
    def forwards(self):
        self._xpos += self._xstep
        self._ypos += self._ystep
        return self.turn_dict()
    
    def backwards(self):
        self._xpos -= self._xstep
        self._ypos -= self._ystep
        return self.turn_dict()
    
    def rotate(self, left:bool):
        if left:
            self._tur_rot -= self._tur_rot_step
        else:
            self._tur_rot += self._tur_rot_step
        return self.turn_dict()
    
    def shoot(self):
        pass
    
    def got_hit(self):
        pass
    
    def set_angle(self, angle:int):
        self._angle = angle
        self._xstep = self._step * math.cos(angle)
        self._ystep = self._step * math.sin(angle)
    
    def turn_dict(self):
        return {
            '_id': self._id,
            'xpos': self._xpos,
            'ypos': self._ypos,
            'rot': self._angle,
            'tur_rot': self._tur_rot
        }
    
    def __repr__(self) -> str:
        return self.__str__()    
        
    def __str__(self) -> str:
        return str(self.details).replace("'", '"')
        