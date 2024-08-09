# https://school.kontur.ru/publications/2567
import asyncio
import time

# это специальный вид функции в Python, который может приостанавливать свое выполнение, отдавая управление обратно вызывающему коду, и возобновлять работу позже.
# Корутины позволяют писать асинхронный код, который может выполнять другие задачи, пока ожидает завершения некоторых операций, таких как ввод-вывод.

async def notification():
    print("посмотри в окно 5 сек")
    for k in range(1, 6):
        # time.sleep(1)
        await asyncio.sleep(1)
        print(k)
    print("посмотрел")


async def main():
    # await notification()
    task = asyncio.create_task(notification())
    await task
    print("Разговариваем с коллегой")
    print("Едим")

asyncio.run(main())