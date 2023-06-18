import json
import csv
from datetime import datetime

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(json_data[0].keys())

        for item in json_data:
            writer.writerow(item.values())

def add_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    is_empty = not is_csv_exists(csv_file)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        if is_empty:
            writer.writerow(json_data[0].keys())

        for item in json_data:
            writer.writerow(item.values())


def is_csv_exists(csv_file):
    # Проверяем, существует ли CSV-файл и имеет ли он данные
    try:
        with open(csv_file, 'r') as file:
            return bool(file.read().strip())
    except FileNotFoundError:
        return False

json_file = 'employees.json'
csv_file = 'output.csv'
convert_json_to_csv(json_file, csv_file)

def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%d.%m.%Y')
    raise TypeError("Type not serializable")

def add_employee(json_file):
    with open(json_file, 'r') as file:
        employees = json.load(file)

    employee = {}
    employee['name'] = input("Enter the employee's name: ")
    employee['birthday'] = datetime.strptime(input("Enter the employee's date of birth (DD.MM.YYYY): "), '%d.%m.%Y')
    employee['weight'] = float(input("Enter the employee's weight: "))
    employee['height'] = float(input("Enter the employee's height: "))
    employee['car'] = input("Does the employee have a car? (True/False): ").lower() == 'true'
    languages = input("Enter the languages separated by commas: ").split(',')
    employee['languages'] = [language.strip() for language in languages]

    employees.append(employee)

    with open(json_file, 'w') as file:
        json.dump(employees, file, indent=4, default=datetime_serializer)

    print("Information about new employee has been successfully added to the JSON file.")

def add_employee_to_csv(csv_file):
    employee = {}
    employee['name'] = input("Enter the employee's name: ")
    employee['birthday'] = datetime.strptime(input("Enter the employee's date of birth (DD.MM.YYYY): "), '%d.%m.%Y')
    employee['weight'] = float(input("Enter the employee's weight: "))
    employee['height'] = float(input("Enter the employee's height: "))
    employee['car'] = input("Does the employee have a car? (True/False): ").lower() == 'true'
    languages = input("Enter the languages separated by commas: ").split(',')
    employee['languages'] = [language.strip() for language in languages]

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(employee.values())

    print("Information about the new employee has been added successfully.")

def search_employee_by_name(json_file):
    name = input("Enter the employee's name to search: ")

    with open(json_file, 'r') as file:
        json_data = json.load(file)

        found = False
        for employee in json_data:
            if employee['name'] == name:
                print("Employee found:")
                print("Name:", employee['name'])
                print("Birthday:", employee['birthday'])
                print("Weight:", employee['weight'])
                print("Height:", employee['height'])
                print("Car:", employee['car'])
                print("Languages:", ", ".join(employee['languages']))
                found = True
                break

        if not found:
            print("Employee not found.")

def language_filter(json_file, language):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    filtered_employees = []
    for employee in json_data:
        languages = [lang.lower() for lang in employee['languages']]
        if language.lower() in languages:
            filtered_employees.append(employee['name'])

    return filtered_employees

def filter_by_birth_year(json_file):
    birth_year = int(input("Enter the birth year: "))

    with open(json_file, 'r') as file:
        json_data = json.load(file)

    filtered_employees = [employee for employee in json_data if int(employee['birthday'].split('.')[-1]) < birth_year]
    if not filtered_employees:
        print("No employees found with birth year less than", birth_year)
        return

    heights = [employee['height'] for employee in filtered_employees]
    average_height = sum(heights) / len(heights)
    print("Average height of employees with birth year less than", birth_year, ":", average_height)

json_file = 'employees.json'
csv_file = 'output.csv'

while True:
    print("Menu:")
    print("1. Convert JSON to CSV")
    print("2. Add employee to JSON")
    print("3. Add employee to CSV")
    print("4. Search employee by name")
    print("5. Language filter")
    print("6. Filter by birth year and average height")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        convert_json_to_csv(json_file, csv_file)
    elif choice == '2':
        add_employee(json_file)
    elif choice == '3':
        add_employee_to_csv(csv_file)
    elif choice == '4':
        search_employee_by_name(json_file)
    elif choice == '5':
        language = input("Enter the language to filter: ")
        result = language_filter(json_file, language)
        print("Filtered employees:", result)
    elif choice == '6':
        filter_by_birth_year(json_file)
    elif choice == '0':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
