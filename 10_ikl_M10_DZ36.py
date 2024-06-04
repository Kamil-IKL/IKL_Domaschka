# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при
# модификации общего ресурса.

import threading

class BankAccount(threading.Thread):
    def __init__(self):
        super().__init__()  # метод вызова всех функций из класса родителя "Thread"
        account_balance = int(input('Внесите первый взнос на счет: ')) # баланс счета клиента

    def Bank_accoint(self,incoming_money, spending_money): # создаю банковский счет клиента
        self.incoming_money = incoming_money # приход ДС на счет клиента
        self.spending_money = spending_money # расход ДС со счета клиента

    def incoming_money(self,amount_incoming): # пополнение счета клиента
        self.amount_incoming = amount_incoming # сумма пополнения

        pass

    def spending_money(self): # списание со счета клиента
        pass


