# Задание на САМПО


def uc_version(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        upper_case_text = result.upper()
        return upper_case_text
    return wrapper


@uc_version
def say_hello(name, age=None):
    print(name)
    print(f"age = {age}")
    return "Hello_dear_user, {name}, you are {a} years old"

print(say_hello('Vasya', age = 12))
