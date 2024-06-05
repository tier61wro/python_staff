def find_num(n: int, p: int) -> int:
    digits = [int(d) for d in str(n)]
    # digits = [*str(n)]
    print(digits)

    total_sum = 0

    for d in digits:
        total_sum = total_sum + int(d)**p
        p += 1

    print(f"{total_sum}")

    if total_sum%n == 0:
        return int(total_sum/n)
    else:
        return -1


res = find_num(695, 2)
res = find_num(691, 2)
print(f'{res=}')

# l = [1, 3, 3]
# for i, el in enumerate(l):
#     print(f'{i=} --- {el}')