class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, horsepower):  # функция, возвращающая аргумент "horsepower"
        self.horsepower = int(horsepower)


# проверка работы класса Car
print('\n=============== родительский класс Car ===============')
Avto = Car()
print(Avto.price)
Avto.horse_powers(150)
print(Avto.__dict__) # проверяю, что внутри объекта


# создаю новый класс - наследника класса Car
class Nissan(Car):
    def __init__(self, price):  # переопределяю свойство родительского класса Car на свое
        self.price = price + 1000000

    def horse_powers(self, horsepower, color):  # переопределяю функцию родительского класса Car (добавил арг.Color)
        Car.horse_powers(self, horsepower)
        self.color = color


print('\n=============== новый класс Nissan ===============')
Avto_1 = Nissan(500000)  # создаю новый объект на базе класса Nissan (от родительского класса Car)
print(Avto_1.price)
Avto_1.horse_powers(200, 'Красный')
print(Avto_1.__dict__)  # проверяю, что внутри объекта


# создаю новый класс - наследника класса Car
class Kia(Car):  # создаю новый класс - наследника класса Car
    def __init__(self):  # переопределяю свойство родительского класса Car на свое
        self.price = price = int(input(f'Введите стоимость = '))  # создаю запрос стоимости

    def horse_powers(self, horsepower):  # переопределяю функцию родительского класса Car
        self.horsepower = horsepower = int(horsepower) * 0.735499  # перевожу мощность двигателя в Квт
        print(f'Мощность Вашего двигателя в КВт = {horsepower}')


print('\n=============== новый класс Kia ===============')
Avto_2 = Kia()  # создаю новый объект на базе класса Kia от родительского класса Car
print(Avto_2.price)
Avto_2.horse_powers(150)
print(Avto_2.__dict__)  # проверяю, что внутри объекта

# общая проверка исходника (родительского класса Car)
print('\n=============== ПРОВЕРКА: опять родительский класс Car ===============')
Avto_3 = Car()
print(Avto_3.price)
Avto_3.horse_powers(150)
print(Avto_3.__dict__)
