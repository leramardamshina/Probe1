import queue
import threading
import time


class Table(threading.Thread):
    def __init__(self, number, is_busy=False):
        super().__init__()
        self.number = number
        self.is_busy = is_busy


class Cafe(threading.Thread):
    def __init__(self, tables):
        super().__init__()
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for customer_number in range(1, 21):
            new_customer = Customer(customer_number)
            print(f'Посетитель {new_customer.number} прибыл')
            time.sleep(1)
            self.serve_customer(new_customer)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}")
                time.sleep(5)
                print(f"Посетитель номер {customer.number} покушал и ушёл")
                table.is_busy = False
                return
        print(f"Посетитель номер {customer.number} ожидает свободный стол")
        time.sleep(0.5)
        self.queue.put(customer)


class Customer(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        print(f'Посетитель номер {self.number} ожидает свободный стол')


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()