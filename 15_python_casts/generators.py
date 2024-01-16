g = (i**2 for i in range(10))

print(type(g))
# <class 'generator'>

# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

l = [i**2 for i in range (1, 10)]
print(type(l))


g2 = firstn(10)
print(type(g2))


for i in g2:
    print(i)