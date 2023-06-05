import random
from pprint import pprint


def first_task(arr, target, low, high) -> int:  # binary search
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return first_task(arr, target, low, mid - 1)

    else:
        return first_task(arr, target, mid + 1, high)


lst_len = int(input("Task 1. Enter the length of the randomly generated list: "))
rnd_list = sorted(random.sample(range(1, 20000), lst_len))
print(f"Yor list is:\n{rnd_list}")
target_nmbr = int(input(f"Choose a number within the range of the list: "))
low = 0
high = len(rnd_list) - 1

result = first_task(rnd_list, target_nmbr, low, high)
print(f"Position of searching element is: {result} ")


def second_task(number):  # Binary converter
    if number // 2 == 0:
        binary_number.append(number % 2)
        return ''.join(map(str, binary_number[::-1]))

    elif number // 2 != 0:
        binary_number.append(number % 2)
        number = number // 2
        return second_task(number)


binary_number = []
decimal_number = int(input("\nTask 2. Enter the digit number that needed to convert to binary format: "))
print(f"The binary format of your number is: {second_task(decimal_number)}")


def task_3(num):  # Prime tester
    if num in [-2, 2]:
        return "The number is a prime"

    elif num == 1 or num % 2 == 0 or num % 3 == 0:
        return "The number is NOT a prime"

    else:
        return "The number is a prime"


testing_num = int(input("\nTask 3. Enter the number that needs to be checked: "))
print(task_3(testing_num))


def task4(num1: int, num2: int) -> int:  # To find the greatest common divisor
    if num1 >= num2:
        remainder = num1 % num2
        divisor = num2

        if remainder == 0:
            return abs(divisor)

        elif num2 % remainder == 0:
            divisor = remainder
            return abs(divisor)

        else:
            remainder, num2 = num2 % remainder, remainder
            return task4(num2, remainder)
    else:
        return task4(num2, num1)


first_num = int(input("\nTask 4. Enter the first integer number: "))
second_num = int(input("Enter the second integer number: "))

print(f"The greatest common divisor of this numbers is: {task4(first_num, second_num)}")


def task5(message: str, shift) -> str:  # Cezar encrypting
    rus_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    eng_alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ''
    for char in message:

        if char.lower() in rus_alpha:
            is_upper = char.isupper()
            char_index = (rus_alpha.index(char.lower()) + shift) % len(rus_alpha)
            encrypted_char = rus_alpha[char_index]

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_message += encrypted_char

        elif char.lower() in eng_alpha:
            is_upper = char.isupper()
            char_index = (eng_alpha.index(char.lower()) + shift) % len(eng_alpha)
            encrypted_char = eng_alpha[char_index]

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_message += encrypted_char

        else:
            encrypted_message += char

    return encrypted_message


def task5_2(message: str, shift) -> str:  # Cezar decrypting
    return task5(message, -shift)


message = input("\nTask 5. Enter the message: ")
shift = int(input("Enter the shift for encrypt/decrypt(integer): "))
action = int(input("Choose an action.'1' to encrypt, '2' to decrypt: "))

if action == 1:
    print(f"Encrypted result is: {task5(message, shift)}")
elif action == 2:
    print(f"Decrypted result is: {task5(message, -shift)}")
else:
    print('Something is wrong with choose action. Try it again')


def task6_1(message: str, key: str) -> str:  # Vigenere encrypting
    rus_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    eng_alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ''
    index = 0
    for char in message:

        if char.lower() in rus_alpha:
            is_upper = char.isupper()
            char_index = (rus_alpha.index(char.lower()) + rus_alpha.index(key[index])) % len(rus_alpha)
            encrypted_char = rus_alpha[char_index]

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_message += encrypted_char
            index = (index + 1) % len(key)

        elif char.lower() in eng_alpha:
            is_upper = char.isupper()
            char_index = (eng_alpha.index(char.lower()) + eng_alpha.index(key[index])) % len(eng_alpha)
            encrypted_char = eng_alpha[char_index]

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_message += encrypted_char
            index = (index + 1) % len(key)

        else:
            encrypted_message += char

    return encrypted_message


def task6_2(message, key):  # Vigenere decrypting
    rus_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    eng_alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ''
    index = 0
    for char in message:

        if char.lower() in rus_alpha:
            is_upper = char.isupper()
            char_index = (rus_alpha.index(char.lower()) - rus_alpha.index(key[index])) % len(rus_alpha)
            encrypted_char = rus_alpha[char_index]

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_message += encrypted_char
            index = (index + 1) % len(key)

        elif char.lower() in eng_alpha:
            is_upper = char.isupper()
            char_index = (eng_alpha.index(char.lower()) - eng_alpha.index(key[index])) % len(eng_alpha)
            encrypted_char = eng_alpha[char_index]

            if is_upper:
                encrypted_char = encrypted_char.upper()

            encrypted_message += encrypted_char
            index = (index + 1) % len(key)

        else:
            encrypted_message += char

    return encrypted_message


message = input("\nTask 6. Enter the message: ")
key = input("Enter the key word in the same language: ")
action = int(input("Choose an action.'1' to encrypt, '2' to decrypt: "))

if action == 1:
    print(f"Encrypted result is: {task6_1(message, key)}")
elif action == 2:
    print(f"Decrypted result is: {task6_2(message, key)}")
else:
    print('Something is wrong with choose action. Try it again')


def task7(M, N):  # randomly generating matrix
    matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
    return matrix

print("Task 7. Randomly generated matrix is: ")
pprint(task7(5, 5))

def task8(matrix: list) ->list: # Finding min and max values in a matrix
    rows = len(matrix)
    cols = len(matrix[0])

    min_value = matrix[0][0]
    max_value = matrix[0][0]
    min_index = (0, 0)
    max_index = (0, 0)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)

    return min_index, max_index


matrix = task7(5,5)
min_index, max_index = task8(matrix)

print('\nTask 8')
pprint(matrix)

print("Min value:", matrix[min_index[0]][min_index[1]], "Index:", min_index)
print("Max value:", matrix[max_index[0]][max_index[1]], "Index:", max_index)

def task9(matrix):  # Sum of the rows in matrix
    total_sum = sum(sum(row) for row in matrix)
    column_percent = []

    for column in range(len(matrix[0])):
        column_sum = sum(row[column] for row in matrix)
        percent = round(((column_sum / total_sum) * 100), 2)
        column_percent.append(percent)
    return column_percent, total_sum


print("\nTask 9")
pprint(matrix)
column_percent, total_sum = task9(matrix)
print(f"Total sum is: {total_sum}")
print(f"Percentages of row sums relative to the total sum {column_percent}")

def task12(matrix, number):
    columns_with_num = []
    columns_without_num = []

    for column in range(len(matrix[0])):
        has_number = False

        for row in matrix:
            if number == row[column]:
                has_number = True

        if has_number == True:
            columns_with_num.append(column)
        else:
            columns_without_num.append(column)

    return columns_with_num, columns_without_num


print("\nTask 12")
pprint(matrix)
number = int(input("Print number that are present in matrix: "))
column_with_num, column_without_num = task12(matrix, number)
print(f"Columns with the desired number: {column_with_num}")
print((f"Columns without the desired number: {column_without_num}"))

def task13(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    main_diagonal_sum = 0
    side_diagonal_sum = 0

    for i in range(len(matrix)):
        main_diagonal_sum += matrix[i][i]
        side_diagonal_sum += matrix[i][cols - i - 1]

    return main_diagonal_sum, side_diagonal_sum

print("\nTask 13")
pprint(matrix)

main_diagonal_sum, side_diagonal_sum = task13(matrix)
print(f"Sum of the numbers in the main diagonal: {main_diagonal_sum}")
print((f"Sum of the numbers in the main diagonal: {side_diagonal_sum}"))

def task14(matrix):  # make_even
    new_matrix = []
    for row in matrix:

        count_ones = sum(row)

        if count_ones % 2 != 0:
            row.append(1)
        else:
            row.append(0)

        new_matrix.append(row)

    return new_matrix


matrix = [[random.randint(0, 1) for i in range(5)] for i in range(5)]
print("\nTask 14\nRandomly generated matrix is: ")
pprint(matrix)

new_matrix = task14(matrix)
print(f"Thw new matrix with even sum in rows is as follows: ")
pprint(new_matrix)
