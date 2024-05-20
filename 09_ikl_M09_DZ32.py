# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.


def all_variants(*args):
    my_data = str(*args).upper() # создал строку и применил метод (все заглавные). Внимание!!! обязательно * перед args
    print(f'Строка для перебора: {my_data}') # для проверки, что в итоге будет интерировать(перебирать)
    for start in range(len(my_data)): # количество итераций(переборов) по длине строки
        for end in range(start + 1, len(my_data) + 1):
            yield my_data[start:end] # создал генератор



a = all_variants('краз')
print(type(a))
for i in a:
    print(i)
