# Функция с параметрами по умолчанию:
def print_params(a=1, b='Cтрока', c=True):
    return (f'Функция, где: a={a}, b={b}, с={c}')

print(f'{print_params()}       # по умолчанию')
print(f'{print_params(b=25)}           # изменили параметр b')
print(f'{print_params()}       # проверка "по умолчанию"')
print(f'{print_params(a='Камиль')}  # изменили параметр a')
print(f'{print_params(c=[1, 2, 3])}  # изменили параметр c, ввели список')
print(f'{print_params(25,40,[1, 2, 3])}     # изменили все параметры')
print(f'{print_params()}       # проверка "по умолчанию"')
# print_params(15, 50, 57, '4 параметр') # ругается, т.к. по умолчанию указано только три параметра


