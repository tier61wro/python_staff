'''
28.3.22
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

Создайте класс Ball, у которого будет только один аргумент ball_type при инициализации
если аргументов нет, то по умолчанию должен быть regular
'''


class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


Ball1 = Ball()
Ball2 = Ball('super')



