import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while file.readline():
            all_data.append(line)
            line = file.readline()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
time_start = time.time()
for name in filenames:
    read_info(name)
time_end = time.time()
print('Линейное:',time_end - time_start)

# Многопроцессный
if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(read_info,filenames)
    end = time.time()
    print('Многопроцессорное', end - start)
