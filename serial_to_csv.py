import serial
from datetime import datetime
import csv

measurement_time = 10

filename = "data/" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
file = open(filename, "w")
writer = csv.writer(file, delimiter=",", lineterminator="\n")
ser = serial.Serial('COM3', 115200)
ser.flushInput()

writer.writerow(["Time (s)", "Distance (mm)"])

start = datetime.now()
time = 0

while time < measurement_time:
    time = (datetime.now() - start).total_seconds()
    ser_bytes = ser.readline()
    decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
    writer.writerow([time, decoded_bytes])
    print(time, decoded_bytes)

ser.close()
file.close()