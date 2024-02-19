#Создайте новый проект или продолжите работу в текущем проекте.
#Создайте минимум два своих собственных исключения, наследуя их от класса Exception. Например, InvalidDataException и ProcessingException.
#Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
#Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
#В основной части программы вызовите эти функции и корректно обработайте

class InvalidDataException(Exception):
     pass
class ProcessingException(Exception):
     pass

class Generate:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def func(self):
        if self.age > 120:
            raise Exception("Возраст не может быть больше 120")
        elif self.age < 0:
            raise ValueError("Возраст не может быть меньше 0")
        else:
            print("Произошла неизвестная ошибка")

class Process:
    try:
        mike = Generate("Mike", 150)
        mike.func()
    except Exception as e:
        print(f"Некорректный возраст: {e}")
    except ValueError as e:
        print(f"Отрицательное значение не допустимо: {e}")
    finally:
        print("Завершено")















        #age = 12
        #print("Возраст: '{self.age}'")
    #except ZeroDivisionError:
        #(print('Строковоые значения недопустимы'))
    #except ValueError:
     #   (print('Пожалуйста, вводите вводите корректные данные'))










#file_name = 'text.txt'
#file = open(file_name, mode='rb')
#file_content=file.read()
#file.close()
#pprint(file_content)


#file_name = 'text.txt'
#with open(file_name, mode='r', encoding='utf8') as file:
 #   for line in file:
  #      print(line, end='')
#print(file.close)


