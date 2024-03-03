name = "Камиль"
print("Мое имя:",name)
age = 52
print("Возраст:",age)
new_age = age+2
print("Новый возраст:",new_age)
is_student = True
print("Я студент и это:",is_student)

'''
Делаю в англоязычном варианте
'''
print('\n===================\nin English\n===================')
name='Kamil'
print('Name:',name)
print('Age:',age)
print('New Age:',new_age)
print('Is Student:',is_student)

print('''
-----------------------------------------------------------------------------
другой вариант вывода на консоль, используя фигурные скобки и перевод строки
-----------------------------------------------------------------------------''')
user = f" Мое имя: {name}\n Возраст: {age}\n Новый возраст: {new_age}\n Я студент: {is_student}\n"
print(user)

'''
определяюсь по типу переменной и ID
'''
print('================================\nПроверка тип переменных и их id\n================================')
name1 = type(name),id(name)
print('Тип и ID переменной Name="Камиль":',name1)
name2 = type(age),id(age)
print('Тип и ID переменной Age="Возраст":',name2)
name3 = type(new_age),id(new_age)
print('Тип и ID переменной New Age="Новый возраст":',name3)
name4 = type(is_student),id(is_student)
print('Тип и ID переменной Is Student="Я студент":',name4)
