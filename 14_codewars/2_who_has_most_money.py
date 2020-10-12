#3.05.2020
'''
You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:

Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
----
получается что случая когда у двух студентов одинаковое количество денег быть не может
всегда или один или все, так устроены тестовые наборы

    # словарь можно генерировать через генератор как и список
    sum_dict = {st.name: st.fives * 5 + st.tens * 10 + st.twenties * 20 for st in students}

    #для подсчета количества вхождений элемента в массив используем count
    l = [3,4,4]
    l.count(4)
    2

'''


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

students = [cam, geoff, phil]


def most_money(students):
    # словарь можно генерировать через генератор как и список
    sum_dict = {st.name: st.fives * 5 + st.tens * 10 + st.twenties * 20 for st in students}

    max_sum = max(sum_dict.values())
    #для подсчета количества вхождений элемента в массив используем count
    if (list(sum_dict.values()).count(max_sum) == len(students)) & (len(students) > 1):
        return 'all'
    else:
        for key, value in sum_dict.items():
            if value == max_sum:
                return key


print(most_money(students))