def add_func(*args, **kwargs):
    print(sum(args))
    h = kwargs;
    print(kwargs.keys())


l = [1, 2, 3]
dict2 = {'m' : 2, 'n' : 3}

add_func(*l, k=1, l=2)
add_func(*l, **dict2)