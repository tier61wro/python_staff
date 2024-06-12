from math import ceil

def find_nod(a: int, b: int) -> int:
    max_d = 1
    for d in range(1, ceil((max(a, b))/2)):
        if (a % d == 0) and (b % d == 0):
            max_d = d
    return max_d



def find_nod_euklide(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a, b = b, r
    return a

if __name__ == '__main__':
    # res = find_nod(20, 12)
    res = find_nod_euklide(20, 12)
    print(res)