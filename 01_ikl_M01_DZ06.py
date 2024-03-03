my_list = ["яблоко", "груша", "киви", "апельсин", "банан", "вишня", "абрикос", "слива"]
print(my_list, type(my_list), id(my_list))
print(f'Первый элемент списка: ',my_list[0],'\nПоследний элемент списка: ',my_list[-1])
print(f'С 3-его по 5-ый эелементы списка включительно: ',my_list[2:5])
my_list.pop(2),my_list.insert(2,'черешня')
print(my_list, id(my_list))

print('\n**************************************************\n')
my_dict = {}
print(my_dict, type(my_dict))
my_dict['name'] = 'Имя'
my_dict['age'] = "Возраст"
my_dict['place of birth'] = 'Место рождения'
my_dict['nationality'] = "Гражданство"
print(my_dict, id(my_dict))
print(f'Вывожу по ключу "age" значение: ',my_dict.get('age'))
my_dict.setdefault(input(f'Введите "Ваш пол" по английски: '),'Ваш пол')
print(my_dict, id(my_dict))