import numpy as np
import matplotlib.pyplot as plt
import os

# CONSTANTS
J = 1

filename = "test_bench_output.csv"
filename2 = "test_bench_output_2.csv"
# path = os.getcwd()
# filename = path + "/" + filename
# times = np.genfromtxt(os.path.join(os.path.expanduser('~'), filename)) / 1000000.0

def get_processed_data(filename, start_offset=0, end_offset=0):
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

    for i in range(20 + start_offset, times.size - end_offset):
        times[i] = np.average(filtered_times[i - 20:i])

    for i in range(20 + start_offset, times.size - end_offset):
        vels[i] = 2 * np.pi / times[i]

    for i in range(20 + start_offset, vels.size - end_offset):
        energies[i] = 0.5 * J * (vels[i]**2)

    for i in range(20 + start_offset, energies.size - end_offset):
        filtered_powers[i] = (energies[i] - energies[i - 1]) / times[i]

    for i in range(20 + start_offset, powers.size - end_offset):
        powers[i] = np.average(filtered_powers[i - 20:i])

    for i in range(1, times.size):
        times[i] = times[i - 1] + times[i]
    
    return times, vels, energies, powers

times, vels, energies, powers = get_processed_data(filename, 20, 20)
times2, vels2, energies2, powers2 = get_processed_data(filename2, 20, 20)

plt.figure()
plt.grid()
plt.plot(times, vels, label=filename)
plt.plot(times2, vels2, label=filename2)
plt.title("Velocity")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(times, energies, label=filename)
plt.plot(times2, energies2, label=filename2)
plt.title("Energy")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(times, powers, label=filename)
plt.plot(times2, powers2, label=filename2)
plt.title("Power")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(vels, powers, label=filename)
plt.plot(vels2, powers2, label=filename2)
plt.ylim(ymin=0)
plt.title("Power vs velocity")
plt.legend()
plt.show()
