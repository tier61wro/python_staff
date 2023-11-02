
def uc_version(func):
    def wrapper():
        result = func()
        upper_case_text = result.upper()
        return upper_case_text
    return wrapper


@uc_version
def say_hello():
    return "Hello_dear_user"

print(say_hello())