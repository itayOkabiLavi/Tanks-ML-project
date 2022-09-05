from BattleGenerator import BattleGenerator
import os
save_to_folder = os.path.join(os.getcwd(), "algorithms", "output")
print(save_to_folder)
bg = BattleGenerator(1)
tank1 = bg.get_tank_dict(1,50,100,0.5,0,0,0.5,0)
bg.add_tank(tank1)
bg.save(save_to_folder)