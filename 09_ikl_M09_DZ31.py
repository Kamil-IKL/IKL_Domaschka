# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = start  # это для счетчика

    def __iter__(self):  # Без этого метода итератора объект неитерируемый (for работать не будет!!!)
        return self

    def __next__(self):
        if self.count < self.end:
            self.count += 1  # это счетчик
            if self.count % 2 == 0:  # сделал условие для четного числа
                return self.count  # возвращаю текущее число
            else:
                self.count += 1
                return self.count
        else:
            raise StopIteration


en = EvenNumbers(10, 25)
for i in en:
    print(i)
