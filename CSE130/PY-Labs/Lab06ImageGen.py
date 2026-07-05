# 1. Name:
#      Aidan Greenwood
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This program is designed to take inputs in the form of rows and columns, and 
#      assign each space within that grid a value of filled or not filled; in order to create an image.
# 4. Algorithmic Efficiency
#      I think that for this it would technicaly be O(n^2), but 
#      a more accurate description would be O(RC) R being rows, and C being columns.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment for me, was the sections for creating a grid, assigning things to it.
#      The biggest problem for me, was I was focusing heavily on what was being said in my pseudocode, and
#      couldn't bridge that gap between the fake and the actual code.
# 6. How long did it take for you to complete the assignment?
#      ~ 2

# Import the file, and read it.
import json

try:
    file = open("130.06.json", "r")
    data = json.load(file)  
except OSError:
    print("Couldn't open 130.06.json")
    exit()

# Set variables, dependent on file.
num_rows = data["num_rows"]
num_columns = data["num_columns"]

file.close()

# Start creating structure.
grid_creation_efficiency = 0

grid = []
for row in range(num_rows):
    new_row = []

    for column in range(num_columns):
        new_row.append(" ")

        grid_creation_efficiency += 1
    
    grid.append(new_row)

current_column = 0

# Begin loops, allowing data to be counted and assigned.
assignment_efficiency = 0

for column in data["data"]:

    current_row = 0
    filled = True

    for number in column:
        count = 0
        while count != number:
            if filled == True:
                grid[current_row][current_column] = "#"
            else:
                grid[current_row][current_column] = " "

            assignment_efficiency += 1

            count += 1
            current_row += 1
        

# Switch to what the previous number wasn't.
        filled = not filled

    current_column = current_column + 1

# Print the grid by rows.
print_efficiency = 0

for row in grid:
    line = ""

    for character in row:
        line += character

        print_efficiency += 1

    print(line)

print(f"\n\n\n{grid_creation_efficiency}")
print(assignment_efficiency)
print(print_efficiency)
