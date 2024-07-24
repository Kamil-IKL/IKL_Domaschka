import threading
import queue
import time


class Table:  # столы в кафе
    def __init__(self, number: int, is_busy: bool):  # анотация аргументов
        self.number = number  # значение - номер стола (int)
        self.is_busy = is_busy  # значение - стол занят(True) или свободен(False)


class Cafe:  # симулятор процессов в кафе
    def __init__(self, tables: list):  # анотация аргумента "tables"(столы) - тип данных список
        self.queue_cafe = queue.Queue()  # (место для хранения очередей) очередь Посетителей
        self.tables = tables  # список действующих столов в кафе
        self.customer_theard = []  # для создания списка Посетителей в очереди

    def customer_arrival(self):  # моделирует приход Посетителя (каждую секунду). Он же простой счетчик
        client_number = 1  # переменная Посетитель
        while client_number <= 20:  # Посетителей должно быть не более 20 (по условию задания)
            time.sleep(1)
            print(f'Посетитель № {client_number} прибыл')
            self.serve_customer(client_number)  # ПОКА ВОПРОС ????!!!!
            # self.customer_theard.append(client) # добавляем в список Посетителей нового Посетителя
            # client.start() # запустил Поток Посетителей
            client_number = client_number + 1

    def serve_customer(self, customer):  # моделирует обслуживание Посетителя
        free_table = False  # переменная "свободный стол" - занят
        for table in self.tables:  # создаем цикл "перебора столов" с условием на занятость(is_busy)
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель №{customer} занял столик №{table.number} (начало обслуживания)')
                customer_th = Customer(self, customer, self.queue_cafe, table)  # создаю поток Посетителей
                customer_th.start() # запустил поток Посетителей
                self.customer_theard.append(customer_th)  # добавляем в список Посетителей нового Посетителя
                free_table = True  # переменная "свободный стол" - занят
                return
        if not free_table: # если стол занят, то Посетитель ставится в очередь
            self.queue_cafe.put(customer)
            print(f'Посетитель №{customer} ждет столик')


class Customer(threading.Thread):  # поток Посетителей
    def __init__(self, cafe, client_number, queue_cafe, table):
        super().__init__()  # метод вызова всех функций из класса родителя "Thread"
        self.cafe = cafe
        self.client_number = client_number
        self.queue_cafe = queue_cafe
        self.table = table

    def run(self):
        time.sleep(5)  # по условию задания стол занимается только на 5 сек
        print(f'Посетитель №{self.client_number} поел и ушел (КОНЕЦ ОБСЛУЖИВАНИЯ)')
        self.table.is_busy = False  # стол свободен
        print(f'СТОЛИК №{self.table.number} освободился')
        if not self.queue_cafe.empty():  # проверяем очередь Посетителей (есть ли там кто-то, кто ждет?)
            next = self.queue_cafe.get()  # если там кто-то есть, то достаем его
            self.cafe.serve_customer(next)  # передаем Посетителя из очереди в функцию "serve_customer" для обслуживания


# Должно выводить на консоль:
# print(f'Посетитель № {"номер Посетителя"} прибыл')
# print(f'Посетитель № {"номер Посетителя"} сел за стол № {"номер Стола"} (начало обслуживания).')
# print(f'Посетитель № {"номер Посетителя"} покушал и ушел (конец обслуживания).')
# print(f'Посетитель № {"номер Посетителя"} ожидает свободный стол (помещение в очередь)')

# создание Столов в кафе
table1 = Table(1, False)
table2 = Table(2, False)
table3 = Table(3, False)
tables = [table1, table2, table3]  # список столов в кафе

# инициализируем Кафе
cafe = Cafe(tables)

# Запускаем поток прибытия Посетителей
th1 = threading.Thread(target=cafe.customer_arrival)
th1.start()
th1.join()
