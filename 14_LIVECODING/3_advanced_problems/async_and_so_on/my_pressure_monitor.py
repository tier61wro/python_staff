import time
import asyncio

async def get_temp():
    print("Getting temp...")
    await asyncio.sleep(2)
    print("Temp is 25 C")

async def get_pres():
    print("Getting pressure...")
    await asyncio.sleep(4)
    print("Pressure is 101 kPa")

async def monitor_tasks():
    while True:
        tasks = asyncio.all_tasks()
        print(f"Current tasks: {len(tasks)}") # Current tasks: 4
        for task in tasks:
            print(task)  # <Task pending name='Task-3' coro=<get_pres()
        await asyncio.sleep(1)  # Check tasks every 1 second

async def main():
    print("---------Start getting data---------")
    print(type(get_temp()))  # <class 'coroutine'>
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_pres())
    monitor_task = asyncio.create_task(monitor_tasks())
    await task1
    await task2
    monitor_task.cancel()  # Cancel the monitoring task once done
    print("---------End getting data---------")

start = time.time()
asyncio.run(main())  # создание Event Loop
finish = time.time()
int()

print(f"Working time = {round(finish-start, 2)} seconds")
