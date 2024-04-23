class House:
    numberOfFloors = 10

for i in range(House.numberOfFloors+1):
    print(f'Текущий этаж {i}')



House.numberOfFloors
print(f'Текущий этаж равен {House.numberOfFloors}')
House.numberOfFloors = 'многоэтажка' # меняю атрибут внутри класса
print(f'Мой дом - это {House.numberOfFloors}')
House.numberOfFloors = 5 # меняю атрибут внутри класса
print(f'Текущий этаж равен {House.numberOfFloors}')


