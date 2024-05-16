# Входные данные
My_List = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def my_square(x):
    return x ** 2


def my_odd_numbers(x):
    return x % 2


# использую функцию map
print(f'\n {' Вариант 1, функция "map"':*^70}')
res = map(lambda x: x ** 2, My_List)  # использую lambda - анонимная функция
print(f'Это тип объекта {type(res)} и наш новый список {list(res)}')

print(f'\n {'Вариант 2, функция "map" (использую свои функции)':*^70}')
res = sorted(map(my_square, My_List)) # дополнительно упорядочил по возрастанию (sorted)
print(f'Это тип объекта {type(res)} и наш новый список {list(res)}')

res = map(my_odd_numbers, My_List)
print(f'Это тип объекта {type(res)} и наш новый список четных и нечетных чисел {list(res)}')

# использую функцию filter - осуществляет выборку из моего списка с учетом заданных условий
print(f'\n {" Вариант 1, функция filter ":*^70}')
res = filter(lambda x: 5 < x < 100, My_List)  # использую lambda - анонимная функция
print(f'Это тип объекта {type(res)} и наш новый список {list(res)}')

print(f'\n {" Вариант 2, функция filter (свои функции) ":*^70}')
res = filter(my_odd_numbers, My_List)
print(f'Это тип объекта {type(res)} и наш новый список {list(res)}')

# использование функций map и filter
print(f'\n {" Одновременное использование функций map и filter ":*^70}')
res = map(my_square, filter(my_odd_numbers, My_List))
print(f'Ответ: наш новый список {list(res)} и тип объекта {type(res)}')

print(f'\n {"Cписковая сборка - аналог функции map и filter":*^70}')
res = [x ** 2 for x in My_List if x % 2]
print(res, type(res))
