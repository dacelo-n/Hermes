# hermes
Hermes was a messenger of the gods, the patron saint of orators and poetry. Our Hermes sets to bring such words and power by producing all the possible variations of casings ( upper, lower case) and permutations of words and numbers entered, to generate a list of "passphrases/passwords" or any meaningful phrase that a user desires. 

import numpy as np
from itertools import permutations, product, chain
import math

def casing_count(word):
    if word.isdigit():      # if a digit, only has one possibility
        r = 1
    else:                   # else its 2 to the power of the length
        r = pow(2, len(word))
    return r
    
def all_casings(input_string):
    if not input_string:
        yield ""
    else:
        first = input_string[:1]
        if first.lower() == first.upper():
            for sub_casing in all_casings(input_string[1:]):
                yield first + sub_casing
        else:
            for sub_casing in all_casings(input_string[1:]):
                yield first.lower() + sub_casing
                yield first.upper() + sub_casing
def perm_count(string_list):
    amount = list(casing_count(item) for item in string_list)
    return np.product(amount) * math.factorial(len(string_list))
    
phrases = (list(input("Enter phrases separated by commas:\n").split(',')))
phrases = [x.strip() for x in phrases]

word_amt = [casing_count(word) for word in phrases]

dictionary = dict(zip(phrases, word_amt))
print(str(dictionary) + ' =  ' + str(perm_count(phrases)) + ' permutations')

alt = set()
for x in phrases:
    alt.add(all_casings(x))
temp = set()
for element in product(*alt):
    for permutation in permutations(element):
        temp.add(chain(permutation)) # my own
        print(list(chain(permutation)))

print(len(temp))
