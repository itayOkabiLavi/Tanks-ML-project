from BattleLogger import BattleLogger
from Tank import get_tank_dict
from Tank import Tank

import os

save_to_folder = os.path.join(os.getcwd(), "algorithms", "output")
bg = BattleLogger(1)

tanks = {}
for i in range(12):
    tanks[i] = Tank(get_tank_dict(i, (i+1)*50, 50, (i * 4 / 11) + 5, 0, 10 * i, 0, 0))
    bg.add_tank(tanks[i].get_details())

for i in range(20):
    bg.new_frame()
    bg.add_turn(tanks[1].forwards())
print("Output file is ready.")
bg.save(save_to_folder)