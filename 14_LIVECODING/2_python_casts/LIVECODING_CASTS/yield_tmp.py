def simple_generator():
    value = 0
    while True:
        received = yield value * value  # Возвращаем квадрат текущего значения
        if received is not None:  # Если значение было отправлено в генератор
            value = received  # Обновляем текущее значение
        else:
            value += 1  # Иначе увеличиваем значение на 1

# Создаем генератор
gen = simple_generator()


# Итерируем по генератору
print(next(gen))  # 0*0 = 0
print(next(gen))  # 1*1 = 1
print(next(gen))
print(gen.send(10))  # Отправляем 10, следующее значение 10*10 = 100
print(next(gen))  # 11*11 = 121 (увеличено на 1 после отправленного значения)
print(next(gen))


