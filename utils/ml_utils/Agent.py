import torch
import random
import numpy as np
from utils.ml_utils.FastforwardNN import FastforwardNN
from utils.ml_utils.Qtable import QTable
from utils.Tank import Tank

ACT_MOVE = 'move'
ACT_ROT = 'rotate'
ACT_TUR_ROT = 'rotate_tur'
ACT_SHT = 'shoot'
ACT_POWER = 'power'

ST_T_X = 'tank.x'
ST_T_Y = 'tank.y'
ST_T_A = 'tank.angle'
ST_T_R = 'tank.range'
ST_C_D = 'coin.distance'
ST_C_A = 'coin.angle'

D_ACTION = "action-type"
D_POWER = "power"
D_POSITIVE = "pos/neg"
        
        
class Agent:
    def __init__(self, nn_props:dict, states=[ST_T_X, ST_T_Y, ST_T_A, ST_T_R, ST_C_D, ST_C_A],
                 actions=[ACT_MOVE, ACT_ROT, ACT_TUR_ROT, ACT_SHT]) -> None:
        self.states = states
        self.states_len = len(self.states)
        self.actions = actions
        self.NN = FastforwardNN(
            **nn_props, 
            input_size=self.states_len, 
            output_size=len(self.actions)+2
        )
        self.memory = QTable(1_000, self.states, self.actions)
        self.exploration = 0.1
    
    def _update_exploration(self):
        self.exploration = 0.1

    def _distance(self, vector, pair):
        return np.sqrt(np.matmul((vector - pair)**2 ,[1, 1]))
    
    def _angle(self, vector, angle):
        # abs_vector = np.sqrt(np.matmul(vector**2, [1, 1]))
        # cos_theta = np.divide(vector * angle, abs_vector * angle)
        # theta = np.arccos(cos_theta)
        v_len = len(vector)
        theta = np.zeros(v_len)
        for i in range(v_len):
            theta[i] = np.arctan2(*vector[i]) 
        return np.degrees(theta) - angle

    def _prepare_state(self, tank: Tank,
                       coins_state = np.array([[0,0]]),
                       bombs_state = np.array([[0,0]])) -> list:
        state = [0] * self.states_len
        state[:4] = [
            tank.center.x,
            tank.center.y,
            tank.angle,
            tank.range
        ]
        angle = tank.angle
        pos = np.array([tank.center.x, tank.center.y]) # TODO: change center of tank to NDarray
        print(coins_state , pos)
        coins_dist = self._distance(coins_state, pos)
        print(coins_dist)
        coins_angl = self._angle(coins_state, angle)
        print(coins_angl)
        # bombs_state = np.append(self._distance(bombs_state, pos), self._angle(bombs_state, angle))
        nearest_coin_ind = np.argpartition(coins_dist, 0)[0]
        print(nearest_coin_ind)
        state[4: self.states_len] = \
            [coins_dist[nearest_coin_ind], coins_angl[nearest_coin_ind]]
        return state
    
    def get_action(self, tank_state: list, coins_state: list, bombs_state: list):
        state = self._prepare_state(tank_state, np.array(coins_state), np.array(bombs_state))
        print('state', state)
        action = self.memory.get_closest_memory_line()
        print('memory:', action)
        explore = random.uniform(0, 1) > self.exploration
        self._update_exploration()
        if explore or not action:
            print('exploring')
            action = self.NN.forward(torch.FloatTensor(state))
            action = self._max_act_of_action(action)
            print('explored action', action)
        return action
    
    def _max_act_of_action(self, action: torch.Tensor):
        # ["move", "rotate", "rotate-turret", "shoot", "power-level"]
        max_action = int(action[0:4].argmax().min())
        max_action = self.actions[max_action]
        power = abs(float(action[4]))
        pos_neg = float(action[5]) > 0.5
        print(action, max_action, power)
        return {
            D_ACTION: max_action,
            D_POWER: power,
            D_POSITIVE: pos_neg
        }
    
    def feedback(self, reward):
        pass