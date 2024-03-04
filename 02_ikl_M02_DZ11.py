print('**** Вариант01 ****')
def print_params_01():  # самая простая функция
    print('Привет', 'Привет')
print_params_01()
print_params_01()
print_params_01()
print('\n**** Вариант 02 ****')


def print_params_02(*args):  # функция "запрашивающая" (не помню точно, как называется)... можно вводить любой аргумент
    print(*args, *args)
print_params_02('Kamil')
print_params_02('Акапулька')
print_params_02('mazerati')
print_params_02('Урааааа, ... Я молодчик :)')


print('\n**** Вариант 03 (попытка сделать через запрос ввода и цикл for ****')
print('Введите имя: ')  # не смог сделать в одну строку, надо думать, .... А надо ли это (в строку)?
name = input()  # количество букв в имени = количеству циклов
for i in name:
    print_params_01()
    print_params_02(name)
print('\n')  # просто первод пустой строки
print_params_01(), print_params_02('Урааааа, сам решил.. Кто молодец? ... Я молодец :)\n')
