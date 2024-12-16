"""
    This program will request five names from the user. Convert the list to uppercase. 
    Bubble Sort the names into ascending order.
    Print to the console. Reverse the name list and print to the console.     
"""

# variable list

name_list = []

# input

for name in range(5):
    name_element = input(f"Please enter name {name + 1}: ")
    name_list.append(name_element)

for i in range(0, len(name_list)):
    name_list[i] = name_list[i].upper()
    # convert all name to upper case to help sort and help priority between 'a'and 'A' case letters
# print name list
print(f"\nThe names were entered in this order: {name_list}")

# Bubble Sort the names into ascending order

exchange = True  # flag to track if an exchange happened

while exchange:
    exchange = False  # reset
    for i in range(len(name_list) - 1):
        # compare
        if name_list[i] > name_list[i + 1]:
            exchange = True  # An exchange is needed
            name_list[i], name_list[i + 1] = name_list[i + 1], name_list[i]

# print the sorted order
print(f"\nThe names were sorted in this order: {name_list}")

# reverse the sorted order
name_list.reverse()
print(f"\nThe names were reversed in this order: {name_list}")
