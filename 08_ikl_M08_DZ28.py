import warnings


def f1(a, b):
    res = a / b
    if 0 <= b < 0.5:
        warnings.warn(f'аргумент {b} - близится к нулю', category=UserWarning)
    print(f'Результат деления = {res}')


# warnings.simplefilter("error") # выводит предупреждение и останавливает выполнение кода
# warnings.simplefilter("ignore") # игнорирует (предупреждения не выводит), код работает
# warnings.simplefilter(("always")) # выводит предупреждение все и всегда, код выполняется
print('Вариант № 1 ... b = 0,3')
f1(10, 0.3)
print(f'{'=' * 40}\n')

print('Вариант № 2 ... b = 0,03')
f1(10, 0.03)
print(f'{'Продолжаем ':*<50}\n')

print('Вариант № 3 ... b = 0 c блоком try-except')
try:
    f1(10, 0)
except ZeroDivisionError as z:
    print(f'Делишь на  ноль ?! Мдаа... крутой !\nНо мы работу продолжаем...', z)
    print(f'{"+" * 50}\n')
