
class BankAccount():
    def __init__(self):
        self.account = ''
        self.deposit = 0

    def account_number(self):  # создал генератор номера счета
        import random
        # self.account = ''
        for i in range(5):
            self.account = self.account + random.choice(list('0123456789'))
        return self.account


    def incoming_money(self, amount): # создал метод пополнения счета клиента
        self.account = BankAccount.account_number() # счет клиента
        self.amount = amount # сумма поступления на счет клиента
        for i in range(5):
            self.deposit += amount
        return self.deposit


a = BankAccount()
print(a)
print(a.account_number(), a.incoming_money(100))