"""This program will take 99 bottles down off the wall with the help of a while loop."""

# 3 bottles of beer on the wall
# 3 bottles of beer
# Take one down, pass it around
# 2 bottles of beer on the wall!

# 2 bottles of beer on the wall
# 2 bottles of beer
# Take one down, pass it around
# 1 bottle of beer on the wall!

# 1 bottle of beer on the wall
# 1 bottle of beer
# take it down, pass it around
# No bottles of beer on the wall!

wall_bottles = 99

while wall_bottles != 0:
    # first line
    if wall_bottles >= 2:
        print(f"{wall_bottles} bottles of beer on the wall")
    if wall_bottles == 1:
        print(f"{wall_bottles} bottle of beer on the wall")
    # second line
    if wall_bottles >= 2:
        print(f"{wall_bottles} bottles of beer")
    if wall_bottles == 1:
        print(f"{wall_bottles} bottle of beer")
    # third line
    if wall_bottles >= 2:
        print("Take one down, pass it around")
    if wall_bottles == 1:
        print("Take it down, pass it around")
    # take a bottle
    wall_bottles -= 1
    # fourth line
    if wall_bottles >= 2:
        print(f"{wall_bottles} bottles of beer on the wall!\n")
    elif wall_bottles == 1:
        print(f"{wall_bottles} bottle of beer on the wall!\n")
    elif wall_bottles == 0:
        print("No bottles of beer on the wall!")
