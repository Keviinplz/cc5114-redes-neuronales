"""
Clase Neuron

Define una neurona, con 3 parámetros, las cuales son sus pesos y su bias
"""

class Neuron:
    def __init__(self, w1, w2, b, lr):
        self.w1 = w1
        self.w2 = w2
        self.b = b
        self.lr = lr

    
    def compute(self, x1, x2):
        return x1 * self.w1 + x2 * self.w2 

    def output(self, x1, x2):
        return 1 if self.compute(x1, x2) + self.b > 0 else 0
        
    def fit(self, x1, x2, t):
        diff = t - self.output(x1, x2)
        self.w1 += self.lr * x1 * diff
        self.w2 += self.lr * x2 * diff
        self.b += self.lr * diff