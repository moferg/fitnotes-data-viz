# Marshall Ferguson - 9/2020

# Features to implement:
# Infinite main loop for user to choose options from
# Implement a log to store errors in another file
# Buid a conversion tool (lb to kg and vice-versa)
# Read data from an external CSV file (DONE)
# Visualize data in a graph
# Use matplotlib 

# Potential features to include:
# Create a dict or list and use it in program (DONE)
# Create and call at least 3 functions
# Create 3 or more unit tests

# Imports

import csv
import matplotlib.pyplot as plt
import numpy as np
import time

# Functions

def unique_values(list1): 
    x = np.array(list1) 
    return list(np.unique(x))

print('Welcome to the FitNotes Data Visualizer!')
time.sleep(1)
print('This application will take in a CSV file from the FitNotes workout app,')
time.sleep(2)
print('and output graphs and visualizations, guiding you to a more data driven approach to working out.')
time.sleep(2)

dates = []
volumes = []

with open('FitNotes_Export_2020_10_04.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names: {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\tOn {row[0]}, you performed {row[1]} for {row[4]} reps at {row[3]} lbs.')
            dates.append(row[0])
            volumes.append(float(row[4]) * float(row[3]))
            line_count += 1
    # print(f'Processed {line_count} lines.')
    # print(dates)
    # print(len(dates))
    # print(volumes)
    # print(len(volumes))

    unique_dates = unique_values(dates)
    print(unique_dates)
    print(len(unique_dates))

    sets_on_date = []
    for date in unique_dates:
        sets_on_date.append(dates.count(date))
    print(sets_on_date)
    print(len(sets_on_date))

    #TODO - set up a list with len() of 18 for volumes of each unique date

    volumes_for_workout = []
    for sets in sets_on_date:
        volumes_for_workout.append(volumes[0:sets])
    print(volumes_for_workout)
    print(len(volumes_for_workout))

    volumes_on_unique_dates = []
    for volume in volumes_for_workout:
        volumes_on_unique_dates.append(sum(volume))
    print(volumes_on_unique_dates)
    print(len(volumes_on_unique_dates))

    fig, ax = plt.subplots()
    ax.bar(unique_dates, volumes_on_unique_dates)
    plt.show()