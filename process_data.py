import numpy as np
import matplotlib.pyplot as plt

# CONSTANTS
J = 1

times = np.genfromtxt("test_bench_output.csv") / 1000000.0
vels = np.zeros(times.size)
energies = np.zeros(times.size)
powers = np.zeros(times.size)

for i in range(times.size):
    vels[i] = 2 * np.pi / times[i]

for i in range(vels.size):
    energies[i] = 0.5 * J * (vels[i]**2)

for i in range(1, energies.size):
    powers[i] = (energies[i] - energies[i - 1]) / float(times[i])

for i in range(1, times.size):
    times[i] = times[i - 1] + times[i]

print times
print vels
print energies
print powers

plt.figure()
plt.grid()
plt.plot(times, vels)
plt.show()

plt.figure()
plt.grid()
plt.plot(times, energies)
plt.show()

plt.figure()
plt.grid()
plt.plot(times, powers)
plt.show()