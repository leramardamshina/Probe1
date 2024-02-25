#Задача 1: Фабрика Функций
#Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
#в зависимости от переданных аргументов.
#Решение 1:
def func(n):
    if n == 2:
        def func1(x):
            return x / 2
    elif n == 0:
        def func1(x):
            return x / 0
    else:
        raise Exception ("Делить на ноль нельзя!")

    return func1

my_numbers = [2,4,6,7,8]

func_1 = func(n=2)
result = map(func_1, my_numbers)
print(list(result))

func_2 = func(n=0)
result = map(func_2, my_numbers)
print(list(result))

#Решение 2:
def create_operation(operation):
    if operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply

    elif operation == "division":
        def division(x, y):
            return x / y
        return division
    else:
        raise Exception ("Делить на ноль нельзя!")

func_multiply = create_operation("multiply")
print(func_multiply(72,15))

func_multiply = create_operation("multiply")
print(func_multiply(7,15))

func_division = create_operation("division")
print(func_division(2,0))

#Задача 2: Лямбда-Функции
#Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
#Например, возведение числа в квадрат

add = lambda x,y: x + y
print (add(x=11,y=45))

def add(x,y):
    return x + y
print(add(5,2))

#Задача 3: Вызываемые Объекты
#Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
#который возвращает площадь прямоугольника, то есть a*b.
class Multiply:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return b * self.a

sqr = Multiply(a=5)
result = sqr(b=4)
print(result)





