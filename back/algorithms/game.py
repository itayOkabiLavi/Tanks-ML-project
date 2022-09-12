from BattleLogger import BattleLogger
from Tank import get_tank_dict
from Tank import Tank

import os

import Bullet

save_to_folder = os.path.join(os.getcwd(), "algorithms", "output")
bg = BattleLogger(1)

tanks = [
    Tank(get_tank_dict(0, 50, 50, 5, 0, 0, 5, 0)),
    Tank(get_tank_dict(1, 150, 50, 7, 45, 90, 7, 0)),
    Tank(get_tank_dict(2, 250, 50, 9, 90, 180, 9, 0)),
    ]

bullets = []

bullet_id = 0

for tank in tanks:
    bg.add_tank(tank)

for i in range(20):
    bg.new_frame()
    for tank in tanks:
        bg.add_turn(tank.forwards())

for i in range(20):
    bg.new_frame()
    for tank in tanks:
        bg.add_turn(tank.rotate())
        
for i in range(1):
    bg.new_frame()
    for tank in tanks:
        bg.add_turn(tank.shoot(bullets.append, bullet_id))
        bullet_id += 1

for i in range(Bullet.RANGE//Bullet.SPEED):
    bg.new_frame()
    for bullet in bullets:
        bg.add_turn(bullet.move())
    
        
print("Output file is ready.")
bg.save(save_to_folder)