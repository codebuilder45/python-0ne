"""
        This program will ask your age and then check against four factors and print the results.
        Driving age will be 16
        Voting age will be 18
        Legal to buy alcohol will be 21
        age eligible for senior discount will be 65
        age_1 will be the integer cast variable
    """

# variable and input

print(" "*10 + "Please use positive integer numbers to respond (Ex: 7,34,200)")
age_1 = float(input(
    f"\nHow many times (age) have you been around the sun while on planet Earth ? "))
age_1 = int(age_1)  # error check before official error check commands
# print(age_1)

# check age and give results

if age_1 <= 0:
    print("\nYou found the sorcerer's stone age-reversing elixir.\n")

# Drive check
if age_1 > 0 and age_1 < 16:
    print("You have a few years to go before driving.")
elif age_1 >= 16:
    print("You are able to drive.")

# Vote check
if age_1 > 0 and age_1 < 18:
    print("You have a few years to go before legal voting age.")
elif age_1 >= 18:
    print("You can legally vote.")

# Alcohol check
if age_1 > 0 and age_1 < 21:
    print("You have a few years to go before being legal to buy alcohol.")
elif age_1 >= 21:
    print("You can legally buy alcohol.")

# Senior discount
if age_1 > 0:
    if age_1 < 65:
        print("You are not eligible for a senior discount yet.")
    elif age_1 >= 65:
        print("You are eligible for a senior discount.")

if age_1 >= 100:
    print("\nLive long and prosper.\n")
