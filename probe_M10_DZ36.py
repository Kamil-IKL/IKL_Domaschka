
import threading


class BankAccount():
    def __init__(self):
        self.account = 0
        self.amount = 0

def account_number(self):  # создал генератор номера счета
    import random
    account = ''
    for i in range(5):
        account = account + random.choice(list('0123456789'))
    return account

def deposit_task(account_number, amount):
    for _ in range(5):
        account.deposit(amount)

deposit_task(100,20)
print(a)





#
#
#     def deposit_task(account, amount):
#         for _ in range(5):
#             account.deposit(amount)
#
#     def withdraw_task(account, amount):
#         for _ in range(5):
#             account.withdraw(amount)
#             account = BankAccount()

# deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
# withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))
#
# deposit_thread.start()
# withdraw_thread.start()
#
# deposit_thread.join()
# withdraw_thread.join()

