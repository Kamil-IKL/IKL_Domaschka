print(f'{"Задача 1: Фабрика Функций ":=<70}')
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.

def create_operation(operation):
    if operation == "fission" or operation == '/':  # для разного типа вызова этой функции
        def fission(x, y):
            return x / y

        return fission  # возвращаю как объект, а не как функцию

    elif operation == 'multiplication' or operation == '*':  # тоже самое (для разного типа вызова)
        def multiplication(x, y):
            return x * y

        return multiplication  # возвращаю как объект, а не как функцию

    elif operation == "square" or operation == "**":  # добавил функцию для выполнения второго задания (см. ниже)
        def square(x):
            return x ** 2

        return square  # возвращаю как объект, а не как функцию


print(f'\n{" Операция деления(fission) ":/^70}')
my_func = create_operation('fission')
print(my_func(20, 2))

my_func = create_operation('/')
print(my_func(x=int(input('Enter X = ')), y=int(input('Enter Y = '))))  # сделал через запрос аргументов

print(f'\n{" Операция умножение(multiplication) ":*^70}')
my_func = create_operation('multiplication')
print(my_func(20, 2))

my_func = create_operation('*')
print(my_func(x=int(input('Введите X = ')), y=int(input("Введите Y = "))))  # сделал через запрос аргументов



print(f'\n{"Задача 2: Лямбда-Функции ":=<70}')
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию
# с использованием def. Например, возведение числа в квадрат

print(f'\n{" Операция возведение в квадрат(**) ":2^70}')
My_list = list(map(int, input('Введите числовой список: ').split()))
print(f'Созданный список {My_list}')

res = map(lambda x: x ** 2, My_list)
print(f'Новый список {list(res)} использовал функцию лямбда')

my_func_1 = create_operation('**')
res = map(my_func_1, My_list)
print(f'Новый список {list(res)} использовал свою функцию "square"')



print(f'\n{"Задача 3: Вызываемые Объекты ":=<70}')
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

class Rect:
    def __init__(self):
        self.a = a = int(input('Введите сторону a = '))
        self.b = b = int(input('Введите сторону b = '))

    def __call__(self):
        # self.b = b = int(input('Введите сторону b = ')) " устал к вечеру, вот и написал сюда, а  надо было в инит (что и сделал)
        return self.a * self.b


my_func_2 = Rect()
print(f'Площадь прямоугольника равна {my_func_2()}')
