def add_author(func):
    def wrapper():
        func()
        print("Code author is Alex")
    return wrapper


def print_hello():
    print("Hello dear user")

original_id = id(print_hello)
# 139788319089136 139788319089136

c = add_author(print_hello)
closure_id = id(c.__closure__[0].cell_contents)
print(original_id, closure_id)




def caps(func):
    def wrapper(*args, **kwargs):
        print("Caps lock starts now")
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@add_author
# @caps
def say_hello(name, age = None):
    return f"Hello dear user, {name}, you are {age} years old"

# res = caps(say_hello)('Sasha', age = 17)
#
# print(res)

