#Напишите 2 функции:
#Функция которая складывает 3 числа (sum_three)
#Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

#Не забудьте написать внутреннюю функцию wrapper в is_prime
#Функция is_prime должна возвращать wrapper
#@is_prime - декоратор для функции sum_three

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    return
            print(str(result) + " Простое")
        else:
            print(str(result) + " Составное")
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
