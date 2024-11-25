import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self, counter=100):
        days = 0
        print(f'{self.name}, на нас напали!')
        while counter:
            counter -= self.power
            time.sleep(1)
            days += 1
            if counter < 0:
                print(f'{self.name} сражается {days} день(дня).., осталось 0 воинов.')
            else:
                print(f"{self.name} сражается {days} день(дня).., осталось {counter} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
