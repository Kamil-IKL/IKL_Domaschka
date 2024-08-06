import inspect
from pprint import pprint
# help(inspect)

def object_info(obj):
    # Получаю тип объекта
    obj_type = type(obj).__name__

    # Получаю атрибуты объекта (используя dir для получения всех атрибутов и убираю скрытые)
    obj_attrib = [attr for attr in dir(obj) if not attr.startswith('_')]

    # Получаем методы объекта (также фильтруем скрытые и оставляем только callable)
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('_')]

    # Получаем модуль, к которому принадлежит объект
    obj_module = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    return {
        'type': obj_type,
        'attributes': obj_attrib,
        'methods': obj_methods,
        'module': obj_module,
    }

class Human:
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    def my_info(self, ):
        # age = int(input(f'Сколько Вам лет {name} ?:  '))
        if self.age < 18:
            print(f'{self.name}, Вы еще молоды ! У вас все впереди, приходите через {18 - self.age} года(лет)')
        elif 18 <= self.age and self.age < 35:
            print(f'{self.name}, Вы влкючены в программу "Молодежь вперед !" ')
        else:
            print(f'{self.name}, уже поздно !!! Вам дальше по коридору и направо...!')


human_01 = Human(12,'Kamil')
human_01.my_info()
human_02 = Human(52,'Антошка')
human_02.my_info()

# интроспекция
introsp_obj = object_info(human_01)
print(introsp_obj)


# # интроспекция
# print(type(human_02)) # узнаем, какой тип объекта (переменная, класс, функция) ?
# pprint(dir(Human)) # узнаем, какие методы и атрибуты у объекта ?
# print(hasattr(human_01, 'name')) # проверяю наличие атрибута "name" в объекте
# print(getattr(human_01, 'name')) # узнаю значение атрибута "name" в объекте
# setattr(human_01, 'name', 'КАМИЛЬ') # изменил значение атрибута 'name' в объекте 'human_01' на новое
# print(human_01.name) # проверяю
# print(getattr(human_01, 'name')) # проверяю через получение атрибута из объекта
#
# print(callable(human_02.name)) # невызываемый тип данных
# print(callable(human_02.my_info)) # вызываемый метод
# human_02.my_info() # проверка






