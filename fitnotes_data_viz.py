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
    '''Takes a list as input and outputs a list with all duplicates removed''' 
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
reps = []
muscle_group = []
exercise_name = []
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
            reps.append(int(row[4]))
            muscle_group.append(row[2])
            exercise_name.append(row[1])
            volumes.append(float(row[4]) * float(row[3]))    # number of reps per set * number of lbs per rep
            line_count += 1
    # print(f'Processed {line_count} lines.')
    print(f'Contents of dates variable: {dates}')
    print(f'Length of dates variable: {len(dates)}')
    print(f'Contents of volumes variable: {volumes}')
    print(f'Length of volumes variable: {len(volumes)}')

    # Remove duplicates from dates list
    unique_dates = unique_values(dates)
    print(f'Contents of unique_dates variable: {unique_dates}')
    print(f'Length of unique_dates variable: {len(unique_dates)}')

    # Create a list of the number of sets performed on a certain date
    sets_on_date = [dates.count(date) for date in unique_dates]
    print(f'Contents of sets_on_date variable: {sets_on_date}')
    print(f'Length of sets_on_date variable: {len(sets_on_date)}')

    # TODO: double check and make sure this is assigning correct volumes to list (IT IS NOT)
    # Create a list of lists containing the volumes lifted on dates
    volumes_for_workout = [volumes[:sets] for sets in sets_on_date]
    print(f'Contents of volumes_for_workout variable: {volumes_for_workout}')
    print(f'Length of volumes_for_workout variable: {len(volumes_for_workout)}')

    # Create a list containing the total volume of all exercises on certain dates
    volumes_on_unique_dates = [sum(volume) for volume in volumes_for_workout]
    print(f'Contents of volumes_on_unique_dates variable: {volumes_on_unique_dates}')
    print(f'Length of volumes_on_unique_dates variable: {len(volumes_on_unique_dates)}')

    # TODO: change graph options so that it shows up larger by default
    # TODO: add body part targeted of each date to graph

    # Create and display a chart with matplotlib graphing volume listed over time
    # ax = plt.axes()
    # ax.bar(unique_dates, volumes_on_unique_dates)
    # ax.scatter(unique_dates, volumes_on_unique_dates, color='r', linewidth=4)
    # ax.plot(unique_dates, volumes_on_unique_dates, color='r', linewidth=2)
    # for i in range(0, len(unique_dates)):
    #     ax.annotate(str(volumes_on_unique_dates[i]) + 'lbs', xy = (i - .35, volumes_on_unique_dates[i]))
    # ax.set_xlabel('Workout Dates')
    # ax.set_ylabel('Workout Volumes (lbs)')
    # ax.set_title('Workout Volumes Over Time')
    # plt.show()