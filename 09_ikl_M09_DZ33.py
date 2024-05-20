# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет
# простым числом и "Составное" в противном случае.


# Это скелет простого декаратора
# def my_dec(func):
#     def wrapper():
#         func()
#     return wrapper

# @my_dec # указываем функции в которую будем вписывать функцию декаратор
# def check(): # это функция декаратор
#     print(f'\n{" Привет Камиль ! ":+^40}\n')
#
# check()


# Сначала написал скелет декаратора
def is_prime(func):
    def wrapper(*args, **kwargs):
        print(f'{"Перед декаратором ":=<40}\n')
        func()
        print(f'\n{" После декаратора":*>40}')

    return wrapper


@is_prime
def sum_three():
    My_list = list(map(int, input('Введите числовой список: ').split()))  # создаю список, используя запрос и map
    print(f'Созданный список {My_list}')
    res = sum(My_list)
    if res % 2 == 0:
        print(f'Сумма чисел = {res} и это составное число')
    else:
        print(f'Сумма чисел = {res} и это простое число')


sum_three()
