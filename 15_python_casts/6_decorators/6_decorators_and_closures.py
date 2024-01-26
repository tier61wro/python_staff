'''
Замыкания сохраняют переменные из своего окружения.
Аналогично, при декорировании функции my_func декоратором my_dec,
новая функция создаётся для оборачивания и расширения поведения my_func с помощью замыкания,
'''

# замыкания
def print_author(name):
    def inner():
        # name переменная из окружения которую захватит замыкание
        print(id(name)) # 140027418796656
        print(f'code_author is {name}')
    return inner

print_alex = print_author('alex')
print_alex()
closure_id = id(print_alex.__closure__[0].cell_contents)
print(closure_id)  # 140027418796656 итого closure_id совпадает с id(name)



# декораторы
def add_author(func):
    def inner():
        # func переменная из окружения которую захватит замыкание
        func()
        print("Code author is Alex")

    return inner

def print_hello():
    print("Hello dear user")

'''
создаем декоратор
add_author(print_hello)
тоже самое что и 
@add_author
print_hello
'''
d = add_author(print_hello)

original_id = id(print_hello)
closure_id = id(d.__closure__[0].cell_contents)
print(f'{original_id} -- {closure_id}')  # 139718076003088 -- 139718076003088