import time
import asyncio


async def get_temp(): # Температура
    print("Getting temp...")
    #time.sleep(2)
    await asyncio.sleep(2)
    print("Temp is 25 C")


async def get_pres(): # Давление
    print("Getting pressure...")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("Pressure is 101 kPa")


async def main():
    print("---------Start getting data---------")
    print(type(get_temp())) # <class 'coroutine'>
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_pres())
    await task1
    await task2
    print("---------End getting data---------")

print(f'---main {type(main())} ---')
start = time.time()                                # Время начала работы
asyncio.run(main())
finish = time.time()                               # Время конца работы

print(f"Working time = {round(finish-start ,2)} seconds")
