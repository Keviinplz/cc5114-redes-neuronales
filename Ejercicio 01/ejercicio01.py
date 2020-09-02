class Neuron:
    def __init__(self, w1, w2, b):
        self.w1 = w1
        self.w2 = w2
        self.b = b

    def compute(self, x1, x2):
        return x1 * self.w1 + x2 * self.w2 

    def output(self, x1, x2):
        return self.compute(x1, x2) + self.b > 0

neuronAND = Neuron(1,1,-1.5)
neuronOR = Neuron(1,1, -0.5)
neuronNAND = Neuron(-2, -2, 3)

# Test's

# AND
assert(neuronAND.output(0,0) == 0)
assert(neuronAND.output(0,1) == 0)
assert(neuronAND.output(1,0) == 0)
assert(neuronAND.output(1,1) == 1)

# OR
assert(neuronOR.output(0,0) == 0)
assert(neuronOR.output(0,1) == 1)
assert(neuronOR.output(1,0) == 1)
assert(neuronOR.output(1,1) == 1)

# NAND
assert(neuronNAND.output(0,0) == 1)
assert(neuronNAND.output(0,1) == 1)
assert(neuronNAND.output(1,0) == 1)
assert(neuronNAND.output(1,1) == 0)


