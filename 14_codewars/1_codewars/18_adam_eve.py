'''
According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
The first object in the array should be an instance of the class Man.
The second should be an instance of the class Woman.
Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
-----------------
сделайте класс Человек, потом класс Woman(Женщина) и Man(Мужчина) так чтобы они были подклассами класса Человек (наследовали его)
в итоге ваша функция God должна возвращать массив где первый элемент должен быть экземпляром класса Man а второй Woman
'''

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

paradise = God()

print(type(paradise))

if isinstance(paradise[0], Man):
    print("you are man!")