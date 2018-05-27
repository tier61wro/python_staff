#!/usr/bin/env pythoni3;
import random

articles = ['the','a'];
nouns = ['cat','dog','woman','man']
verbs = ['sang','ran','jumped']
adverbs = ['loudly','quietly','well','badly']
for _ in range (1,6):
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



