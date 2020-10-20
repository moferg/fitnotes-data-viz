# Marshall Ferguson - 9/2020

# Features to implement:
# Infinite main loop for user to choose options from
# Implement a log to store errors in another file
# Buid a conversion tool (lb to kg and vice-versa)
# Read data from an external CSV file (DONE)
# Visualize data in a graph (DONE)
# Use matplotlib (DONE) 

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
    '''Takes a list as input and outputs a list with all duplicates removes''' 
    x = np.array(list1) 
    return list(np.unique(x))

# Create an welcoming menu for the user
print('Welcome to the FitNotes Data Visualizer!')
time.sleep(1)
print('This application will take in a CSV file from the FitNotes workout app,')
time.sleep(2)
print('and output graphs and visualizations, guiding you to a more data driven approach to working out.')
time.sleep(2)

# Variables created before opening CSV file
dates = []
volumes = []

# Open CSV file and extract needed data
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

    # Remove duplicates from dates list
    unique_dates = unique_values(dates)
    # print(unique_dates)
    # print(len(unique_dates))

    # Create a list of the number of sets performed on a certain date
    sets_on_date = [dates.count(date) for date in unique_dates]
    # print(sets_on_date)
    # print(len(sets_on_date))

    # Create a list of lists containing the volumes lifted on dates
    volumes_for_workout = [volumes[0:sets] for sets in sets_on_date]
    # print(volumes_for_workout)
    # print(len(volumes_for_workout))

    # Create a list containing the total volume of all exercises on certain dates
    volumes_on_unique_dates = [sum(volume) for volume in volumes_for_workout]
    # print(volumes_on_unique_dates)
    # print(len(volumes_on_unique_dates))

    #TODO: change graph options so that it shows up larger by default

    # Create and display a chart with matplotlib graphing volume listed over time
    ax = plt.axes()
    ax.bar(unique_dates, volumes_on_unique_dates)
    ax.scatter(unique_dates, volumes_on_unique_dates, color='r', linewidth=4)
    ax.plot(unique_dates, volumes_on_unique_dates, color='r', linewidth=2)
    for i in range(0, len(unique_dates)):
        ax.annotate(str(volumes_on_unique_dates[i]) + 'lbs', xy = (i - .35, volumes_on_unique_dates[i]))
    ax.set_xlabel('Workout Dates')
    ax.set_ylabel('Workout Volumes (lbs)')
    ax.set_title('Workout Volumes Over Time')
    plt.show()