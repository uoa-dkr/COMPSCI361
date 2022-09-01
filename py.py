import math
import random
import oop
import oop as ts
from oop import toppings as tp, make_pizza as mp, a as A                # or * (to import all function(list/tuple/dic/varbs))
import string

print('\n\na\n n\t  r')
print(' a\tr')
print("this is an \"escape\" of a double-quote")

# input
input('\nwhat is your name?')
print(input("what's ur name?"))  # command + / (to comment)
print(len(input('x\n')))
print()


# import and randomness
print(random.randrange(1, 10))
print(random.choice([1,2,3]))
print(oop.a)
print(ts.a)
print(A)
oop.toppings('peperoni')
tp('peperoni')
mp('m', s = 'mushroom', m = 'cheese', l = 'pepper')


# f-string(3.7 or beyond) and format(3.6 or before)
a, b = 'hi', 1; print(a); print(b)
print(f'\nhello is {a} and 2-1={b}')
print('hello is {} and {}'.format('Hi',b))
print()


# list and its modification
lst = list(); lst = []
alphabet = string.ascii_lowercase

for letter in alphabet:
    lst.append(letter)                                       # append an element
lst.extend([1, 1, 1, True])                                  # extend an element
lst.pop(); lst.pop(2)                                        # pop an element
lst.remove('a')                                              # remove an element
del lst[0]                                                   # delete an element
lst.insert(0, 1)                                             # insert an element
print(lst.index('k'));print(lst.index(1,1,len(lst)-1))       # find the index of given element
lst.reverse();print(lst);lst[::-1];print(lst[::5])           # reverse the list/pick every 5th element
print(f'\n\t\t\t{lst.count(1)}')                             # count num of given element
lst = f'\n{[str(element) for element in lst]}';print(lst)    # list comprehension
print()

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
lst = student_scores[:]                                      # to create a new list by[:]
for i in range(len(lst)-1):
    if lst[0] <= lst[1]:
        del lst[0]
    else:
        lst.pop(1)
print(lst[0]); print(student_scores)                         # exclude[:] cause unexpected result


# tuple
tp = ()                                         # empty tuple
tp = (1,)                                       # single tuple must with a comma afterwards
tp = 1,'a'                                      # tuple with mixed datatype
print(tuple('abc'))                             # ('a','b','c')
print(tp[0])
x,y = tp; x,y = y,x                             # assignment and swap value
print(x);print(y)
tp = (1,2,3),(4,5,6)                            # nested tuple
print(tp)
tp = 1,2,3,4,5,6
x,y,*rest = tp;print(y,rest);print()



# dictionary
dic = {}                                        # create an empty dictionary
dic['color'] = 'red'                            # add an element to the dic
print(dic['color'])                             # retrieve an element
dic['color'] = 'blue';print(dic['color'])       # modify the value of the dic
print(dic.get('colours','incorrect spelling'))  # access an element if it exists otherwise return error message
print()

user = {'user_name':'Kdu407', 'first_name':'kerui'.title(), 'last_name':'du'.title()}
for keys, values in user.items():
    print(keys)
    print(f'values:{values}\n')

user.update({'user_name':'kdu407','full_name':'Dukerui'})   # merge two dics
print(user)
print()


# set(A set is an unordered collection of unique elements, display is ordered)
print(set({3,2,1,2,4,6,1,3}))
print({2,2,1,6,3})
print()

a = set(list(range(5)))
print(a)
b = set(range(2,6))
print(b)

print(a.difference(b))
print(a.union(b))                                   # or a | b
print(a.intersection(b))                            # or a & b
a.add(4);print(a)
a.remove(4);print(a)
a.update(b);print(a)
print()


# while loop(to avoid infinite loop, cmd + c)
while True:
    if input('\ninput nothing to break') == '':
        print('\nbye bye\n')
        break
    elif input('\ninput nothing to break') != '':
        continue
    else:
        pass



