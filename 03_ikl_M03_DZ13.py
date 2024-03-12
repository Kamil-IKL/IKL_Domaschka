def print_params(a=1, b='Cтрока', c=True):
    print(f'Функция, где: a={a}, b={b}, с={c}')


#print_params()                         # по умолчанию
#print_params(b=25)                     # изменили параметр b
#print_params()                         # проверка "по умолчанию"
#print_params(a='Камиль')               # изменили параметр a
#print_params(c=[1, 2, 3])              # изменили параметр c, ввели список
#print_params(25,40,[1, 2, 3]) # изменили все параметры
#print_params()                         # проверка "по умолчанию"
# print_params(15, 50, 57, '4 параметр') # ругается, т.к. по умолчанию указано только три параметра

values_list = ['Номер', 'Цвет', 102]
print_params(*values_list)
values_dict = {'a':'Номер', 'b':'Цвет', 'c':'Политра'}
print_params(**values_dict)
