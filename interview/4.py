funcs = []
for i in range(5):
    funcs.append(lambda x: x * i)

for f in funcs:
    print(f(1))
