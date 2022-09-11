from Tank import Tank
from algorithms.Bullet import Bullet

class BattleLogger:
    _battleId: int
    _filename:str
    _tanks: list
    _frames: list
    def __init__(self, _id: int) -> None:
        self._battleId = _id
        self._filename = "battle_{}.txt".format(_id)
        self._tanks = []
        self._frames = []
    
    # _id,
    # xpos,
    # ypos,
    # size,
    # rot,
    # color_rot,
    # tursize,
    # tur_rot
    def add_tank(self, tank:dict):
        self._tanks.append(str(tank).replace("'", '"'))
    
    def add_turn(self, turn:dict):
        self._frames[-1] += str(turn).replace("'", '"') + ';'
    
    def new_frame(self, frame:str=""):
        self._frames.append(frame)
    
    def get_description(self):
        tanks = "\n".join(self._tanks)
        frames = "\n".join(self._frames)
        separator = "g"
        return "\n".join([str(self._battleId), tanks, separator, frames])
    
    def save(self, folder):
        with open(folder + "/" + self._filename, 'w') as f:
            f.write(self.get_description())