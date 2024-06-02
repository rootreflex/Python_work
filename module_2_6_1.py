print('"Распаковка параметров и параметры функции"')
print("")

def print_params (a = 1, b = 'строка', c = False):
   print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
Vector = 'Best repair service'
values_list = [[1,2,3], 'Vector', True]
values_dict = {'a': 1, 'b': 2, 'c': True}
values_list_2 = [bool, "football"]
print(type(values_dict))
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

print("")
print("")
print("Created by VectorⓇ")