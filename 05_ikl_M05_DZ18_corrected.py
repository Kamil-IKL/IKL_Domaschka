class House:
    def __init__(self, NumberOfFloors):
        self.NumberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.NumberOfFloors = floors
        print(f'Теперь это дом из {self.NumberOfFloors} этажей')


a1 = House(1)  # создаю новый объект
print(a1.NumberOfFloors) # проверяю чему равет атрибут внутри класса
a1.setNewNumberOfFloors(5) # задаю этажность
print(a1.__dict__) # проверка изменений

a2 = House(2)  # создаю новый объект
print(a2.NumberOfFloors) # проверяю чему равет атрибут внутри класса
a2.setNewNumberOfFloors(15) # задаю этажность
print(a2.__dict__) # проверка изменений

a3 = House(3)  # создаю новый объект
print(a3.NumberOfFloors) # проверяю чему равет атрибут внутри класса
a3.setNewNumberOfFloors(15) # задаю этажность
print(a3.__dict__) # проверка изменений
