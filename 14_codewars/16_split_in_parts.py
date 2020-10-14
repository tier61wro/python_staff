'''
14.10.20
Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
----
самоканкатенация и инкремент
res += l
i += 1
'''

def split_in_parts(s, part_length):
	i = 1
	res = ''
	for l in s:
		res += l
		if i % part_length == 0:
			res += ' '
		i += 1
	return res.rstrip()


#out = split_in_parts("supercalifragilisticexpialidocious", 3)
out = split_in_parts("HelloKata", 1)
print(f'---{out}---')
