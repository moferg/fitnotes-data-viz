# Marshall Ferguson - 9/2020

# Features to implement:
# Infinite main loop for user to choose options from
# Implement a log to store errors in another file
# Buid a conversion tool (lb to kg and vice-versa)
# Read data from an external CSV file
# Visualize data in a graph
# Use matplotlib 

# Potential features to include:
# Create a dict or list and use it in program
# Create and call at least 3 functions
# Create 3 or more unit tests

# Imports

import csv
import matplotlib as plt
import time

print('Welcome to the FitNotes Data Visualizer!')
time.sleep(1)
print('This application will take in a CSV file from the FitNotes workout app,')
time.sleep(2)
print('and output graphs and visualizations, guiding you to a more data driven approach to working out.')
time.sleep(2)

with open('FitNotes_Export_2020_09_29.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tOn {row[0]}, you worked out your {row[2]}.')
            print(f'\tYou performed {row[1]} for {row[4]} reps at {row[3]} lbs.')
            line_count += 1
    print(f'Processed {line_count} lines.')