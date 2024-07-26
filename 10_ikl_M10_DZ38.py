# Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов на
# обновление информации в многопользовательской среде.
#
# Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление информации
# о поступлении товаров и отгрузке товаров. Наша задача заключается в разработке программы, которая будет эффективно
# обрабатывать эти запросы в многопользовательской среде, с использованием механизма мультипроцессорности для
# обеспечения быстрой реакции на поступающие данные.
#
# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
# Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
#
# Есть 2 действия: receipt - получение, shipment - отгрузка.
# а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа,
# если позиция уже была в словаре)
# б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
#
# 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс,
# запускает его(start) и замораживает(join).

import multiprocessing


class WarehouseManager:  # менеджер склада
    def __init__(self):
        self.data = multiprocessing.Manager().dict()  # словарь, организован через мультипроцессор

    def process_request(self, request: tuple):
        product, action, quantity = request  # action - действие, product - товар, quantity - количество

        if action == 'receipt':  # receipt - получение
            # Обработка поступления товара
            if product in self.data:
                self.data[product] += quantity  # увеличиваем количество
            else:
                self.data[product] = quantity  # добавляем новый товар

        elif action == 'shipment':  # shipment - отгрузка
            # Обработка отгрузки товара
            if product in self.data and self.data[product] > 0:
                if self.data[product] >= quantity:
                    self.data[product] -= quantity  # уменьшаем количество
                else:
                    print(f'Недостаточное количество товара {product} на складе (в наличие {self.data[product]}) !!!')
            else:
                print(f'Товара {product} на складе нет !')
        else:
            print(f'Некорректное действие')

        return self.data

    def run(self, requests):  # метод принимает список запросов
        processes = []  # создаю список процессов
        for request in requests:  # создаю цикл процессов по запросам
            p = multiprocessing.Process(target=self.process_request, args=(request,))  # создал процесс
            processes.append(p)  # добавил процесс по списку запросов
            p.start()  # запустил процесс по списку запросов

        for p in processes:
            p.join()


if __name__ == '__main__':
    # Создаем менеджер склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [("product1", "receipt", 1000),
                ("product2", "receipt", 1500),
                ("product1", "shipment", 800),
                ("product3", "receipt", 200),
                ("product2", "shipment", 500),
                ("product1", "shipment", 500),
                ("product2", "receipt", 1000)]

    manager.run(requests)
    print(dict(manager.data))






