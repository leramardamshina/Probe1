import queue
import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self): #моделирует приход посетителя(каждую секунду)
        for i in range(1, 21):
            time.sleep(1)
            print(f'Посетитель номер {i} прибыл')
            customer = Customer(i, self)
            customer.start()

    def serve_customer(self, customer): #моделирует обслуживание посетителя.
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.customer_number} сел за стол {table.number}.")
                time.sleep(5)
                print(f"Посетитель номер {customer.customer_number} покушал и ушёл.")
                table.is_busy = False
                return
        print(f"Посетитель номер {customer.customer_number} ожидает свободный стол")
        self.queue.put(customer)

class Customer(threading.Thread): #Запускается, если есть свободные столы
    def __init__(self,customer_number, cafe):
        super().__init__()
        self.customer_number = customer_number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)

if __name__ == '__main__':
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    cafe = Cafe(tables)

    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()