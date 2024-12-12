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
        print(f"{wall_bottles} bottles of beer")
        print("Take one down, pass it around")
        wall_bottles -= 1
        if wall_bottles >= 2:
            print(f"{wall_bottles} bottles of beer on the wall!\n")
        if wall_bottles == 1:
            print(f"{wall_bottles} bottle of beer on the wall!\n")
            print(f"{wall_bottles} bottle of beer on the wall")
            print(f"{wall_bottles} bottle of beer")
            print("Take it down, pass it around")
            wall_bottles -= 1
            print("No bottles of beer on the wall!")
