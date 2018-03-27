import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("test_bench_output.csv")
for i in range(data.size):
    vel = 1/data[i]
    data[i] = vel

print data
