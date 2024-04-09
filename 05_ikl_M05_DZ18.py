class House:
    def __init__(self, NumberOfFloors):
        self.NumberOfFloors = NumberOfFloors

    def setNewNumberOfFloors(self):
        floors = self.NumberOfFloors
        print(f'Вывожу на консоль NumberOfFloors = {floors}')


a1 = House(10)  # создаю новый объект с атрибутом 10
a2 = House(15)  # создаю новый объект с атрибутом 15
a3 = House(25)  # создаю новый объект с атрибутом 25
a1.setNewNumberOfFloors()  # вызываю метод(функцию) в объекте с атрибутом 10
a2.setNewNumberOfFloors()  # вызываю метод(функцию) в объекте с атрибутом 15
a3.setNewNumberOfFloors()  # вызываю метод(функцию) в объекте с атрибутом 25




