import math

#TASK-1
print("---------------TASK-1----------------")
var_a = float(input("Enter the number \'a\': "))
var_b = float(input("Enter the number \'b\': "))
var_x = float(input("Enter the number \'x\': "))
print("\n--------------RESULTS----------------")
#item_a
float_result1 = ((var_a ** 2) / 3) + ((var_a ** 2 + 4) / var_b) + (((var_a ** 2 + 4)) ** (1 / 2)) / 4 + \
                (((var_a ** 2 + 4)** 3) ** (1/2)) / 4
print(f"Item a) result is: {round(float_result1, 2)}")
#item_b
float_result2 = (math.cos(var_x) + math.sin(var_x))
print(f"Item b) result is: {round(float_result2, 2)}")
#item_c
float_result3 = (((math.cos(var_x ** 2)) ** 2) + (((math.sin(2 * var_x - 1))) ** 2)) ** (1 / 3)
print(f"Item c) result is: {round(float_result3, 2)}")
#item_d
float_result4 = (5 * var_x) + (3 * (var_x ** 2)) *((1 + (math.sin(var_x) ** 2)) ** (1 / 2))
print(f"Item d) result is: {round(float_result4, 2)}")
#TASK-2

print("\n---------------TASK-2----------------")
print("Let's count monthly payment for your credit")
print("Please enter the values for the following credit terms")
print("-------------------------------------")
annual_interest_rate = float(input("Annual interest rate is (only number): "))
loan_amount = int(input("Total loan amount is: "))
loan_term = int(input("Loan term in months is: "))
monthly_payment = (loan_amount * ((annual_interest_rate/12) / 100) *
                   ((1 + (annual_interest_rate / 12 / 100)) ** loan_term)) / (((1 + (annual_interest_rate / 12 / 100))
                                                                               ** loan_term) - 1)
print("\n--------------RESULTS----------------")
print(f">>>Your monthly payment will consist of: ${round(monthly_payment, 2)}")
print(f">>>The total amount of payments will be: ${round(monthly_payment * loan_term, 2)}")
print(f">>>The overpayment on the loan will be: ${round((monthly_payment * loan_term) - loan_amount, 2)}")

# TASK-3
print("\n-----------------TASK-3--------------")
print("Now let's compare duration of one year on two planets\nPlease enter the values of the following terms")
print("-------------------------------------")
orb_radius1 = float(input(f"The orbital radius of the first planet (million kilometers) is: "))
orb_radius2 = float(input(f"The orbital radius of the second planet (million kilometers) is: "))
orb_velocity1 = float(input(f"The orbital velocity of the first planet (km/s) is: "))
orb_velocity2 = float(input(f"The orbital velocity of the second planet (km/s) is: "))
year_duration1 = ((2 * math.pi * (orb_radius1 * (10 ** 6)) / orb_velocity1) / (86.4 * 10 ** 3))
year_duration2 = ((2 * math.pi * (orb_radius2 * (10 ** 6)) / orb_velocity2) / (86.4 * 10 ** 3))
print("\n---------------RESULTS-----------------")
print(f">>>The duration of a year on the first planet (in days) is: {round(year_duration1)}")
print(f">>>The duration of a year on the second planet (in days) is: {round(year_duration2)}")
print(f">>>Is the duration of the year on the first planet longer than on the second planet? "
      f"{bool(year_duration1 > year_duration2)}")
