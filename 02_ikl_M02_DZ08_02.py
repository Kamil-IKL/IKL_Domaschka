print('\n********* примеры *********\n')

print("Введите числа a и b, где а > b")
a = int(input('а = ',))
b = int(input('b = ',))
if a > b:
    print('a > b')
if a > b and a > 0:
    print('Успех')
if (a > b) and (a > 0 or b < 1000):
    print('Успех')
if 5 < b and b < 10:
    print('Успех')

