import codewars_test as test

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(obj_list):
    name_money_dict = {}
    for obj in obj_list:
        name_money_dict[obj.name] = obj.fives*5 + obj.tens*10 + obj.twenties*20


    if len(name_money_dict) == 1:
        print(name_money_dict.keys())
        return list(name_money_dict.keys())[0]
    elif len(set(name_money_dict.values())) == 1:
        return "all"
    else:
        max_el = (sorted(name_money_dict.values()).pop())
        for k in name_money_dict:
            if name_money_dict[k] == max_el:
                return k



phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)
# roma = Student("Roma", 2, 0, 0)


# res = most_money([cam, geoff, phil])
test.assert_equals(most_money([cam, geoff, phil]), "Phil")
test.assert_equals(most_money([cam, geoff]), "all")
test.assert_equals(most_money([geoff]), "Geoff")

# print(res)
