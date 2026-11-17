# Create a sample CSV file and read rows using the csv module


import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Sensor", "Reading"])
    writer.writerow(["S1", "Temperature", "26.5"])
    writer.writerow(["S2", "Humidity", "60.0"])
with open("data.csv", "r") as f:
    for row in csv.reader(f):
        print(row)