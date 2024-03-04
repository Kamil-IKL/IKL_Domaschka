car_list = ['BMW', 'UAZ', 'Ford', 'Lada', 'Citren']
cars_count = int() # int - переводит в целое число ... если (10,25),то --> 10; если (10,52), то --> 11 (учти!) 
for i in car_list:
    print(f'Я езжу на автомабиле марки: {i} cars_count = {cars_count}')
    cars_count += 10
