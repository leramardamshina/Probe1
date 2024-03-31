import queue
import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(threading.Thread):
    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def run(self):
        print(f"Посетитель номер {self.number} покушал и ушёл.")
        time.sleep(1)
        self.table.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for customer in range(1, 21):
            time.sleep(1)
            print(f'Посетитель номер {customer} прибыл')
            self.serve_customer(customer)

    def serve_customer(self, customer_number):
        while True:
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    print(f'Посетитель номер {customer_number} сел за стол {table.number}')
                    customer = Customer(customer_number, table)
                    customer.start()
                    break
            else:
                print(f"Посетитель номер {customer_number} ожидает свободный стол")
                self.queue.put(customer_number)
                time.sleep(1)

if __name__ == '__main__':
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    cafe = Cafe(tables)

    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    customer_arrival_thread.join()
