def test_print_them_all_v1(*args):
    print('test_print_them_all_v1')
    print('тип args:', type(args))
    print(args)
    for k, args in enumerate(args):
        print('позиционный параметр:', k, args)
test_print_them_all_v1(5, 'sos', 3.14)





