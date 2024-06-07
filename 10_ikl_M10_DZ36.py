# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при
# модификации общего ресурса.

import threading
import time

lock = threading.Lock()  # создал замок


# создал генератор номера счета
def account_number():
    import random
    account = ''
    for i in range(5):
        account += random.choice(list('0123456789'))
    return account


account = account_number()  # создаю номер счета Клиента
balance = int(input('Внесите первый взнос на счет: '))  # создал баланс счета Клиента через запрос
print(f'{"":*^50}')
print(f'Баланс Вашего счета №"{account} составляет {balance}')
print(f'{"":*^50}')


class BankAccount(threading.Thread):  # создал класс движения ДС на счете Клиента
    def __init__(self, amount_incoming, amount_spending):
        super().__init__()  # метод вызова всех функций из класса родителя "Thread"
        self.amount_incoming = amount_incoming  # сумма пополнения счета
        self.amount_spending = amount_spending  # сумма списания счета
        global account, balance  # перенес сюда глобальные переменные (номер и баланс счета Клиента)
        self.balance = balance  # вот "загвозка" была пока не привязал значение переменной внутри класса к глобал

    def incoming_money(self):  # пополнение счета Клиента
        # balance = self.balance # остаток на счете Клиента
        with lock:  # включил локальный замок с автозакрытием
            for i in range(5):  # логика пополнения счета Клиента (5 итераций)
                time.sleep(1)
                global balance  # обязательно, иначе будет меняться значение только внутри класса
                balance += self.amount_incoming  # наконец-то вышел на переменную глобал
                print(f'Сумма пополнения = {self.amount_incoming},  баланс Вашего счета №{account} = {self.balance}')
                self.balance = balance  # обязательно переопределяю значение в глобал переменной
            return self.balance

    def spending_money(self):  # списание со счета Клиента
        # b = balance # остаток на счете Клиента
        with lock:  # включил локальный замок с автозакрытием
            for j in range(5):  # логика списания со счета Клиента (5 итераций)
                time.sleep(1)
                global balance
                balance += -self.amount_spending
                print(f'Сумма списания = {-self.amount_spending}, баланс Вашего счета №{account} = {self.balance}')
                self.balance = balance
            return self.balance

    def run(self):  # переопределил метод run
        a = self.amount_incoming * 5  # т.к. 5 итераций в цикле функции incoming_money(self)
        b = self.amount_spending * 5  # т.к. 5 итераций в цикле функции spending_money(self)
        if a > 0 and b == 0:  # это проверка при создании объекта для пополнения счета Клиента
            BankAccount.incoming_money(self)
            print(f'ПРОВЕРКА: после ВСЕХ пополнений = {a} баланс Вашего счета №{account} = {balance}\n')
        elif b > 0 and a == 0:  # это проверка при создании объекта для списания со счета Клиента
            BankAccount.spending_money(self)
            print(f'ПРОВЕРКА: после Всех списаний = {-b}, баланс Вашего счета №{account} = {balance}')
        elif a == 0 and b == 0:
            print(f'Баланс Вашего счета №{account} остался без изменений'.upper())
        else:
            print('Один из аргументов класса'.upper() + ' BankAccount() ' + 'должен быть равен 0'.upper())


incoming = BankAccount(10, 0)  # создаю поток пополнение счета Клиента
spending = BankAccount(0, 5)  # создаю поток списания со счета Клиента
incoming.start()  # запуск потока пополнения счета Клиента
spending.start()  # запуск потока счписания со счета Клиента
incoming.join()  # честно говоря, так и не понял, для чего этот метод нужен ?
spending.join()  # честно говоря, так и не понял, для чего этот метод нужен ?
# time.sleep(11)
print(f'\n{"":*^70}')
print(f'ПРОВЕРКА: после ВСЕХ операций баланс Вашего счета №{account} = {balance}')
print(f'{"":*^70}')
