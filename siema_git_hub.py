# Hello Github!
# In this code I'll just print some programs to see how it's gonna look like in Github

import random as r

new_list = input('Enter some words: ').split()
print('. '.join(new_list).title())
print('Random word from list of your written words: ', r.choice(new_list))
print('Your sorted list: ', sorted(new_list))
print('Your list converted to dictionary with numeric keys: ', {i: new_list[i] for i in range(len(new_list))})