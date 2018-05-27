#!/usr/bin/env pythoni3;
import random
from sys import argv

if (len(argv) > 1):
    num_lines = argv[1]
else: 
    num_lines = 5

print ("The poem will have " + str(num_lines) + " lines")

articles = ['the','a'];
nouns = ['cat','dog','woman','man']
verbs = ['sang','ran','jumped']
adverbs = ['loudly','quietly','well','badly']
for _ in range (1, (int(num_lines) + 1)):
    str_out = ''
    art = random.choice(articles)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    struct = random.randint(0, 1)
    if struct == 0:
        str_out = art + ' ' + noun + ' ' + adverb
    else:
        str_out = art + ' ' + noun +' '+ verb
    print (str_out)



