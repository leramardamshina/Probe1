#Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
#При создании и инициализации объекта этого класса создаются атрибуты:
#start – начальное значение (если значение не передано, то 0)
#end – конечное значение (если значение не передано, то 1)

class EvenNumbers:
    def __init__(self, start=1, end=20, n=0):
        self.start = start
        self.end = end
        self.n = n

    def __iter__(self, n=0):
        self.n = n
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 2
            return self.start - 1

en = EvenNumbers(1,20)
for i in en:
    print(i)