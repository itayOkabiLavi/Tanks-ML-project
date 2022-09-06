from Tank import Tank

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
        self._tanks.append(Tank(tank))
    
    def add_turn(self, turn:dict):
        if not self._frames:
            raise Exception("Frames list is empty. create a new frame")
        self._frames[-1].append(str(turn).replace("'", '"'))
    
    def new_frame(self, frame:list):
        if frame is None:
            self._frames.append([])
        else:
            self._frames.append(frame)
    
    def get_tank_dict(self,
                      _id,
                        xpos,
                        ypos,
                        size,
                        rot,
                        color_rot,
                        tursize,
                        tur_rot):
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
    
    def get_description(self):
        iddesc = "{}\n".format(self._battleId)
        tanks = ""
        for tank in self._tanks:
            tanks += tank + "\n"
        separator = "g\n"
        return "{}{}{}".format(iddesc, tanks, separator)
    
    def save(self, folder):
        with open(folder + "/" + self._filename, 'w') as f:
            f.write(self.get_description())