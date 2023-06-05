import math
from datetime import datetime as dt
import random

print("\n-----------TASK-1-----------")

# a)
x = math.radians(int(input(">>>Enter a number in degrees: ")))
n = 0
summa = 0
eps = 0.0001
term = 1

while eps < abs(term):
    term = (-1) ** n * (x ** (2 * n + 1)) / (math.factorial(2 * n + 1))
    n += 1
    summa += term
print(f"a) Sin(x) = {round(summa, 2)}")
# b)
n = 0
summa = 0
term = 1

while abs(term) >= eps:
    term = (-1) ** n * (x ** (2 * n)) / (math.factorial(2 * n))
    n += 1
    summa += term
print(f"b) Cos(x) = {round(summa, 2)}")

print("\n-----------TASK-2-----------")
total_money = int(input("Enter the amount of money that Masha needs: "))
daily_savings= int(input("Enter the amount of dayly savings: "))
total_savings = 0
days_count = 0
while total_savings < total_money:
    days_count += 1
    if days_count % 7 == 0:
        continue
    total_savings += daily_savings
print(f"Needed amount of days: {days_count}")
print(f"Total ammount of savings: {total_savings}")

print("\n-----------TASK-3-----------")
fibo_length = int(input(">>> Enter amount of numbers in fibonaсci series: "))
a = 1
b = 1
count = 0

while count < fibo_length:
    if b < 1:
        print(a, b, end=' ')
        a = 1
        b += a
        count = 2
    else:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

print("\n-----------TASK-4-----------")
input_str = input(">>>Enter numbers separated by space: ")
number_list = input_str.split()
number_list = [int(x) for x in number_list]
print(f"Cool! Now yor list is:\n{number_list}")
biggest_number = number_list[0]
lowest_number = number_list[0]
sum = 0

for a in number_list:
    sum += a
    if a > biggest_number:
        biggest_number = a
    if a < lowest_number:
        lowest_number = a

print(f"Biggest number is: {biggest_number}")
print(f"Lowest number is: {lowest_number}")
print(f"Sum of all numbers in list is: {sum}")

print("\n-----------TASK-5-----------")
input_str2 = input(">>>Enter numbers separated by space: ")
number_list2 = input_str2.split()
number_list2 = [int(x) for x in number_list2]
print(f"Awesome! Now your list is:\n{number_list2}")
pos_counter_a = 0
pos_counter_b = 0

unique_values = []
for a in number_list2:
    pos_counter_b = 0
    for b in number_list2:
        if pos_counter_a == pos_counter_b:
            pos_counter_b += 1
            continue
        if a == b and a not in unique_values:
            unique_values.append(a)
        pos_counter_b += 1
    pos_counter_a += 1
if len(unique_values) == 0:
    print("All values in your list are unique!")
else:
    print("And your list has some repeating numbers: ")
    for z in unique_values:
        if number_list2.count(z) > 1:
            print(f"Number {z} repeated {number_list2.count(z)} times")

print("\n-----------TASK-6-----------")
sorted_list = sorted(random.sample(range(1, 100), 20))
print(f"The random-generated list is: {sorted_list}")
target_number = int(input("Enter the integer number in list range: "))

left_border = 0
right_border = len(sorted_list) - 1
position = len(sorted_list) + 1

while left_border <= right_border:
    mid = (left_border + right_border) // 2
    mid_value = sorted_list[mid]

    if mid_value == target_number:
        position = mid
        break
    elif mid_value < target_number:
        left_border = mid + 1
    else:
        right_border = mid - 1
print("The target element", target_number, "located at position", position)

print("\n-----------TASK-7-----------")
random_list = sorted(random.sample(range(1, 1000), 20))
shift = random.randint(1, len(random_list) - 1)
shifted_list = random_list[shift:] + random_list[:shift]
print(f"The random-generated shifted list is: {shifted_list}")
target_number = int(input("Enter the integer number in list range: "))

if shifted_list[len(shifted_list) - 1] > target_number:
    left_border = shifted_list.index(min(shifted_list))
    right_border = len(shifted_list) - 1
else:
    left_border = 0
    right_border = shifted_list.index(min(shifted_list)) - 1

position = len(shifted_list) + 1

while left_border <= right_border:
    mid = (left_border + right_border) // 2
    mid_value = shifted_list[mid]

    if mid_value == target_number:
        position = mid
        break
    elif mid_value < target_number:
        left_border = mid + 1
    else:
        right_border = mid- 1
print("The target element", target_number, "located at position", position)