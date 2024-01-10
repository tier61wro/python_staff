
def caps(func):
    def wrapper(*args, **kwargs):
        print("Caps lock starts now")
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# @caps
def say_hello(name, age = None):
    return f"Hello dear user, {name}, you are {age} years old"

res = caps(say_hello)('Sasha', age = 17)

print(res)

