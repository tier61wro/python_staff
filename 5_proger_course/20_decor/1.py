#!/usr/bin/env python3
#Создайте декоратор, который обернет функцию. Кроме того, добавьте в вашу простую функцию аргументы и сделайте так чтобы вы могли передавать их через декораторы.
def show_decorated_age(myfunk): # уменьшает возраст на три года
    def wrapper(age_y, age_m):
        age_y -= 3
        myfunk(age_y, age_m)
    return wrapper

@show_decorated_age
def show_age(age_y, age_m):
    print ("my age is {} years {} months".format(age_y, age_m))

show_age(32,6)
