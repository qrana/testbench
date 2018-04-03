A program to measure speed, energy and power of a wheel rolling on a bench.

Consists of an Arduino that is connected to the bench and a serial wire between the Arduino and a Laptop.

Arduino meaures rising edges of the sensor pulse, and outputs the time difference between two consequent pulses to the serial. 
The laptop then reads the serial and stores the data in a csv-file. The python script for reading the serial is called
serial-reader.py. Another python script, process_data.py, can be used to output figures based on the csv-file.
