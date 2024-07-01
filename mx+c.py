import torch
from torch import torch.nn

class Model(torch.nn):
    def __init__(self):
        super.__init__()
        torch.manual_seed(42)
        self.m = torch.rand(1)
        torch.manual_seed(42)
        self.c = torch.rand(1)
    def forward(X):
        return self.m * X + self.c

optimizer = torch.nn.Modules