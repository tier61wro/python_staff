import time


def print1():
    print(1)


def print2():
    time.sleep(10)
    print(2)


def print3():
    print(3)

def main():
    print1()
    print2()
    print3()


main()