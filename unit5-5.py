# Created by: Luca
# Created on: Dec 2017
# Created for: ICS3U
# This finds the average of a 2D array with random numbers

from numpy import random

def two_dimension_loop_average(array):
    # finds average in passed 2D array
    total = 0
    
    for row in array:
        for column in row:
            total = total + column
    average = total / (len(array[0]) * len(array))
    
    return average


row_number = int(raw_input("Enter the number of rows: "))
if row_number < 0:
    row_number = int(raw_input("Please enter a positive number for the number of rows: "))
else:
    pass

column_number = int(raw_input("Enter  number of columns: "))
if column_number < 0:
    column_number = int(raw_input("Please enter a positive number for the number of columns: "))
else:
    pass


table = []

for row in range(0, row_number):
    table.append([])
    for column in range(0, column_number):
        table[row].append(random.randint(0, 50+1))

average_of_element_table = two_dimension_loop_average(table)


print(table)
print("\nThe average of your numbers in the table is approximately: " + str(average_of_element_table) + ".\n")
