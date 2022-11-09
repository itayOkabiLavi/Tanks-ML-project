import torch
import numpy as np
from utils.ml_utils.FastforwardNN import FastforwardNN
from utils.ml_utils.Qtable import QTable
from utils.Tank import Tank

ACT_MOVE = 'move'
ACT_ROT = 'rotate'
ACT_TUR_ROT = 'rotate_tur'
ACT_SHT = 'shoot'
ACT_POWER = 'power'

D_ACTION = "action-type"
D_POWER = "power"
D_POSITIVE = "pos/neg"
        
        
class Agent:
    def __init__(self, nn_props:dict, q_table_props: dict) -> None:
        self.NN = FastforwardNN(**nn_props)
        self.actions = [ACT_MOVE, ACT_ROT, ACT_TUR_ROT, ACT_SHT]
        self.memory = QTable(**q_table_props)
        self.exploration = 0.1
    
    def _update_exploration(self):
        self.exploration = 0.1

    def _calulate_relative_dist_and_angle(self, tank_x, tank_y, x, y):
        return 

    def _prepare_state(self, tank: Tank,
                       coins_state = np.array([[0,0]]),
                       bombs_state = np.array([[0,0]])) -> list:
        state = [
            tank.center.x,
            tank.center.y,
            tank.angle,
            tank.turret.angle,
            tank.height,
            tank.range,
            tank.armor
        ]
        angle = tank.angle
        pos = np.array([tank.center.x, tank.center.y]) # TODO: change center of tank to NDarray
        coins_state = []
    
    def get_action(self, tank_state: list, coins_state: list, bombs_state: list):
        # action = self.memory
        state = self._prepare_state(tank_state, coins_state, bombs_state)
        action = self.NN.forward(torch.FloatTensor(state))
        action = self._max_act_of_action(action)
        self._update_exploration()
        return action
    
    def _max_act_of_action(self, action: torch.Tensor):
        # ["move", "rotate", "rotate-turret", "shoot", "power-level"]
        max_action = int(action[0:4].argmax().min())
        max_action = self.actions[max_action]
        power = float(action[4])
        pos_neg = float(action[5]) > 0.5
        print(action, max_action, power)
        return {
            D_ACTION: max_action,
            D_POWER: power,
            D_POSITIVE: pos_neg
        }
    