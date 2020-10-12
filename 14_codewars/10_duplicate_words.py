'''
#11.05.2020
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
Example:
Input:
'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
Output:
'alpha beta gamma delta'
----
else в одну строчку
words_uniq.append(w) if words_dict[w] == 1 else {}
'''
import re
def remove_duplicate_words(s):
    words = re.split(' ', s)
    words_dict = {}
    words_uniq = []
    for w in words:
        words_dict[w] = words_dict.get(w, 0) + 1
        words_uniq.append(w) if words_dict[w] == 1 else {}
    return ' '.join(words_uniq)

str_in  = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
str_out = remove_duplicate_words(str_in)
print(str_out)