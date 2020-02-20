from itertools import groupby
from operator import itemgetter

word_list = ['tbe','gave','so','yay','set','make','go','snow','take','kee','come','think',
     'hook','want','adg']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)