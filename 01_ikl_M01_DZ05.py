print('''*******************\n Работа с кортежом\n*******************''')
immutable_var = (2, "Kamil", 24)
print(immutable_var, type(immutable_var), immutable_var[1], id(immutable_var))
print(f'''immutable_var.append(145), immutable_var.insert(1,145) - добавить не могу и это правильно (неизменяемый список)''')
print("del immutable_var[1] - удалять элементы также не могу и это правильно (неизменяемый список)")
print(immutable_var * 3, id(immutable_var))
print("immutable_var.sort() - не сортирует и это правильно (неизменяемый список)\n")

print('''*******************\n Работа со списком\n*******************''')
name = mytable_list = [2, 'Kamil', 24]
print(name, type(name), name[1], id(name))
print(name + [20], id(name))
mytable_list.append(145), print(name,id(name))
name.append('Alfia'), print(name,id(name))
name.insert(1,10), print(name,id(name))
name.append(32), name.append(1), name.append(50), name.append('ikl'), print(name, id(mytable_list))
del name[2]
print(name, id(mytable_list))
name.remove('Alfia'), name.remove('ikl'), print(name, id(name))
name.sort(),print(f'первый список с учетом сортировки по возрастанию: ',mytable_list,id(mytable_list),"\n")
name1 = mytable_list1 = ['aaaa','ffff','kkkk','bbbb']
print(name1, id(name1))
name1.append('африка'), name1.insert(1,'Камиль'), print(name1, id(name1))
''' При сортировке учитывается заглавные буквы, латинская или кириллица'''
name1.sort(reverse=True), print(f'второй список с учетом сортировки по убыванию: ',mytable_list1,id(mytable_list1),"\n")
name2 = name + name1
print(f'итоговый список: ',name2, id(name2))
name3 = name2 * 2
print(name3)
