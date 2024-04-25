class Vehicle:  # родительский класс Vehicle (автомобиль)
    def __init__(self):
        self.vehicle_type = 'None'
        super().__init__()  # этот метод позволяет включить все иниты последующих(ниже) родительских классов

    pass


class Car:  # родительский класс Car (автомобиль)
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, horse_power):
        self.horse_power = horse_power

    pass


print(f'\n======== проверка создания родительских классов =========')
print(f'объект класса Vehicle')
Avto_1 = Vehicle()
print(Avto_1.__dict__)  # проверка содержимого класса Vehicle

print(f'\nобъект класса Car')
Avto_2 = Car()
Avto_2.horse_powers(100)
print(Avto_2.__dict__)  # проверка содержимого класса Car


# создаю наследуемый класс из двух родительских классов Vehicle и Car
class Nissan(Vehicle, Car):
    def __init__(self):
        self.vehicle_type = 'Автобус'  # переопределил свойство vehicle_type из род.класса Vehicle
        super(Car).__init__()
        self.price = 2000000  # переопределил свойство price из род.класса Car

    def horse_powers(self, horsepower):  # переопределяю функцию родительского класса Car
        self.horsepower = horsepower = int(horsepower) * 0.735499  # перевожу мощность двигателя в Квт
        print(f'Мощность Вашего двигателя в КВт = {horsepower}')

    pass


print(f'\n=============== проверка наследование классов ============')
print(Nissan.__mro__)  # проверяю цепочку наследования классов

print(f'\n================== объект класса NISSAN ====================')
Avto_3 = Nissan()
print(f'Тип автомобиля - {Avto_3.vehicle_type}')
print(f'Стоимость автомобиля - {Avto_3.price}')
Avto_3.horse_powers(100)
print(Avto_3.__dict__)

print(f'\n==============Контрольная проверка родительских классов=============')

print(f'объект класса Vehicle')
Avto_1 = Vehicle()
print(Avto_1.__dict__)

print(f'\nобъект класса Car')
Avto_2 = Car()
Avto_2.horse_powers(100)
print(Avto_2.__dict__)
