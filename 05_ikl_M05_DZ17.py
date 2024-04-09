class House:
    numberOfFloors = 10

House.numberOfFloors
print(f'Текущий этаж равен {House.numberOfFloors}')
House.numberOfFloors = 'многоэтажка'
print(f'Мой дом - это {House.numberOfFloors}')
House.numberOfFloors = 5
print(f'Текущий этаж равен {House.numberOfFloors}')
