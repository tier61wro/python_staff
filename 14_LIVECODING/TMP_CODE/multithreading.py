import threading
import time

def print_numbers(thread_id):
    for i in range(5):
        print(f"Thread {thread_id}: {i}")
        time.sleep(1)  # Симуляция задержки для демонстрации многопоточности

# Создаем два потока
thread1 = threading.Thread(target=print_numbers, args=(1,))
thread2 = threading.Thread(target=print_numbers, args=(2,))

# Запускаем потоки
thread1.start()
thread2.start()

# Ожидаем завершения потоков
thread1.join()
thread2.join()

print("Both threads have finished execution.")
