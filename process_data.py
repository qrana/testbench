import numpy as np
import matplotlib.pyplot as plt
import os

# CONSTANTS
J = 1

filename = "test_bench_output.csv"
# path = os.getcwd()
# filename = path + "/" + filename
# times = np.genfromtxt(os.path.join(os.path.expanduser('~'), filename)) / 1000000.0
filtered_times = np.genfromtxt(filename) / 1000000.0
times = np.zeros(filtered_times.size)
vels = np.zeros(times.size)
energies = np.zeros(times.size)
powers = np.zeros(times.size)
filtered_powers = np.zeros(times.size)


for i in range(6, filtered_times.size - 2):
    previous_average = np.average(filtered_times[i -5:i -1])
    diff_to_previous_average = (filtered_times[i] - previous_average) / previous_average
    if abs(diff_to_previous_average) > 0.02:
        print("Averaging", i)
        filtered_times[i] = (filtered_times[i-1] + filtered_times[i+2]) / 2.0

for i in range(20, times.size):
   times[i] = np.average(filtered_times[i - 20:i])

for i in range(20, times.size):
    vels[i] = 2 * np.pi / times[i]

for i in range(20, vels.size):
    energies[i] = 0.5 * J * (vels[i]**2)

for i in range(20, energies.size):
    filtered_powers[i] = (energies[i] - energies[i - 1]) / times[i]

for i in range(20, powers.size):
    powers[i] = np.average(filtered_powers[i - 20:i])

plt.figure()
plt.grid()
plt.plot(times)
plt.title("Times")
plt.show()

for i in range(1, times.size):
    times[i] = times[i - 1] + times[i]

plt.figure()
plt.grid()
plt.plot(times, vels)
plt.title("Velocity")
plt.show()

plt.figure()
plt.grid()
plt.plot(times, energies)
plt.title("Energy")
plt.show()

plt.figure()
plt.grid()
plt.plot(times, powers)
plt.title("Power")
plt.show()
