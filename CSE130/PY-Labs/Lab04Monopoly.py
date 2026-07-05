# 1. Name:
#      Aidan Greenwood
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      Helps find the quickest route to getting a hotel on Pennsylvania, if possible.
# 4. What was the hardest part? Be as specific as possible.
#      I think that the hardest part, was the logic; making sure that all the if statements were used correctly.
# 5. How long did it take for you to complete the assignment?
#      2 hours

property_nums = 0
hotel_need = 1

# Hotel on pennsylvania already?

# one_hotel = input("\nDo you have a hotel on pennsylvania?(yes, no) ").lower()
# if one_hotel == "yes":
#     print("You cannot purchase a hotel if the property already has one.")
# else:

# Color Group

colors = input("Do You have all the green properties?(yes, no) ").lower()
if colors == "no":
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
else:

# What on each property (Swaps)

    PC_num = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    if PC_num == 5:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
    else:
        property_nums += PC_num

        NC_num = int(input("What is on North Carolina Avenue? (0, 1, ... 5) "))
        if NC_num == 5:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
        else:
            property_nums += NC_num    

            PA_num = int(input("What is on Pennsylvania Avenue? (0, 1, ... 5) "))
            if PA_num == 5:
                print("There is already a hotel on pennsylvania")
            else:
                property_nums += PA_num
    
                num_house_need =  12 - property_nums

# How many houses

                house_availability = int(input("How many houses are there to purchase? "))
                if house_availability < num_house_need:
                    print("There are not enough houses available for purchase at this time.")
                else:
                    cost = (num_house_need + hotel_need) * 200                    

# How many hotels available

                    hotel_availability = int(input("How many hotels are there to purchase? "))
                    if hotel_availability < 1:
                        print("There are not enough hotels available for purchase at this time.")
                    else:
                        
# How much money

                        money_available = int(input("How much cash do you have to spend? "))
                        if money_available < cost:
                            print("You do not have sufficient funds to purchase a hotel at this time.")
                        else:

# Money needed

                            print(f"\nThis will cost ${cost}.")

# Needed stuff

                            print(f"Purchase 1 hotel and {num_house_need} house(s).")

# Number of Houses/Hotels on each

                            PA_needed = 4 - PA_num
                            PC_needed = 4 - PC_num
                            NC_needed = 4 - NC_num
                            
                            print("Put 1 hotel on Pennsylvania and return any houses to the bank.")
                            if PC_needed != 0:
                                print(f"Put {PC_needed} house(s) on Pacific.")
                            if NC_needed != 0:
                                print(f"Put {NC_needed} house(s) on North Carolina.")
