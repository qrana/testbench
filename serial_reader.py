import serial

FILENAME = "test_bench_output"

ser = serial.Serial('COM8', 115200, timeout=10)
print(ser.name)

time_data = []
lambda_data = []

while ser.readline() == "":
    continue

mode_phase = 0
while True:
    line = ser.readline()
    line = line.rstrip()
    if mode_phase % 2 == 0:
        time_data.append(line)
    else:
        lambda_data.append(line)
    if line == "":
        break
    mode_phase += 1

ser.close()

for line in time_data:
    print(line)
for line in lambda_data:
    print(line)

with open(FILENAME + "_time.csv", 'w') as file:
    for line in time_data:
        file.write(line + "\n")

with open(FILENAME + "_lambda.csv", 'w') as file:
    for line in lambda_data:
        file.write(line + "\n")
