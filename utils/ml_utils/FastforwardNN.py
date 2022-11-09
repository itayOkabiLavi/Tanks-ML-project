from turtle import forward
import torch
import torch.nn as nn
import torch.optim as opt
import torch.nn.functional as funcs

def get_ffnnn_dict(learning_rate, input_size, layer1_size, layer2_size, output_size):
    return {
        'learning_rate': learning_rate,
        'input_size': input_size, 
        'layer1_size': layer1_size, 
        'layer2_size': layer2_size, 
        'output_size': output_size
    }

class FastforwardNN(nn.Module):
    def __init__(self, learning_rate, input_size, layer1_size, layer2_size, output_size) -> None:
        super(FastforwardNN, self).__init__()
        
        self.input_size = input_size
        self.layer1_size = layer1_size
        self.layer2_size = layer2_size
        self.output_size = output_size
        
        self.lr = learning_rate
        
        self.in_l1 = nn.Linear(self.input_size, self.layer1_size, bias=False)
        self.l1_l2 = nn.Linear(self.layer1_size, self.layer2_size, bias=False)
        self.l2_out = nn.Linear(self.layer2_size, self.output_size, bias=False)
        
        print(self.in_l1.weight)
        print(self.l1_l2.weight)
        print(self.l2_out.weight)
        
        self.optimizer = opt.Adam(self.parameters(), lr=self.lr)
        self.L = nn.MSELoss()
        self.mem = set()
        
    def forward(self, inp: torch.Tensor):
        x = funcs.relu(self.in_l1(inp))
        x = funcs.relu(self.l1_l2(x))
        output = funcs.softsign(self.l2_out(x))
        # print("input:", inp)
        # print("output:", output)
        # if (str(inp), str(output)) not in self.mem:
        #     self.mem.add((str(inp), str(output)))
        return output
        