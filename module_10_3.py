from random import randint
from time import sleep
import threading

lock = threading.Lock()


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = lock

    def deposit(self):
        for i in range(100):
            rand = randint(50, 500)
            self.balance += rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            sleep(0.001)
            if self.balance >= 500 and lock.locked():
                lock.release()

    def take(self):
        for i in range(100):
            rand1 = randint(50, 500)
            print(f'Запрос на {rand1}')
            if rand1 <= self.balance:
                self.balance -= rand1
                print(f'Снятие: {rand1}. Баланс: {self.balance}')
                sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
