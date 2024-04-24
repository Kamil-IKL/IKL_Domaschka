class Buiding:  # создал класс строительство
    total = 0  # создал атрибут класса

    def __init__(self):  # создал инициализатор для класса
        Buiding.total += 1
        # Building = Buiding.total + 1 # это ошибка (тотал не увеличивается)
        Building = Buiding.total


# Building_1 = Buiding()
# Building_2 = Buiding()
# Building_3 = Buiding()
# print(Building_1, type(Building_1), id(Building_1))
# print(Building_2, type(Building_2), id(Building_2))
# print(Building_3, type(Building_3), id(Building_3))


for i in range(40):
    Building = Buiding()
    print(Buiding.total, Building, type(Building), id(Building))


