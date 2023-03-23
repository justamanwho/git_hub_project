# Hello GitHub!
# In this code I'll just print some programs to see how it's gonna look like in GitHub

import random as r
import os

# Some experiments with list
new_list = input('Enter some words: ').split()
print('. '.join(new_list).title())
print('Random word from list of your written words: ', r.choice(new_list))
print('Your sorted list: ', sorted(new_list))
print('Your list converted to dictionary with numeric keys: ', {i: new_list[i] for i in range(len(new_list))})

string = 'Hello my friend, my name is Dima.'
new_string = string.replace('Dima', 'Yoshikage Kira')
print(new_string)


# I love this recursive function.
def find_factorial(num):
    if num == 0:
        return 1
    else:
        return num * find_factorial(num-1)


print(find_factorial(5))


# Creating russian roulette
# Trying to delete System32 from python obviously gives PermissionError
# If error appears, message outputs

try:
    if r.randint(0, 6) == 0:
        os.remove('C:/Windows/System32')
    else:
        print('You are lucky!')
except PermissionError:
    print('OS successfully removed. Do you want to restart your computer now or later?')