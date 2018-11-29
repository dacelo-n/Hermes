import numpy as np
from itertools import permutations, product, chain
import math


def casing_count(word):
    """
    :param word: any word to be counted
    Determines if input is a word or number
    then takes length of the word and times it by the power of 2
    :return: the count
    """
    if word.isdigit():      # if a digit, only has one possibility
        r = 1
    else:                   # else its 2 to the power of the length
        r = pow(2, len(word))
    return r


def all_casings(input_string):
    """
    :param input_string: 
    Takes a string, passes it through generator.
    """
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
    """
    :param string_list: 
    amount is equal to the casing count for each word in the list
    :return: the product of amount and the factorial of the length of the list
    """
    amount = list(casing_count(item) for item in string_list)
    return np.product(amount) * math.factorial(len(string_list))


# phrases saved as a list, with white spaces eliminated
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
        temp.add(chain(permutation))
        print(list(chain(permutation)))

print(len(temp))

final =[list(gen) for gen in temp]

with open('file.txt', 'w') as file:
    for x in final:
        file.write("".join(x) + ",")
