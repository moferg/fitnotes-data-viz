# Marshall Ferguson - 9/2020

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
            line_count += 1
        else:
            dates.append(row[0])
            muscle_group.append(row[2])
            exercise_name.append(row[1])
            # number of reps per set * number of lbs per rep = volume per set
            volumes.append(float(row[4]) * float(row[3]))
            line_count += 1

# Remove duplicates from dates list
unique_dates = unique_values(dates)

# Remove duplicates from muscle group list
unique_muscle_group = unique_values(muscle_group)

# Remove duplicates from exercise name list
unique_exercise_name = unique_values(exercise_name)

# Create a list of the number of sets performed on a certain date
sets_on_date = [dates.count(date) for date in unique_dates]

# Create a list of the number of times a muscle group was targetted
muscle_group_count = [muscle_group.count(muscle) for muscle in unique_muscle_group]

# Create a list of the number of times an exercise was performed
exercise_name_count = [exercise_name.count(exercise) for exercise in unique_exercise_name]

# Remove the year from dates in unique_dates list
unique_dates = [date.lstrip('2020-') for date in unique_dates]

# Remove extraneous notation from exercise names
unique_exercise_name = [name.replace('(Pulley)', '') for name in unique_exercise_name]

# Create a list of lists containing the volumes lifted on dates
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

# Create a list containing the total volume of all exercises on certain dates
volumes_on_unique_dates = [sum(volume) for volume in volumes_for_workout]

if __name__ == "__main__":

    # Create an welcoming menu for the user
    clear_screen()
    print('Welcome to the FitNotes Data Visualizer!')
    time.sleep(2)
    print('This application will take in a CSV file from the FitNotes workout app,')
    time.sleep(3)
    print('and output graphs and visualizations, guiding you to a more data driven approach to working out.')
    time.sleep(4)
    clear_screen()

    while True:
        print('Please select the graph you would like to see.')
        print('1. Bar graph charting volume over time in lbs')
        print('2. Bar graph charting volume over time in kgs')
        print('3. Pie chart graphing percentages of workouts targetting different muscle groups')
        print('4. Pie chart graphing percenteages of exercises performed')
        user_choice = input('(Enter a number from the list or "q" to quit)     ')
        user_choice = user_choice.lower()
        if user_choice == '1':
            # Create and display a bar graph with matplotlib graphing volume listed over time
            plt.figure(figsize=(22.5, 11))
            plt.bar(unique_dates, volumes_on_unique_dates)
            x = np.arange(len(volumes_on_unique_dates))
            z = np.polyfit(x, volumes_on_unique_dates, 1)
            p = np.poly1d(z)
            plt.plot(x, p(x), "r--")
            for i in range(0, len(unique_dates)):
                plt.annotate(str(int(volumes_on_unique_dates[i])), xy=(i - .45, volumes_on_unique_dates[i]))
            plt.xlabel('Workout Dates')
            plt.ylabel('Workout Volumes (lbs)')
            plt.title('Workout Volumes (in lbs) Over Time')
            plt.legend(['Trend Line', 'Volume (in lbs)'], loc="upper left")
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
            x = np.arange(len(volumes_on_unique_dates_kg))
            z = np.polyfit(x, volumes_on_unique_dates_kg, 1)
            p = np.poly1d(z)
            plt.plot(x, p(x), "r--")
            for i in range(0, len(unique_dates)):
                plt.annotate(str("%.2f" % volumes_on_unique_dates_kg[i]), xy=(i - .45, volumes_on_unique_dates_kg[i]))
            plt.xlabel('Workout Dates')
            plt.ylabel('Workout Volumes (kgs)')
            plt.title('Workout Volumes (in kgs) Over Time')
            plt.legend(['Trend Line', 'Volume (in kgs)'], loc="upper left")
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
            plt.pie(exercise_name_count, labels=unique_exercise_name, autopct='%1.1f%%', 
                    colors=('tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:cyan'))
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
