#Импортируйте модуль warnings.
#Реализуйте функцию для расчёта деления, которая будет генерировать предупреждение, если делитель близок к нулю
#(например, меньше 0.01), предупреждая об опасности деления на ноль.
#Сгенерируйте UserWarning в этом случае.
#Используйте разные фильтры для управления поведением программы при появлении такого предупреждения: always, ignore, error

import warnings

class Generate:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2
    def division(self):

        if self.num2 < 0.01:
            warnings.warn("предупреждение об опасности деления на ноль",UserWarning)
        elif self.num2 > 0.01:
            result = self.num1 / self.num2
            print(f"продолжаем деление. Результат: {result}")


gen = Generate(num1=10,num2=0.001)
gen.division()

print('Пример: фильтр "always"')
warnings.simplefilter("always", UserWarning)
gen.division()

print('Пример: фильтр "ignore"')
warnings.simplefilter("ignore", UserWarning)
gen.division()

print('Пример: фильтр "error"')
warnings.simplefilter("error", UserWarning)
gen.division()
