# Задание:
# сумма продажи * скидка *
#     0 -  5000 *   5 %  *
#  5000 - 15000 *  12 %  *
# 15000 - 25000 *  20 %  *
# свыше - 25000 *  30 %  *

p = int(input('Введите сумму продажи: '))
if p > 0:
    if 0 < p < 5000:
        discount = int(p * 5 / 100)
        print('Скидка: ', discount)
    elif 5000 <= p < 15000:
        discount = int(p * 12 / 100)
        print('Скидка: ', discount)
    elif 15000 <= p <= 25000:
        discount = int(p * 20 / 100)
        print('Скидка: ', discount)
    elif p > 25000:
        discount = int(p * 30 / 100)
        print('Скидка: ', discount)
    print('Сумма со скидкой: ', p - discount)
else:
    print('\nНекорректная сумма')
