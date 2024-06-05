'''
13.10.20
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
----
самый простой способ получить список из строки в питоне:
list('aeiou')
'''
import re

def disemvowel(string):
	vowels = list('aeiou')
	vowels.extend(list('aeiou'.upper()))
	res = ''
	for l in list(string):
		if l not in vowels:
			res = res + l
	return res

# красивый способ через регулярки
def disemvowel_re(string):
	return re.sub(r"[aeiouAEIOU]", "", string)

result = disemvowel("This website is for losers LOL!")
print(result)

