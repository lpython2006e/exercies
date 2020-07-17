# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
# (Subject to availability of these constructs in your language of choice.) for loop
import re


def total_for(list_ele, count=0):
    for i in list_ele:
        if str(i).isdigit():
            count += i
    return count


print('The result of for loop:', total_for([1, 's', 0, -5, 'e', 3, 6]))


# while loop


def total_while(list_ele, count=0, x=0):
    while x < len(list_ele):
        if str(list_ele[x]).isdigit():
            count += list_ele[x]
        x += 1
    return count


print('The result of while loop:', total_while([4, 's', 0, 'e', 9, 6, -5]))


# recursion
def total_recursion(list_ele):
    if len(list_ele) == 1:
        return list_ele[0]
    count = list_ele[0]
    list_ele.pop(0)
    count += total_recursion(list_ele)
    return count


print('The result of recursion:', total_recursion([1, -5, 0, 3, 6]))
