"""
    This program will request how many steps taken each day for a week from the user. Calculate the
    total number of steps taken and the average daily number of steps. Then print out a review and 
    findings to the console.     
"""

# variables

total_steps = 0
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
steps = []

# input

for the_day in days:
    steps_for_the_day = -1  # catch initialize for each loop
    while not int(steps_for_the_day) >= 0:  # basic number error catch
        steps_for_the_day = input(
            f"Please enter the total number of steps for {the_day}: ")
        if int(steps_for_the_day) < 0:
            print(
                "Walking backwards is not a negative step. Please try again and enter a positive integer or 0.")
    steps.append([the_day, steps_for_the_day])
    total_steps += int(steps_for_the_day)  # calculate total steps by a loop
# print total steps
print(f"\nYou walked {total_steps:.0f} steps for the week.\n")

# Review the amount of steps for each day

# for loop retrieving day and steps with indexing based on length of steps
# steps- an array with seven index positions with two elements per index position
for e in range(len(steps)):
    # 'e' index position, element 1 with the day
    the_day = steps[e][0]
    # 'e' index position, element 2 with the steps for that day
    steps_for_the_day = steps[e][1]
    print(f"{the_day}, you walked {steps_for_the_day} steps.")

# calculate average daily number of steps

steps_average = total_steps / len(steps)
print(f"\nYou walked around an average of {
      steps_average:.0f} steps for each day.")
