''' сделал через ввод текста на консоли '''
my_string = input('Введи ниже любоой текст:\n')
print(f"Длина введенной строки (текста) = {len(my_string)}")
print(my_string.upper())
print(my_string.lower())
user_my_string = (my_string.replace(' ',''))
print(f'{user_my_string}\nДлина строки (текста) без пробелов = {len(user_my_string)}')
print(f'Первый символ строки (текста) = ',my_string[0])
print(f'Последний символ строки (текста) = ',my_string[-1])
