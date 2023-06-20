second_num = float(input("Enter the first number: "))
first_num = float(input("Enter the second number: "))

width = 15
first_string = str(first_num)
second_string = str(second_num)
print(f"{second_string}".rjust(width))
print(f"* {first_string}".rjust(width))
print("--------------".rjust(width))
dot_deleted_first = first_string.replace('.', '')
dot_deleted_second = second_string.replace('.', '')
next_digit_count = 0
prod_string = ""
shift_count = 0
prev_number = 0

for a in dot_deleted_first[::-1]:
    pos_counter = 0
    for b in dot_deleted_second[::-1]:
        if a == '.' or b == '.' or a == '0':
            pos_counter += 1
            continue
        prod = int(a) * int(b)
        if pos_counter + 1 == len(dot_deleted_second):
            # print(f'Длина произведения {len(prod_number) + 1}')
            # print(f'Длина списка {len(second_list)}')
            prod_string += str((prod + next_digit_count) % 10)
            if 10 < prod + next_digit_count:
                prod_string += str((prod + next_digit_count) // 10)
            # print(f'Изменение в строке сравнения длины, теперь prod_number равно {prod_number}')
            continue
        if prod + next_digit_count >= 10:
            prod_string += str((prod + next_digit_count) % 10)
            # print(f'Произведение {prod_number}')
            next_digit_count = (prod + next_digit_count) // 10
            pos_counter += 1
        else:
            prod_string += str((prod + next_digit_count) % 10)
            pos_counter += 1
            next_digit_count = 0
    if a == '.' or b == '.':
        continue
    if len(prod_string) > 0:
        print(f"{prod_string[::-1]}{shift_count * ' '}".rjust(width))
        # print(f"Это счетчик смещения:{shift_count}")
        # print(f"Это текущее количество нулей в счетчике смещения: {str(shift_count * '0')}")
        prev_number = prev_number + int((prod_string[::-1]) + str(shift_count * '0'))
        # print(f"Это предидущее число: {prev_number}")
        shift_count += 1
    else:
        shift_count += 1

    prod_string = ""
    next_digit_count = 0
prev_number = str(prev_number)
dot_index_first_number = first_string.find(".")
dot_index_second_number = second_string.find(".")
dot_shift = ((len(first_string) - 1) - dot_index_first_number) + (len(second_string) - 1) - dot_index_second_number
print("--------------".rjust(width))
print(f"{(prev_number[0:len(prev_number) - dot_shift]) + '.' + prev_number[len(prev_number) - dot_shift:]}".rjust(width))
print(f"Check first_num * second_num = {first_num * second_num}")
