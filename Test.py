import json
import csv
from datetime import datetime

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