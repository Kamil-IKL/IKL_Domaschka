# что нельзя сравнивать разные типы
if '6' != 5: # Внимание! "Цифра" 6 это не цифра, а текст и значит сравниваешь текст с цифрой (подвох ! учти !),
             # т.е. даже будет '5' вместо '6' и также будет не равно. Здесь оператор "!=" - это значит "не равно".
             # Поэтому условие выполняется. При использовании других операторов - "тема" не рабочая.
             # Нельзя сравнивать разные типы данных.           
    print('успех')

#if '6' > 5: # выдает ошибку ... и это правильно !!!
             # попытка сравнить текст с цифрой. (Нельзя, учти!)
#    print('успех')

# Traceback (most recent call last):
#   File "C:\Users\Компьютер\Documents\PYTHON_PROJECT_URBAN\02_Modul_IKL_pythonProject\04_ikl_M02DZ02.py", line 5, in <module>
#     if '6' > 5:
#        ^^^^^^^
# TypeError: '>' not supported between instances of 'str' and 'int'
# и это правильно

# if [5, 6] > 5: # выдает ошибку ... и это правильно !!!
                 # попытка сравнить список с цифрой. (Нельзя, учти!)
#    print('успех')

# Traceback (most recent call last):
#  File "C:\Users\Камиль\Documents\00_UNIVER_URBAN\02_Modul_IKL_ pythonProject\04_ikl_M02DZ02.py", line 15, in <module>
#    if [5, 6] > 5:
#       ^^^^^^^^^^
# TypeError: '>' not supported between instances of 'list' and 'int'

