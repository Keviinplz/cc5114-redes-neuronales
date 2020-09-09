from neuron import *

neuronAND = Neuron(1,1,-1.5, 0)
neuronOR = Neuron(1,1, -0.5, 0)
neuronNAND = Neuron(-2, -2, 3, 0)

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
