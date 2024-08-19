# изменяемые значения по умолчанию

def f(val, a=[]):
    a.append(val)
    return a

print(f(18))
print(f(19, []))
print(f(33))
