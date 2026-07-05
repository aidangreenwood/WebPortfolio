# 1. Name:
#      Aidan Greenwood
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This will take an unsorted list from a file
#      then sort it and display that sorted list.
# 4. What was the hardest part? Be as specific as possible.
#      This was one of the first times I have used a function
#      and kind of understood what I was doing, so that part was minorly chalanging.
#      I'd say that the most chalanging part, was just knowing where all the variable
#      would be use, and figuring out the "math" of the algorithm.
# 5. How long did it take for you to complete the assignment?
#      4 hours

import json

# Ask for file name.
file_name = input("Enter the name of the file: ")
assert type(file_name) == str

# Make sure the file can open.
try:
    file = open(file_name, "r")
    data = json.load(file)

except OSError:
    print(f"Couldn't open {file_name}")
    exit()

def swap_sort():

    # Make varaibles.
    file_list = data["array"]

    assert len(file_list) >= 0
    length_of_list = len(file_list)

    if len(file_list) == 0:
        print("The list is empty and can't be sorted.")
        return
    if len(file_list) == 1:
        print("The list only has one item, it is already sorted.")
        for i in file_list:
            print(f"\t{i}")
        return

    marker_i = len(file_list) - 1

    # While the marker hasn't reached the first index...
    while marker_i > 0:

        biggest_so_far = file_list[0]
        biggest_num_i = 0

        # For each item in list...
        for i in range(marker_i + 1):

            assert 0 <= i <= marker_i
            assert 0 <= biggest_num_i <= len(file_list)

            # If new item is bigger that biggest_so_far
            # set biggest_so_far as new item.
            if biggest_so_far < file_list[i]:
                biggest_so_far = file_list[i]
                biggest_num_i = i

        # Swap biggest_so_far with last in index
        file_list[biggest_num_i], file_list[marker_i] = file_list[marker_i], file_list[biggest_num_i]
        marker_i -= 1

        assert length_of_list == len(file_list)

    # Print the sorted list
    print(f"The values in {file_name} are:")
    for i in file_list:
        print(f"\t{i}")
    return
swap_sort()