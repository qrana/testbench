import serial

FILENAME = "test_bench_output_2.csv"

ser = serial.Serial('COM8', 115200, timeout=10)
print(ser.name)

data = []

while ser.readline() == "":
    continue

while True:
    line = ser.readline()
    line = line.rstrip()
    data.append(line)
    if line == "":
        break


for line in data:
    print(line)

with open(FILENAME, 'w') as file:
    for line in data:
        file.write(line + "\n")

ser.close()
