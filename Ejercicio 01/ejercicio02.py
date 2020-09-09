import random
import matplotlib.pyplot as plt
import numpy as np

import neuron

# Init Valuesgi
seed = 42
training_range = 10000
learning_rate = 0.01

neuron = neuron.Neuron(1, 2, -1, learning_rate)
random.seed(seed)

def f(x):
    return -0.5*x - 3

for iteration in range(training_range):
    xValue = random.randint(0, 50) - 25 # Integers between [-25, 25]
    yValue = random.randint(0, 50) - 25 # Integers between [-25, 25]
    if (f(xValue) >= yValue):
        t = 0
    else:
        t = 1
    neuron.fit(xValue, yValue, t)

xRange = np.arange(-25, 25)
plt.plot(xRange, f(xRange))
test_points = 500
for i in range(test_points):
    xValue = random.randint(0, 50) - 25 # Integers between [-25, 25]
    yValue = random.randint(0, 50) - 25 # Integers between [-25, 25]

    prediction = neuron.output(xValue, yValue)
    if prediction == 0: 
        plt.plot(xValue, yValue, '*r')
    else: 
        plt.plot(xValue, yValue, '*b')
        
plt.show()