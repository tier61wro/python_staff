def gen():
    for i in range(10):
        yield i


def reverse_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


g  = reverse_countdown(4)

for i in g:
    print(i)

#print (next(g))
#print (next(g))
#print (next(g))
#print (next(g))
