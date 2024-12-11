"""
    This program will ask for monthly take home income, amount spent in each of the categories below,
    calculate the percentage of the total budget spent in each of the categories below, and report the findings.
    Housing 
    Utilities
    Groceries
    Transportation
    Health Care
    Personal Care
    Clothing
    Debt
    Note: dollar and cents format is necessary because we have not been taught error catching up to this point.
"""
# variables and input of costs

print("This program will help calculate what percentage of the budget each category is.")
print("Please enter all monetary amounts using dollar and cents numeric format:  000.00")
budget_total = float(input("\nPlease enter your monthly take home income:  "))
housing_cost = float(
    input("\nPlease enter the amount spent for housing cost:  "))
utilities_cost = float(
    input("Please enter the amount spent for utilities cost:  "))
groceries_cost = float(
    input("Please enter the amount spent for groceries cost:  "))
transportation_cost = float(
    input("Please enter the amount spent for transportation cost:  "))
health_care_cost = float(
    input("Please enter the amount spent for health care cost:  "))
personal_care_cost = float(
    input("Please enter the amount spent for personal care cost:  "))
clothing_cost = float(
    input("Please enter the amount spent for clothing cost:  "))
debt_cost = float(input("Please enter the amount spent for debt cost:  "))

# calculate each category percentage of the budget

housing_percent = (housing_cost / budget_total) * 1e2
utilities_percent = (utilities_cost / budget_total) * 1e2
groceries_percent = (groceries_cost / budget_total) * 1e2
transportation_percent = (transportation_cost / budget_total) * 1e2
health_care_percent = (health_care_cost / budget_total) * 1e2
personal_care_percent = (personal_care_cost / budget_total) * 1e2
clothing_cost_percent = (clothing_cost / budget_total) * 1e2
debt_percent = (debt_cost / budget_total) * 1e2

# print monthly total budget and each category percentage of the budget

print(f"\nYour total monthly budget: ${budget_total:.2f}")
print("\nCategory percentages of the Monthly Budget" + "\n" + "-" * 42)
print(f"${housing_cost:.2f} spent for housing is around {
      housing_percent:.2f}% ")
print(f"${utilities_cost:.2f} spent for utilities is around {
      utilities_percent:.2f}% ")
print(f"${groceries_cost:.2f} spent for groceries is around {
      groceries_percent:.2f}% ")
print(f"${transportation_cost:.2f} spent for transportation is around {
      transportation_percent:.2f}% ")
print(f"${health_care_cost:.2f} spent for health care is around {
      health_care_percent:.2f}% ")
print(f"${personal_care_cost:.2f} spent for personal care is around {
      personal_care_percent:.2f}% ")
print(f"${clothing_cost:.2f} spent for clothing is around {
      clothing_cost_percent:.2f}% ")
print(f"${debt_cost:.2f} spent for debt is around {debt_percent:.2f}% ")
