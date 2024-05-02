import csv
def write_holiday_cities(first_letter):
    visited_cities = set() #уже песетили
    desired_cities = set() #хотят посетить

    with open('travel-notes.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            name, visited, desired = row
            if name.startswith(first_letter):
                visited_cities.update(visited.split(';'))
                desired_cities.update(desired.split(';'))

    all_cities = sorted(visited_cities.union(desired_cities))
    not_visited_cities = sorted(desired_cities.difference(visited_cities))

    next_city = not_visited_cities[0] if not_visited_cities else "No new cities left to visit"

    with open('holiday.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Посетили:', ', '.join(all_cities)])
        csv_writer.writerow(['Хотят посетить:', ', '.join(desired_cities)])
        csv_writer.writerow(['Никогда не были в:', ', '.join(not_visited_cities)])
        csv_writer.writerow(['Следующим городом будет:',next_city])

write_holiday_cities('L')
write_holiday_cities('R')