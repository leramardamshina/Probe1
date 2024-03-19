#Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и уходящих после
#завершения приема.
#Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят.
#Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.

#Создайте 3 класса:
#1.Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, is_busy(bool) - занят стол или нет.
#2.Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
#Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
#Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
#Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов, в случае наличия стола -
# начинает обслуживание посетителя (запуск потока), в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
#3.Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

#Так же должны выводиться текстовые сообщения соответствующие событиям:
#Посетитель номер <номер посетителя> прибыл.
#Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
#Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
#Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)


import queue
import threading
import time

class Table(threading.Thread):
    def __init__(self,number,is_busy=False):
        #super().__init__(*args,**kwargs)
        self.number = number # номер стола
        self.is_busy = is_busy
class Cafe(threading.Thread):
    def __init__(self,table):
        #super().__init__(*args,**kwargs)
        self.queue = queue.Queue()
        self.table = table

    def customer_arrival(self, customer): #моделирует приход посетителя(каждую секунду)
        for customer in range(1, 21):
            time.sleep(1)
        print(f'Посетитель {customer.number} прибыл')

    def serve_customer(self, customer): #моделирует обслуживание посетителя.
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.number} сел за стол {table.number}")
                time.sleep(5)
                print(f"Посетитель номер {customer.number} покушал и ушёл")
                table.is_busy = False
                return
        print(f"Посетитель номер {customer.number} ожидает свободный стол")
        self.queue.put(customer)

class Customer(threading.Thread):#Запускается, если есть свободные столы
    def __init__(self, customer):
        self.customer = customer



#Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

#Инициализируем кафе
cafe = Cafe(tables)

#Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

#Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
