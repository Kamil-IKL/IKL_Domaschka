# что нельзя сравнивать разные типы
if '6' != 5:
    print('успех')

#if '6' > 5:
#    print('успех')
# выдает ошибку:
# Traceback (most recent call last):
#   File "C:\Users\Компьютер\Documents\PYTHON_PROJECT_URBAN\02_Modul_IKL_pythonProject\04_ikl_M02DZ02.py", line 5, in <module>
#     if '6' > 5:
#        ^^^^^^^
# TypeError: '>' not supported between instances of 'str' and 'int'
# и это правильно

# if [5, 6] > 5:
    print('успех')
# Traceback (most recent call last):
#  File "C:\Users\Камиль\Documents\00_UNIVER_URBAN\02_Modul_IKL_ pythonProject\04_ikl_M02DZ02.py", line 15, in <module>
#    if [5, 6] > 5:
#       ^^^^^^^^^^
# TypeError: '>' not supported between instances of 'list' and 'int'

