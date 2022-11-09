import pandas as pd

class QTable:
    def __init__(self, mem_length, 
                 states: list, actions: list, 
                 memory = pd.DataFrame()) -> None:
        self.state_columns = states
        self.action_columns = actions
        if memory.empty:
            self.memory = pd.DataFrame([], columns=self.state_columns + self.action_columns)
            self.mem_pointer = 0
        else:
            self.memory = memory.copy()
            self.mem_pointer = len(self.memory.index)
        self.memory.set_index(self.state_columns)
        self.rate = 0.1
        self.reward_update = lambda newR, oldR: self.rate*newR + (1-self.rate)*oldR
    
    def add_memory_line(self, state, action, reward: float):
        if state not in self.memory.index:
            self.memory.loc[state] = 0
            self.memory[action].loc[state] = reward
        else:
            self.memory[action].loc[state] = self.reward_update(
                reward, self.memory[action].loc[state]
            )
            
    def get_memory_line(self, state):
        return self.memory.loc[state]
    
    def get_closest_memory_line(self):
        pass
        
    def get_action(self, state):
        if state not in self.memory.index:
            return None
        max_action = self.memory.loc[state].idxmax()
        return max_action