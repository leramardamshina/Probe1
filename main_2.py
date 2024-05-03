import json

def employees_rewrite(sort_type):
    if sort_type not in ['firstName', 'lastName', 'department', 'salary']:
        raise ValueError('Bad key for sorting')

    with open('employees.json') as f:
        data = json.load(f)

    sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])

    if sort_type == 'salary':
        sorted_data = sorted(data['employees'], key=lambda x: x[sort_type], reverse=True)

    output_filename = f'employees_{sort_type}_sorted.json'
    with open(output_filename, 'w') as f:
        json.dump({'employees': sorted_data}, f, indent=4)


# Пример вызова функции для сортировки по ключу 'lastName'
employees_rewrite('lastName')
# Пример вызова функции для сортировки по другим ключам: 'firstName', 'department', 'salary'
employees_rewrite('firstName')
employees_rewrite('department')
employees_rewrite('salary')