'''
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
----
enaumerate может принимать в качестве вротого аргумента число с которого надо начинать отсчет
можно итерироваться как по листу хэшей
# for v in enumerate(lines, 1):
# 	print (v)
(1, 'a')
(2, 'b')
так и по ключам - значениям - как во втором примере

'''
def number_long(lines):
	i = 0
	list_out = []
	for line in lines:
		list_out.append(str(i+1) + ': ' + line)
		i = i + 1
	return list_out

def number(lines):
	return [f'{n}: l' for n, l in enumerate(lines, 1)]

print(number(["a", "b", "c"]))
