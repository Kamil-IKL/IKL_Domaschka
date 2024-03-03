# Вариант01
def print_params_01():
    print('Привет', 'Привет')
print_params_01()
print_params_01()
print_params_01()

# Вариант 02
def print_params_02(*args):
    print(*args,*args)
print_params_02('Kamil')
print_params_02('Акапулька')
print_params_02('mazerati')
print_params_02('Урааааа, сам докумекал.. Кто молодец? ... Я молодец :)\n')

