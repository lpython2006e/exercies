"""Write three functions that compute the sum of the numbers in a list:
using a for-loop, a while-loop and recursion. (Subject to availability of these constructs in your language of choice.)"""


def sum_for_loop(x):
    sum = 0
    for i in range(0, len(x)):
        sum += x[i]
    return sum


def sum_while_loop(x):
    sum = 0
    i = 0
    while i < len(x):
        sum += x[i]
        i += 1
    return sum


def _recursion_sum(a, thelist):
    x= int(a)
    if x == 0:
        return 0
    else:
        return thelist[x - 1] + _recursion_sum(x - 1, thelist)


mylist = [1, 2, 3, 4, 5]
a = sum_for_loop(mylist)
print("for loop", a)
b = sum_while_loop(mylist)
print("while loop", b)
c = _recursion_sum(5, mylist)
print ("recursion ",c)
