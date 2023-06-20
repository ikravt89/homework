print("----------- TASK 1 -------------")
print("""Problem statement: 
Есть три целочисленные переменные,  вывести значения по условиям""")
var_a = int(input("Enter the value of variable 'a': "))
var_b = int(input("Enter the value of variable 'b': "))
var_c = int(input("Enter the value of variable 'c': "))
print( f"\nSum of all variables is: {var_a + var_b + var_c}")
print(f"Difference of all variables is: {var_a - var_b - var_c}")
print(f"Product of all variables is: {var_a * var_b * var_c}")
print(f"a - b + c is: {var_a - var_b + var_c}")
print(f"a * b / c is: {round(var_a * var_b / var_c, 2)}")
print(f"Remainder of (a + b) / c is: {(var_a + var_b) % var_c}")
print("\n----------- TASK 2 -------------")
print("""Problem statement:
Дан прямоугольный треугольник с катетами cat_a и cat_b.
Найти площадь треугольника и его гипотенузу.""")
cat_a = int(input("Enter the value of cat_a: "))
cat_b = int(input("Enter the value of cat_b: "))
print(f"Triangle area is: {(cat_a * cat_b) / 2}")
print(f"Triangle hypotenuse is: {round((cat_a ** 2 + cat_b ** 2) ** (1/2), 2)}")

print("\n----------- TASK 3 -------------")
print("""Problem statement: 
Дана строка, состоящая из слов, разделенных пробелами.
(Например, ‘test1 test2 test3 test4 test5’).
Определите, сколько в ней слов.""")
task_string = "test1 test2 test3 test4 test5"
task_string2 = input("If you want to use the sample words, print 'yes'. Otherwise, print your own words: ")
if task_string2 == "yes":
    print(f"\nNumber of words is: {task_string.count(' ') + 1}")
else:
    print(f"\nNumber of words is: {task_string2.count(' ') + 1}")
print("\n----------- TASK 4 -------------")
print("""Problem statement:
Дана строка. Замените в этой строке все появления буквы h на букву H,
кроме первого и последнего вхождения.Дано: ‘hhhabchghhh""")
task_string3 = "hhhabchghhh"
task_string3 = task_string3.replace('h', 'H', task_string3.count('h') - 1)
task_string3 = task_string3.replace('H', 'h', 1)
print(f"Result: {task_string3}")

print("\n----------- TASK 5 -------------")
print("""Problem statement:
Вывести символы строки по условию.""")
task_string4 = input("Enter a string value:")
print(task_string4[2])
print(task_string4[len(task_string4)-2])
print(task_string4[0:5])
print(task_string4[0:len(task_string4) - 2])
print(task_string4[0::2])
print(task_string4[1::2])
print(task_string4[::-1])
print(task_string4[::-2])
print(len(task_string4))

print("\n----------- TASK 6 -------------")
print("""Problem statement:
Дано целое число. Выведите его последнюю цифру.
Например, дано 200 - последняя цифра 0. Дано 123 - последняя цифра 3. Дано 587 - последняя 7.""")
task_int1 = int(input("Enter an integer: "))

print(f"The last number is {task_int1 % 10}")

print("\n----------- TASK 7 -------------")
print("""Problem statement:
Дано трехзначное число, найти количество его десятков. 
Например, дано 123 – количество десятков: 2, дано 978 – количество десятков: 7. 
""")
task_int2 = int(input("Enter a three-digit number: "))
print(f"Number of tens place: {(task_int2 % 100) // 10}")


print("\n----------- TASK 8 -------------")
print("""Problem statement:
Дано трехзначное число, найти сумму его цифр. 
Например, дано 123 – сумма 6, дано 555, сумма 15. 
""")

task_int3 = int(input("Enter a three-digit number: "))

print(f"Sum of all numbers is: {(task_int3 // 100) + ((task_int3 % 100) // 10) + ((task_int3 % 10))}")

