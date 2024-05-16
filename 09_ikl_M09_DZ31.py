# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
class EvenNumbers:
    def __iter__(self):
        return self

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = start  # это счетчик

    def __next__(self):
        if self.count < self.end:
            self.count += 1
            if self.count % 2 == 0:
                return self.count
        else:
            raise StopIteration


en = EvenNumbers(10, 25)

for i in en:
    print(i)
