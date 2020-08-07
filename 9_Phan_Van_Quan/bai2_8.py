#Write a function on_all that applies a function to every element of a list.
# Use it to print the first twenty perfect squares.
# The perfect squares can be found by multiplying each natural number with itself.
# The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16.
# Twelve for example is not a perfect square because there is no natural number m so that m*m=12.
# (This question is tricky if your programming language makes it difficult to pass functions as arguments.)
from math import sqrt
def on_all(list_1):
    element = []
    for num in list_1:
        perfect = sqrt(num)
        if int(perfect) == perfect and perfect != 0:
            element.append(perfect)
    return element
list_2 = [1,144,4,2,9,81,100,144,121,36]
print(on_all(list_2))
