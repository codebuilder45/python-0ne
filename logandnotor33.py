"""
    This program will request two different integers from the user, and use the logical operators
    and, or ,and not, to analyze their properties.   
"""
# input

intgr_1 = int(input("Please enter the first integer:  "))
intgr_2 = int(input("Please enter the second integer:  "))

# analyze

print(f"\ninteger1 is greater than or equal to 1 ?  {not intgr_1 < 1}")
print(f"integer2 is less than or equal to 0 ?  {intgr_2 < 0 or intgr_2 == 0}")
print(f"both integers are greater than 20 ?  {intgr_1 > 20 and intgr_2 > 20}")
print(f"at the same time each integer cubed is positive and even ?  {(not (intgr_1 ** 3) < 1) and (
    (intgr_1 ** 3) % 2 == 0) and (not (intgr_2 ** 3) < 1) and ((intgr_2 ** 3) % 2 == 0)}")
print(f"is either integer less than two times itself ?  {(intgr_1 < (intgr_1 * 2)) or (intgr_2 < (intgr_2 * 2))}")
print(f"one of the integers is not divisible by 3 ?  {(not (intgr_1 % 3 == 0)) or (not (intgr_2 % 3 == 0))}\n")
