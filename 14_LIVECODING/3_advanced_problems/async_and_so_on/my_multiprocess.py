import time
import multiprocessing as mp

# Функция, которую будет выполнять новый процесс
def process():
    print("Процесс запущен")
    time.sleep(10)
    print("Процесс завершен")

# Функция для проверки состояния процесса
def check_process(p):
    while p.is_alive():
        print("Процесс все еще выполняется...")
        time.sleep(2)
    print("Процесс завершен")

# Функция для создания и запуска нового процесса
def new_process():
    # Создаем новый процесс, который выполняет функцию process
    p = mp.Process(target=process)
    # Запускаем новый процесс
    p.start()
    # Проверяем состояние процесса
    check_process(p)

if __name__ == '__main__':
    # Запускаем функцию, которая создает и проверяет новый процесс
    new_process()
