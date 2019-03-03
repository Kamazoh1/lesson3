import csv

employees = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}]

with open('employees.csv', 'w', encoding='utf-8', newline='') as emp_file:
    field_headers = ['name', 'age', 'job']
    writer = csv.DictWriter(emp_file, field_headers, delimiter=';')
    writer.writeheader()
    for employee in employees:
        writer.writerow(employee)
    