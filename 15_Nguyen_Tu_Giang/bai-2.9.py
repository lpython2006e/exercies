# Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect squares. The perfect squares can be found by multiplying each natural number with itself. The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16. Twelve for example is not a perfect square because there is no natural number m so that m*m=12. (This question is tricky if your programming language makes it difficult to pass functions as arguments.)
import re


def mul(i):
    for x in range(int(i), int(i) + 20):
        print(x, '*', x, '=', x * x)
        x += 1


def on_all(list_ele, count=0):
    list_num = re.findall('[0-9]', str(list_ele))
    for i in list_num:
        print('Twenty perfect squares of', i, ':')
        mul(i)


print(on_all([1, 's', 0, 'e', 3, 6]))
