def test():
    a, b = 1, 2
    print('simple:', a, b)
test()


def test2 (x, y, z):
    return (x ** 2 + y ** 2 + z ** 2) ** 3
res = test2 (2,4,6)
print(res)
