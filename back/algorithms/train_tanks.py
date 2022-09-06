from BattleLogger import BattleLogger
import os
save_to_folder = os.path.join(os.getcwd(), "algorithms", "output")
print(save_to_folder)
bg = BattleLogger(1)

bg.add_tank(bg.get_tank_dict(1,50,100,0.5,0,0,0.5,0))
bg.add_tank(bg.get_tank_dict(2,50,100,1,180,90,1,0))

bg.new_frame([])
bg.add_turn()
bg.save(save_to_folder)