# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.

import time
import threading


def my_funct_num():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


def my_funct_alphabet():
    for i in range(97, 107):  # начиная с 97 - это алфавит, если использовать "chr"
        print(chr(i))
        time.sleep(1)
    # alphabet = [print(chr(i)) for i in range(97, 107)] # тоже самое - это запись в строку, но не знаю
    # как сделать интервал по времени (куда воткнуть "time.sleep()")


thr_num = threading.Thread(target=my_funct_num)  # создаю поток по числам (см. задание)
thr_alp = threading.Thread(target=my_funct_alphabet)  # создаю поток по буквам (см. задание)
thr_num.start()  # запускаю поток по числам (см. задание)
# print(threading.enumerate()) # проверяю сколько "живых" потоков на данный момент запущено
thr_alp.start()  # запускаю поток по буквам (см. задание)
print(threading.enumerate())  # проверяю сколько "живых" потоков на данный момент запущено (обращаю внимание - работает)
