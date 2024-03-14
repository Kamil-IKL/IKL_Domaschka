print('Создаем бесконечный цикл')

while True:
    number_1 = int(input('\nВведите первое число: '))
    number_2 = int(input('Введите второе число: '))
    print('Сумма чисел: ', number_1 + number_2)
    str = (input('Нажмите Y или y для заверешения программы: '))
    if str == 'Y' or str == 'y':
        break


print('\nПоздравляю, Вы вышли из бесконечного цикла')
