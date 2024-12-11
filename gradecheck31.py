# This program will convert a numeric grade from 0-100 to a letter grade
# request the numeric grade
grade = int(input("Please enter the numeric grade:  "))

# Check if grade is between 0-100
if grade > 0 and grade < 100:
    if grade >= 90:
        letter_grade = "A"
    # Check if grade is a B
    elif grade <= 89 and grade >= 80:
        letter_grade = "B"
    # Check if grade is a C
    elif grade <= 79 and grade >= 70:
        letter_grade = "C"
    # Check if grade is a D
    elif grade <= 69 and grade >= 60:
        letter_grade = "D"
    # Below 60
    else:
        letter_grade = "F"
    print("The letter grade is: ", letter_grade)
elif grade < 0 or grade > 100:
    print("Numeric grade is out of range.")
