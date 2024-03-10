#Напишите программу, которая создает два потока.
#Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
#Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
#Оба потока должны работать параллельно.
#Примечание:
#Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации, пока процессы не завершатся.
#Для установки интервала в 1 секунду используйте функцию sleep() из модуля time, предварительно импортировав его.


import time
from threading import Thread

def numbers():
    for i in range(1,11):
        print(i, flush=True)
        time.sleep(1)

def func():
    for x in 'аbcdefghij':
        print(x, flush=True)
        time.sleep(1)

t_1 = Thread(target=numbers)
t_2 = Thread(target=func)

t_1.start()
t_2.start()

t_1.join()
t_2.join()


