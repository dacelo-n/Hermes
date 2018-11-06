import numpy as np
from itertools import permutations, product, chain
import math


# amount of possible casing alterations
def casing_count(word):
    if word.isdigit():      # if a digit, only has one possibility
        r = 1
    else:                   # else its 2 to the power of the length
        r = pow(2, len(word))
    return r


# produces all casings to the word
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


# amount of permutations for the whole set:
# product of all casing for each word, times the factorial
# of the set length
def perm_count(string_list):
    amount = list(casing_count(item) for item in string_list)
    return np.product(amount) * math.factorial(len(string_list))


# phrases saved as a list, with white spaces elminated
phrases = (list(input("Enter phrases separated by commas:\n").split(',')))
phrases = [x.strip() for x in phrases]
# amount of casings for each word stored in list
word_amt = [casing_count(word) for word in phrases]
# dictionary of words & casings  printed with total permutations
dictionary = dict(zip(phrases, word_amt))
print(str(dictionary) + ' =  ' + str(perm_count(phrases)) + ' permutations')
# altered list of phrases: all casings
alt = set()
for x in phrases:
    alt.add(all_casings(x))
# permutations of altered list
temp = set()
for element in product(*alt):
    for permutation in permutations(element):
        temp.add(chain(permutation)) # my own
        print(list(chain(permutation)))

print(len(temp))

