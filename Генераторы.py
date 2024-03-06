#Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
#В функцию передаётся только сама строка.

def all_variants(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n) + 1):
            yield n[i:j]

a = all_variants(n="abc")
for i in a:
    print(i)