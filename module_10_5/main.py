from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    with open(name,"r") as file:
        all_data = [line for line in file]


filenames = [f'./file {number}.txt' for number in range(1, 5)]
#Линейный запуск
# start_time = datetime.now()
# for i in filenames:
#     read_info(i)
# stop_time = datetime.now()
# end_time = stop_time - start_time
# print(end_time)


#Многопроцессный запуск
if __name__ == '__main__':
    start_time1 = datetime.now()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    stop_time1 = datetime.now()
    end_time1 = stop_time1 - start_time1
    print(end_time1)


