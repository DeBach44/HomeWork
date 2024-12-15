
from random import randint
import threading
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(1, 101):
            d = randint(50,500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += d
            print(f"Пополнение: {d}. Баланс: {self.balance}")
            sleep(0.001)


    def take(self):
        for i in range(1, 101):
            t = randint(50, 500)
            print(f"Запрос на {t}")
            if t <= self.balance:
                self.balance -= t
                print(f"Снятие: {t}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
