"""
    This program will count from 1 to 300, check for all numbers divisible by seven, and print a summary.
"""
for i in range(1, 301):  # for loop uses variable i to count from 1-300 by increments of 1
    if i % 7 == 0:      # each number is divided by 7 and checked for a remainder
        # if there is no remainder, which is noted by a 0, the number is printed
        print(i)
    if i > 300:        # if the loop goes past 300, there is a break programmed in
        break           # to exit the loop and continue with the next line of code
else:                   # if the loop completes with no break, the message below is printed
    print("for loop completed with no break")
print("end")            # end of program print line
