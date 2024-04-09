class House:
    numberOfFloors = 10

a = House()
a.numberOfFloors = 'многоэтажка'
print(f'Мой дом - это {a.numberOfFloors}')
a.numberOfFloors = 5
print(f'Текущий этаж равен {a.numberOfFloors}')
