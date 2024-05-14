def print_params(a=1, b='srting', c=True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [5 , 'man', None]
values_dict = {'a': 9, 'b': 'value', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [7, 'brics']
print_params(*values_list2, 42)

