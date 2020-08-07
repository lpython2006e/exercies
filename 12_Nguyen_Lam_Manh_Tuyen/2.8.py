#Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect squares.
# The perfect squares can be found by multiplying each natural number with itself. The first few perfect squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16.
# Twelve for example is not a perfect square because there is no natural number m so that m*m=12.
# (This question is tricky if your programming language makes it difficult to pass functions as arguments.)

import math


def on_all(lists):
    result = []
    for i in range(0, len(lists)):
        if len(result) != 20:
            num = math.sqrt(lists[i])
            if int(num) == num and num != 0.0:
                result.append(int(num))
    return result
list_1= [1,2,3,4,5,6,7,8,9,7,5,4,6,7,10101]
print(on_all(list_1))