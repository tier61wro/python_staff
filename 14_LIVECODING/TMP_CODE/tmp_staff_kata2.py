# num = 123
# digits = [int(d) for d in str(num)]
#
# print(digits)

# l = [1, 3, 3]

# for i, k in enumerate(l, 1):
#     print(f"{i} --- {k}")

# l = ['alex','rik','morty']
#
# d = {word: len(word) for word in l}
#
# print(d)

# l = [3, 4, 5]
# l_max = max(l)
# l_min = min(l)
#
# print(l_max, l_min)

# seq = [1, 2, 3]
#
# seq_rew = []
# for i in range(0, len(seq)):
#     seq_rew.append(seq.pop())
#
# print(seq_rew)


# a = 2
# b = 3
# a, b = b, a
#
# print(f"{a=}, {b=}")

# l = [3, 4, 4]
# print(l.count(4))

# # import re
# text = " A     wise old owl lived in an oak "
# # print(re.split('', text))
# #
# print(text.split())
# print(text.split(' '))

# l = ['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
#
# l_str = ' '.join(l)
# print(l_str)

# word = 'Sasha'
# word = None
#
# l = len(word) if word else 0
#
# print(l)
# arr = ['Sasha', "Vasya", None]
# # kata тернар внутри генератора
# len_arr = [(len(word) if word else 0) for word in arr]
# print(len_arr)


# improve kata set
l = [20,37,20,21]
dict_l = {num: l.count(num) for num in set(l)}
print(dict_l)


# l = [20,37,20,21]
# dict_l = dict([(num, l.count(num)) for num in set(l)])
#
# print(dict_l)
#
# b = 3
# potenga = lambda x: x*x
# a = potenga(b)
# print(a)

# digits = [1, 2, 3, 7, 8, 9, 3]
# del (digits[3])
# digits.insert(5, 7)
# print(digits)

# num_str = '12789'
# if '789' in num_str:
#     print('found')

# arr = [7, 8, 9]
# num_str = ''.join(map(str, arr))
# print(f'{num_str=}')

# import re
# num_str = '1237892789'
# if m := re.search("789", num_str):
#     print(m)
# start, end = m.span()
# print(f'{start=} {end=}')
#
#
# import re
# str_in ='17892789'
# str_out = re.sub('789', '897', str_in)
# print(f'{str_out=}')



ex = 10
del ex
ex2 = 20
del(ex2)
