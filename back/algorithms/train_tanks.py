from BattleLogger import BattleLogger
from Tank import get_tank_dict
from Tank import Tank

import os

save_to_folder = os.path.join(os.getcwd(), "algorithms", "output")
bg = BattleLogger(1)

tanks = {
    0: Tank(get_tank_dict(0, 50, 50, 5, 0, 0, 5, 0)),
    1: Tank(get_tank_dict(1, 150, 50, 7, 45, 90, 7, 0)),
    2: Tank(get_tank_dict(2, 250, 50, 9, 90, 180, 9, 0)),
    }

for key in tanks:
    bg.add_tank(tanks[key])

for i in range(20):
    bg.new_frame()
    for key in tanks:
        bg.add_turn(tanks[key].forwards())

for i in range(20):
    bg.new_frame()
    for key in tanks:
        bg.add_turn(tanks[key].rotate())
        
for i in range(20):
    bg.new_frame()
    for key in tanks:
        bg.add_turn(tanks[key].rotate_turret())
        
print("Output file is ready.")
bg.save(save_to_folder)