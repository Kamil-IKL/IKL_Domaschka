# Распаковка параметров:
def print_params(a=1, b='Cтрока', c=True):
    return (f'Функция, где: a={a}, b={b}, с={c}')


print(f'{print_params()}        # функция по умолчанию\n')

values_list = [False, 'Цвет', 102]      # создаю список
resul_list = print_params(*values_list) # передаю элементы списка в параметры функции)
print(resul_list)

print(f'{print_params()}        # проверка функции по умолчанию\n')

values_dict = {'a' : True, 'b' : 526, 'c' : "Цвет"} # создаю словарь
resul_dict = print_params(**values_dict) # передаю аргументы словаря в параметры функции (Учти!! не сами ключи "a,b,c")
print(resul_dict)

print(f'{print_params()}        # проверка функции по умолчанию\n')


