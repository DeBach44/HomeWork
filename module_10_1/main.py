# DeBach
# module_10_1 "Потоковая запись в файлы"

from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {str(i)}\n")
            sleep(0.1)
        print(f"Завершилась запись в файл: {file_name}")


start_time_1 = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
stop_time_1 = datetime.now()
end_time_1 = stop_time_1 - start_time_1
print(f"Работа потоков {end_time_1}")

start_time_2 = datetime.now()
thr_1 = Thread(target=write_words, args=(10, "example5.txt"))
thr_2 = Thread(target=write_words, args=(30, "example6.txt"))
thr_3 = Thread(target=write_words, args=(200, "example7.txt"))
thr_4 = Thread(target=write_words, args=(100, "example8.txt"))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

stop_time_2 = datetime.now()
end_time_2 = stop_time_2 - start_time_2
print(f"Работа потоков {end_time_2}")
