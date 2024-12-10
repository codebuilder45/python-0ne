"""   
    This program will convert kilograms into pounds. The conversion formula is:  
    number of Kilograms (kg) * 2.20462 equals number of pounds (lb).
    There will be five examples. The assignment example was to four decimal places.
"""

# variables

con_factor = 2.20462  # conversion factor to multiply kg(s) by to get lb(s)
kg_1 = 2  # kilogram example variables
kg_2 = 14
kg_3 = 5.5
kg_4 = 20
kg_5 = 17.3

# math

lb_1 = kg_1 * con_factor
lb_2 = kg_2 * con_factor
lb_3 = kg_3 * con_factor
lb_4 = kg_4 * con_factor
lb_5 = kg_5 * con_factor

# print summary

print(f"{kg_1} kilograms is approximately {lb_1:.4f} pounds.")
print(f"{kg_2} kilograms is approximately {lb_2:.4f} pounds.")
print(f"{kg_3} kilograms is approximately {lb_3:.4f} pounds.")
print(f"{kg_4} kilograms is approximately {lb_4:.4f} pounds.")
print(f"{kg_5} kilograms is approximately {lb_5:.4f} pounds.")
