import re
import json

def task_1(line):  # find_most_common_word
    word = line.split()
    word_counts = {}
    for word in word:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    most_common_word = max(word_counts)
    count = word_counts[most_common_word]
    return most_common_word, count


with open("Less_8_Task_1_input.txt.", "r") as file:
    lines = file.readlines()

with open("Less_8_Task_1_output.txt", "w") as output_file:
    for line in lines:
        line = line.strip()
        most_common_word, count = task_1(line)
        output_file.write(f"{most_common_word} - Count: {count}\n")


def task_2(file_name, stop_words_file):  # censor_text
    with open(stop_words_file, 'r', encoding='utf-8') as stop_words_file:
        stop_words = stop_words_file.read().split()

    with open(file_name, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    for word in stop_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)

    return text


stop_words_file = 'Less_8_Task_2_stop_words.txt'
file_name = 'Less_8_Task_2_for_censor.txt'

print(f"\nTask_2.The censored tex is as follows:\n{task_2(file_name, stop_words_file)}")


def task_3(file):  # students grades
    with open(file, 'r') as students_file:
        rows = students_file.readlines()
    print(f"\nTask_3. Students who have grades lower than 3 are:")
    for row in rows:
        data = row.strip().split()
        name = ' '.join(data[:-1])
        grade = int(data[-1])

        if grade < 3:
            print(f"{name} - grade: {grade}")


file_name = 'Less_8_Task_3_students.txt'
task_3(file_name)

def task4(file):
    with open(file, 'r') as file:
        data = file.read()

    numbers = []
    current_number = ''

    for char in data:
        if char.isdigit():
            current_number += char

        else:
            if current_number:
                numbers.append(int(current_number))
                current_number = ''

    if char.isdigit():
        numbers.append(int(current_number))

    total_sum = sum(numbers)
    return total_sum


testing_file = 'Less_8_Task_4_input.txt'
print(f"\nTask_4.Sum of all numbers is: {task4(testing_file)}")

def task5(filename): # Cezar encrypting
    with open(filename, 'r') as file:
        content = file.read()

    rus_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    eng_alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ''
    lines = content.split("\n")

    for i, line in enumerate(lines):
        shift = i + 1
        for char in line:
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

        encrypted_message += "\n"

    return encrypted_message

def task5_2(filename):
    return task5()


filename = "Less_8_Task_5_input.txt"
encrypted_text = task5(filename)
print(f"\nTask_5. Encrypted text:\n{encrypted_text}")
