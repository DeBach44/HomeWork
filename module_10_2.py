# DeBach
# module_10_1 "Потоковая запись в файлы"
import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.days = 0
        


    def fight(self, enemy = 100,days = 0):
        while self.enemy > 0:
            self.enemy -= self.power
            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemy} воинов.")
            time.sleep(1)


    def run(self):
        print(f"{self.name}, на нас напали!")
        self.fight()
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    list_ = [first_knight, second_knight]

    for i in list_:
        i.start()
    for i in list_:
        i.join()

    print('Все битвы закончились!')