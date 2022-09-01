import math
import random

a = math.e

print(random.randrange(1, 10, 1))   # 1-9  (int)
print(random.random())              # 0-1  (float)
print(random.randint(1,10))         # 1-10 (int)
print(random.normalvariate(0, 10))  # mean = 0, sd = 10 (rnorm(0,10))
print(random.uniform(0, 2))         # mean = 0, sd = 2 (runif(0, 2 ))
print()


def toppings(*topping):             # allow multiple parameter and forms a tuple
    print(topping)

toppings('salt', 'cheese')
print()


def make_pizza(size, **topping):
    print(f'the size of the pizza is {size.upper()}\n')
    print(f'add some toppings {topping.get(size, "dont have such a topping")}')

make_pizza('s', s = 'mushroom', m = 'cheese', l = 'pepper')
make_pizza('e', s = 'mushroom', m = 'cheese', l = 'pepper')



class dog:                                                     # basic class
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age
        self.dog_weight = 5

    def name(self):
        print(f'\nThe name of dog is {self.dog_name}')

    def age(self):
        print(f'The age of dog is {self.dog_age}')

    def gender(self, num):
        if num == 0:
            return 'male'.title()
        elif num == 1:
            return 'Female'
        return 'Undefined'

    def weight(self):
        print(f'The dog weights around {self.dog_weight} kg')

    def gain_weight(self, how_much):
        self.dog_weight += how_much


my_dog = dog('kat',8)                                      # my_dog is <__main__.dog object at 0x1030d6e80>
print(f'\n\n{my_dog.dog_name}');print(my_dog.dog_age)
my_dog.name();my_dog.age();my_dog.weight();print(f'This dog is {my_dog.gender(1)}\n')

my_dog.dog_weight = 10                                     # to modify parameter
my_dog.weight()
my_dog.gain_weight(5)                                      # alternative way to increment
my_dog.weight()


class zoo(dog):                                            # sub-class
    def __init__(self, name, age):
        super().__init__(name, age)                        # dog.__init__(self,name)

    def dogs(self):
        print(f'\nthere is a dog named {self.dog_name} '
              f'and aged {self.dog_age} and weighted {self.dog_weight} kg')

z = zoo('anivia',10)
z.dogs()
z.name()


# class animal(object):
#     __height_of_baby_dog = 0
#
#     def __init__(self, height):
#         self.__height = height                    # subclass but don't inherit(create by itself)
#
#     def height_increment(self, num):
#         num.__height += num
#         print(f'now the dog is {self.__height} cm')
#
#     def height_decrement(self, num):
#         num.__height += num
#         print(f'now the dog is {self.__height} cm')
#
#     def baby_height(self, num):
#         print(f'the baby dog has height {self.__height_of_baby_dog} cm')
#         self.__height_of_baby_dog += num
#         print(f'now changes to {self.__height_of_baby_dog} cm')
#
# a_dog = animal(20)
# a_dog.height_decrement(10)




####################################################################################################
# basic stuff(quick remainder)

x = 'ad ada da d d'
y = (x.split(' '))
z = 'dk'
print(y)
print('?'.join(y))
print(x,z,sep=',')
print(x,end='?')
print()
print()


####################################################################################################
# read/write/edit a file by open(,)

read_file = open('data/file1','r')              # default(r, w, a / r+, w+, a+)
print(read_file.read(12))                       # first 12 include the blanks
print()

read_file = open('data/file1')                  # return whole info
print(read_file.read())
print()

read_file = open('data/file1')                  # return some info b
print(read_file.readline())
print()

with open('data/file1') as read_file:           # each line with extra blank line return list
    content = read_file.readlines()
print(content)
print()


append_file = open('data/file1','a')            # to append(do not override)
append_file.write('\nThese are list of LoL champs list above')
append_file.close()


overwrite_file = open('data/file1','w+')
overwrite_file.write('anivia\nkat\nfizz zed\nyasuo darius j4 annie ezreal'
                     '\nvn mf ahri wukong\nsyndra lee xin cass cait amumu jax')
overwrite_file.close()


####################################################################################################
# try-except - else-finally (IndexError/KeyError/NameError/TypeError/FileNotFoundError)

try:                                             # test if there is an error
    print(d)
except NameError:
    print('\nd is not defined')
except:
    print('there is no such a variable')

try:
    print(f'\n{1*2}')
except:
    print('how come')
else:                                            # else statement executed when no error occur
    print('the result is 2')

try:
    print(5/0)
except ZeroDivisionError:
    print("\ncan't divide by 0")
else:
    print('maybe you can')
finally:                                         # finally statement executed regardless of error
    print('good luck\n\n')

# if not type(z) is int:                         # raise an error
#     raise TypeError("Sorry, must be integer")
#
# if z != 1:
#     raise Exception(f'z is {z}')
