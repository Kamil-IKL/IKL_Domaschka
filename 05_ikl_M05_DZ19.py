class Buiding:
    def __init__(self, numberOdFloors, buidingType):
        self.numberOfFloors = int(numberOdFloors)  # неважно как ввели, всегда переводит в число
        self.buildingType = str(buidingType)  # неважно как ввели, всегда переводит в строку

    def __eq__(self, other):  # перезагружаем оператор равенства
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            print(f'Объекты одинаковые')
        else:
            print(f'Внимание! Объекты разные')


a1 = Buiding(10, 5)  # вводим все числами
b1 = Buiding('10', '5')  # вводим все строками
a1 == b1
b1 = Buiding(5, 10)
a1 == b1
