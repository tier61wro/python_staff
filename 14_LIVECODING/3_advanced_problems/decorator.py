from datetime import datetime

def add_data(func):
    def wrapper(*args):
        print(datetime.now(), end=' ')
        func(*args)
    return wrapper


@add_data
def log_func(string_in: str):
     print(f"LOG FUNCTION: {string_in}")

log_func("server error 502")