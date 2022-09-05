class BattleGenerator:
    battleId: int
    filename:str
    tanks: list
    def __init__(self, _id: int) -> None:
        self.battleId = _id
        self.filename = "battle_{}.txt".format(_id)
        self.tanks = []
    
    # _id,
    # xpos,
    # ypos,
    # size,
    # rot,
    # color_rot,
    # tursize,
    # tur_rot
    def add_tank(self, tank:dict):
        self.tanks.append(
            "{"+
                "'_id': {},".format(tank['_id']) + 
                "'xpos': {},".format(tank['xpos']) + 
                "'ypos': {},".format(tank['ypos']) + 
                "'size': {},".format(tank['size']) + 
                "'rot': {},".format(tank['rot']) + 
                "'color_rot': {},".format(tank['color_rot']) + 
                "'tursize': {},".format(tank['tursize']) + 
                "'tur_rot': {},".format(tank['tur_rot']) + 
            "}"
        )
    
    
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
        iddesc = "{}\n".format(self.battleId)
        tanks = ""
        for tank in self.tanks:
            tanks += tank + "\n"
        separator = "g\n"
        return "{}{}{}".format(iddesc, tanks, separator)
    
    def save(self, folder):
        with open(folder + "/" + self.filename, 'w') as f:
            f.write(self.get_description())