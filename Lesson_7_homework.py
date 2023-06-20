from typing import List
from functools import reduce
import timeit
import time

def task_4 (func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {func.__name__}: {execution_time} sec")
        return result
    return wrapper


@task_4
def Task_1(*args) -> list:
    string_numbers = list(map(str, numbers))
    return string_numbers

numbers = []
n = int(input("Enter the number of values: "))

for i in range(n):
    num = int(input("Enter the number: "))
    numbers.append(num)

print(f"Your list is{Task_1(numbers)}")

@task_4
def task_2(n: int) -> List[int]:
    numbers: List[int] = []

    for i in range(n):
        number: int = int(input(f"Enter the number {i + 1}: "))
        numbers.append(number)

    filtered_numbers: List[int] = list(filter(lambda x: x > 0, numbers))
    return filtered_numbers


n: int = int(input("Enter the number of values: "))
result: List[int] = task_2(n)
print(f"Positive numbers is: {result}")

@task_4
def task_3(strings: List[str]) -> List[str]:
    def is_palindrome(string: str) -> bool:
        return string == string[::-1]

    palindromes = list(filter(is_palindrome, strings))
    return palindromes


strings = input("Enter the testing values separated by space: ").split()
palindromes = task_3(strings)
print("Palindromes:", palindromes)


@task_4
def task_5(room):
    return room["length"] * room["width"]

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3}
]

room_areas = map(task_5, rooms)
total_area = reduce(lambda x, y: x + y, room_areas)

print("Total area:", total_area)
