class MyNameException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} - this is the value type "int", but it should be "str"'


class MyAgeException(Exception):
    def __init__(self, name, minage, maxage):
        self.name = name
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f'{self.name} is not correct years old, change between {self.minage} and {self.maxage}'


class Human:
    def __init__(self, name, age):
        self.name = name == str(name)
        minage, maxage = 0, 110
        if name == str(name):
            self.name = name
        else:
            raise MyNameException(name)

        if age >= minage and age <= maxage:
            self.age = age
        else:
            raise MyAgeException(name, minage, maxage)

    def __str__(self):
        return f'{self.name} is {self.age} years'


human_01 = Human("4561", 80)
print(human_01)

human_02 = Human("Kamil", 52)
print(human_02)
print("*" * 40)

try:
    human_01 = Human(4561, 80)
    print(human_01)
except MyNameException as z:
    print(f'Чувак! .. Имя не может быть числом...', z)

try:
    human_02 = Human("Kamil", -52)
    print(human_02)
except MyAgeException as z:
    print(f'Неправильно введен аргумент возраст...', z)
print("*" * 40)
