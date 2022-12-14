
import utils.TrainingZoneGameByHand as TZBH

from utils.ml_utils.Agent import D_ACTION, D_POSITIVE, D_POWER, Agent, ACT_MOVE, ACT_POWER, ACT_ROT, ACT_SHT, ACT_TUR_ROT
from utils.ml_utils.FastforwardNN import get_ffnnn_dict


LAYER1_SIZE = 10
LAYER2_SIZE = 10
LR = 0.01

class TrainingZoneGameAuto(TZBH.TrainingZoneGameByHand):
    def __init__(self, background_image_path=TZBH.ZONE_IMAGE) -> None:
        super().__init__(background_image_path)
        self.tank_props = ["x-pos", "y-pos", "angle", "tur_angle", "size", "range", "armor"]
        self.tank_props_size = len(self.tank_props)
        self.state_size = 2*(self.total_coins + self.total_bombs) + self.tank_props_size
        self.action_props = ["move", "rotate", "rotate-turret", "shoot", "power-level", "pos/neg"]
        self.action_props_size = len(self.action_props)
        
        ffnn_props = get_ffnnn_dict(LR, LAYER1_SIZE, LAYER2_SIZE)
        self.agent = Agent(ffnn_props)
        
        self.actions_conv = { }
            
    def _get_state(self):
        return \
            self.tank, \
            [[coin.topleft.x, coin.topleft.y] for coin in self.coins], \
            [[bomb.topleft.x, bomb.topleft.y] for bomb in self.bombs]
        
    
    def _action(self, action):
        print(" --- action --- ")
        
        if action[D_ACTION] == ACT_MOVE:
            forward = action[D_POSITIVE]
            power = (action[D_POWER] % 0.5) * 2.0
            self.tank.move(power, forward)
            print(ACT_MOVE, forward, power)
            
        elif action[D_ACTION] == ACT_ROT:
            self.tank.rotate(action[D_POWER], action[D_POSITIVE])
            print(ACT_ROT,action[D_POSITIVE],action[D_POWER])
            
        elif action[D_ACTION] == ACT_TUR_ROT:
            self.tank.rotate_turret(action[D_POWER], action[D_POSITIVE])
            print(ACT_TUR_ROT, action[D_POSITIVE],action[D_POWER])
            
        elif action[D_ACTION] == ACT_SHT:
            self.tank.shoot()
            print(ACT_SHT)    
        else:
            raise Exception(ValueError("Illegal action {}".format(action)))
        
    
    def play_round(self):
        state = self._get_state()
        action = self.agent.get_action(*state)
        self._action(action)
        
        self._bullets_collisions()
        # game not over, render.
        self._render()
        
        self.clock.tick(TZBH.GAME_SPEED)
        # input("\nPress to cont")
        return self._tank_collisions(self.tank), self.tank.score