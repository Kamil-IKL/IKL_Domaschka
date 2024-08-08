class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

# obj = Runner("VALERA")
# for i in (range(10)):
#     # obj = Runner(f"VALERA_{i}")
#     # print(obj)
#     obj.walk()
#     print(obj.distance)
obj_1 = Runner("VALERA")
for i in range(10):
    obj_1.walk(), print(obj_1.distance)
    obj_1.run(), print(obj_1.distance)
# obj_2 = Runner('Leonid')
# for i in range(10):
#     obj_2.walk()
#     obj_2.run()
#     print(obj_2.distance)
