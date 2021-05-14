from helpers import get_countries
import string

""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """

def shortest_names(x):
    y = len(min(countries, key=len))
    short_list = []
    for i in x:
        if len(i) == y:
            short_list.append(i)
    print(short_list)
    return

def most_vowels(x):
    vowel_list = sorted(x, key=lambda word: sum(ch in 'aeiou' for ch in word), reverse=True)
    top_list = vowel_list[0:3]
    print(top_list)
    return

#def alphabet_set(x):
#    sorted_list = sorted(x, reverse=True)
#    alphabet = list(string.ascii_lowercase)
#    checklist = []
#    counter = 0
#    for i in sorted_list:
#        counter = (counter + 1)
#        y = list(i)
#        print(y)
#        print(counter)
#        for i in y:
#            if i not in checklist:
#                if i in alphabet:
#                    checklist.append(i)
#        checklist.sort()
#        print(checklist)
#        if(checklist == alphabet):
#            print('done')
#            break
#    return

def alphabet_set(input_list):
    sorted_list = sorted([x.lower() for x in input_list], reverse=False)
    alphabet = sorted((list(string.ascii_lowercase)), reverse=True)
    filter_list = []
    checklist = []
    counter = 0
    for i in alphabet:
        matching = sorted([naam for naam in sorted_list if i in naam], key = lambda sub : len(list(set(sub))), reverse=True)
        filter_list.append(matching[0])
    print(filter_list)
    for i in filter_list:
        counter = (counter + 1)
        y = list(i)
        print(counter)
        print(y)
        for i in y:
            if i not in checklist:
                if i in alphabet:
                    checklist.append(i)
        checklist.sort()
        print(checklist)
        if((sorted(checklist, reverse=True)) == alphabet):
            print('done')
            break
    return

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    
    
    