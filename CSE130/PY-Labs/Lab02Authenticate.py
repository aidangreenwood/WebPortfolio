# 1. Name:
#      Aidan Greenwood
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      Will take a list of usernames and passwords, then uses them as the user inputs their username and password,
# checks with the actual username and password, and verifies that it is you.
# 4. What was the hardest part? Be as specific as possible.
#      I tried doing this assignment before class, so I had a few problems, especially opening the file, 
# and then figuring out the best way to work with it to make it usable. 
# 5. How long did it take for you to complete the assignment?
#      2

# Open the file, transform each section into a separate list
import json

try:
    file = open("Lab02.json", "r")
    data = json.load(file)  
except OSError:
    print("Couldn't open Lab02.json")
    exit()

usernames = data["username"]
passwords = data["password"]

file.close()

# Ask the user for a username and password.
user_username = input("Username: ")
user_password = input("Password: ")

# Verify if the user is allowed
if user_username in usernames:
    index = usernames.index(user_username)
    
    if passwords[index] == user_password:
        print(f"Welcome back {user_username}.")
    else:
        print("You are not authorized to use the system.")
else:
    print("You are not authorized to use the system.")
    