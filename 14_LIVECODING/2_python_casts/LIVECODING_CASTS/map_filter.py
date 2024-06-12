# map
# letters = ['m', 'a', 'm', 'a']
letters = 'mama'


def upper(string: str) -> str:
    return string.upper()

l_upper = ''.join(list(map(upper, letters)))
#l_upper = ''.join(list(map(lambda x: x.upper(), letters)))

print(l_upper)

# filter

number_list = [1, 12, 20, 21]

# number_list_odd = list(filter(lambda x: x % 2 == 1, number_list))
number_list_odd = [n for n in number_list if n % 2 == 1]

print(number_list_odd)