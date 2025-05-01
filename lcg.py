from config import Config

# Linear Congruential Generator
class LinearCongruentialGenerator:


    def __init__(self,seed):
        self.a = Config.a
        self.m = Config.m
        self.c = Config.c

        self.state = int.from_bytes(seed, byteorder='big')
    
    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state