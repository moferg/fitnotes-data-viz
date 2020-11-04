# Marshall Ferguson - 9/2020

# Features to implement:
# Infinite main loop for user to choose options from (DONE)
# Buid a conversion tool (lb to kg)
# Read data from an external CSV file (DONE)
# Visualize data in a graph (DONE)
# Use matplotlib (DONE) 

# Potential features to include:
# Create a dict or list and use it in program (DONE)
# Create and call at least 3 functions
# Create 3 or more unit tests (DONE)

# Imports

import csv
import matplotlib.pyplot as plt
import numpy as np
import time
from os import system, name 

# Functions

def unique_values(list1):
    '''Takes a list as input and outputs a list with all duplicates removed''' 
    x = np.array(list1) 
    return list(np.unique(x))

def clear_screen():
    '''Clears out the terminal/console to a blank screen'''
    if name == 'nt':
        system('cls')
    if name == 'posix':
        system('clear')

# Variables created before opening CSV file
dates = []
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
            muscle_group.append(row[2])
            exercise_name.append(row[1])
            volumes.append(float(row[4]) * float(row[3]))    # number of reps per set * number of lbs per rep = volume per set
            line_count += 1
    # print(f'Processed {line_count} lines.')
    # print(f'Contents of dates variable: {dates}')
    # print(f'Length of dates variable: {len(dates)}')
    # print(f'Contents of volumes variable: {volumes}')
    # print(f'Length of volumes variable: {len(volumes)}')
    # print(f'Contents of muscle_group variable: {muscle_group}')
    # print(f'Length of muscle_group variable: {len(muscle_group)}')
    # print(f'Contents of exercise_name variable: {exercise_name}')
    # print(f'Length of exercise_name variable: {len(exercise_name)}')

# Remove duplicates from dates list
unique_dates = unique_values(dates)
# print(f'Contents of unique_dates variable: {unique_dates}')
# print(f'Length of unique_dates variable: {len(unique_dates)}')

# Remove duplicates from muscle group list
unique_muscle_group = unique_values(muscle_group)
# print(f'Contents of unique_muscle_group variable: {unique_muscle_group}')
# print(f'Length of unique_muscle_group variable: {len(unique_muscle_group)}')

# Remove duplicates from exercise name list
unique_exercise_name = unique_values(exercise_name)
# print(f'Contents of unique_exercise_name variable: {unique_exercise_name}')
# print(f'Length of unique_exercise_name variable: {len(unique_exercise_name)}')

# Create a list of the number of sets performed on a certain date
sets_on_date = [dates.count(date) for date in unique_dates]
# print(f'Contents of sets_on_date variable: {sets_on_date}')
# print(f'Length of sets_on_date variable: {len(sets_on_date)}')

# Create a list of the number of times a muscle group was targetted 
muscle_group_count = [muscle_group.count(muscle) for muscle in unique_muscle_group]
# print(f'Contents of muscle_group_count variable: {muscle_group_count}')
# print(f'Length of muscle_group_count variable: {len(muscle_group_count)}')

# Create a list of the number of times an exercise was performed
exercise_name_count = [exercise_name.count(exercise) for exercise in unique_exercise_name]
# print(f'Contents of exercise_name_count variable: {exercise_name_count}')
# print(f'Length of exercise_name_count variable: {len(exercise_name_count)}')

# Remove the year from dates in unique_dates list
unique_dates = [date.lstrip('2020-') for date in unique_dates]
# print(f'Contents of unique_dates variable: {unique_dates}')
# print(f'Length of unique_dates variable: {len(unique_dates)}')

# Remove extraneous notation from exercise names
unique_exercise_name = [name.replace('(Pulley)', '') for name in unique_exercise_name]
# print(f'Contents of unique_exercise_name variable: {unique_exercise_name}')
# print(f'Length of unique_exercise_name variable: {len(unique_exercise_name)}')

# Create a list of lists containing the volumes lifted on dates
# volumes_for_workout = [volumes[:sets] for sets in sets_on_date]
volumes_for_workout = []
volumes_for_workout.append(volumes[0:18])          # 18
volumes_for_workout.append(volumes[18:45])         # 27
volumes_for_workout.append(volumes[45:65])         # 20
volumes_for_workout.append(volumes[65:92])         # 27
volumes_for_workout.append(volumes[92:120])        # 28
volumes_for_workout.append(volumes[120:140])       # 20
volumes_for_workout.append(volumes[140:166])       # 26
volumes_for_workout.append(volumes[166:193])       # 27
volumes_for_workout.append(volumes[193:212])       # 19
volumes_for_workout.append(volumes[212:239])       # 27
volumes_for_workout.append(volumes[239:267])       # 28
volumes_for_workout.append(volumes[267:286])       # 19
volumes_for_workout.append(volumes[286:311])       # 25
volumes_for_workout.append(volumes[311:339])       # 28
volumes_for_workout.append(volumes[339:358])       # 19
volumes_for_workout.append(volumes[358:386])       # 28
volumes_for_workout.append(volumes[386:416])       # 30
volumes_for_workout.append(volumes[416:436])       # 20
# print(f'Contents of volumes_for_workout variable: {volumes_for_workout}')
# print(f'Length of volumes_for_workout variable: {len(volumes_for_workout)}')

# Create a list containing the total volume of all exercises on certain dates
volumes_on_unique_dates = [sum(volume) for volume in volumes_for_workout]
# print(f'Contents of volumes_on_unique_dates variable: {volumes_on_unique_dates}')
# print(f'Length of volumes_on_unique_dates variable: {len(volumes_on_unique_dates)}')

# Create an welcoming menu for the user
print('Welcome to the FitNotes Data Visualizer!')
time.sleep(1)
print('This application will take in a CSV file from the FitNotes workout app,')
time.sleep(2)
print('and output graphs and visualizations, guiding you to a more data driven approach to working out.')
time.sleep(2)
clear_screen()

while True:
    print('Please select the graph you would like to see.')
    print('1. Bar graph charting volume over time in lbs')
    print('2. Bar graph charting volume over time in kgs')
    print('3. Pie chart graphing percentages of workouts targetting different muscle groups')
    print('4. Pie chart graphing percenteages of exercises performed')
    print('"q" to quit')
    user_choice = input('(Enter a number from the list or "q" to quit)     ')
    user_choice = user_choice.lower()
    if user_choice == '1':
        # Create and display a bar graph with matplotlib graphing volume listed over time
        plt.figure(figsize=(22.5, 11))
        plt.bar(unique_dates, volumes_on_unique_dates)
        for i in range(0, len(unique_dates)):
            plt.annotate(str(volumes_on_unique_dates[i]) + 'lbs', xy = (i - .45, volumes_on_unique_dates[i]))
        plt.xlabel('Workout Dates')
        plt.ylabel('Workout Volumes (lbs)')
        plt.title('Workout Volumes Over Time')
        plt.show()
        clear_screen()
    elif user_choice == '2':
        # Convert volumes from lbs to kgs
        volumes_on_unique_dates_kg = []
        for volume in volumes_on_unique_dates:
            volume = volume * 0.454
            volumes_on_unique_dates_kg.append(volume)
        # Create and display a bar graph with matplotlib graphing volume listed over time
        plt.figure(figsize=(22.5, 11))
        plt.bar(unique_dates, volumes_on_unique_dates_kg)
        for i in range(0, len(unique_dates)):
            plt.annotate(str("%.2f" % volumes_on_unique_dates_kg[i]) + 'kgs', xy = (i - .45, volumes_on_unique_dates_kg[i]))
        plt.xlabel('Workout Dates')
        plt.ylabel('Workout Volumes (kgs)')
        plt.title('Workout Volumes Over Time')
        plt.show()
        clear_screen()
    elif user_choice == '3':
        # Create and display a pie chart graphing percentages of workouts targetting different muscle groups
        plt.figure(figsize=(15, 11))
        plt.pie(muscle_group_count, labels=unique_muscle_group, autopct='%1.1f%%')
        plt.title('Percentages of Muscle Groups Targetted')
        plt.show()
        clear_screen()
    elif user_choice == '4':
        # Create and display a pie chart graphing percenteages of exercises performed
        plt.figure(figsize=(15, 11))
        plt.pie(exercise_name_count, labels=unique_exercise_name, autopct='%1.1f%%')
        plt.title('Percentages of Exercises Performed')
        plt.show()
        clear_screen()
    elif user_choice == 'q':
        clear_screen()
        break
    else:
        print('Sorry, that was not a valid option. Please select a number from the list of options of press "q" to quit')
        time.sleep(1.5)
        clear_screen()