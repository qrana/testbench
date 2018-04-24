import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# CONSTANTS
J = 1
n_per_rev = 10.0

filename = sys.argv[1]
filename = filename.split(".")
filename_base = filename[0]
filename_end = filename[1]

filename_time = filename_base + "_time." + filename_end
filename_lambda = filename_base + "_lambda." + filename_end

# filename_time = "test_bench_output_time.csv"
# filename_time2 = "test_bench_output_2_time.csv"
# filename_lambda = "test_bench_output_lambda.csv"
# filename_lambda2 = "test_bench_output_2_lambda.csv"
# path = os.getcwd()
# filename_time = path + "/" + filename_time
# times = np.genfromtxt(os.path.join(os.path.expanduser('~'), filename_time)) / 1000000.0

def get_processed_data(filename_time, start_offset=0, end_offset=0):
    filtered_times = np.genfromtxt(filename_time) / 1000000.0
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
        vels[i] = 141/18.0 * 22/49.5 * 29/20.0 *60 / times[i] / n_per_rev

    for i in range(20 + start_offset, vels.size - end_offset):
        energies[i] = 0.5 * J * (vels[i]**2)

    for i in range(20 + start_offset, energies.size - end_offset):
        filtered_powers[i] = (energies[i] - energies[i - 1]) / times[i]

    for i in range(20 + start_offset, powers.size - end_offset):
        powers[i] = np.average(filtered_powers[i - 20:i])

    for i in range(1, times.size):
        times[i] = times[i - 1] + times[i]
    
    return times, vels, energies, powers

def get_lambda_data(filename_lambda, start_offset = 0, end_offset = 0):
    unaveraged_lambdas = np.genfromtxt(filename_lambda)
    lambdas = np.zeros(unaveraged_lambdas.size)
    for i in range(20 + start_offset, unaveraged_lambdas.size - end_offset):
        lambdas[i] = np.average(unaveraged_lambdas[i - 20:i]) / 255.0 / 1.023 + 0.5
    return lambdas

times, vels, energies, powers = get_processed_data(filename_time, 20, 20)
#times2, vels2, energies2, powers2 = get_processed_data(filename_time2, 20, 20)
lambdas = get_lambda_data(filename_lambda, 10, 30)
#lambdas2 = get_lambda_data(filename_lambda2)
times2 = []
vels2 = []
energies2 = []
powers2 = []
lambdas2 = []

plt.figure()
plt.grid()
plt.plot(times, vels, label=filename_time)
#plt.plot(times2, vels2, label=filename_time2)
plt.title("Velocity")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(times, energies, label=filename_time)
#plt.plot(times2, energies2, label=filename_time2)
plt.title("Energy")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(times, powers, label=filename_time)
#plt.plot(times2, powers2, label=filename_time2)
plt.title("Power")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(times, lambdas, label=filename_lambda)
#plt.plot(times2, lambdas2, label=filename_lambda2)
plt.title("Lambda")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(vels, powers, label=filename_time)
#plt.plot(vels2, powers2, label=filename_time2)
plt.ylim(ymin=0)
plt.title("Power vs velocity")
plt.legend()
plt.show()

plt.figure()
plt.grid()
plt.plot(vels, lambdas, label=filename_lambda)
#plt.plot(vels2, lambdas2, label=filename_lambda2)
plt.ylim(ymin=0)
plt.title("Lambda vs velocity")
plt.legend()
plt.show()
