#Write three functions that compute the sum of the numbers in a list:
# using a for-loop,
# a while-loop and recursion.
# (Subject to availability of these constructs in your language of choice.)

def sum_for_loop(lists):
    sum = 0
    for i in lists:
        sum += i
    return sum

def sum_while_loop(lists):
    sum = 0
    number = 0
    while(number<len(lists)):
        sum = sum + lists[number]
        number +=1
    return sum

def sum_recursion_list(lists, size):
    if(size==0):
        return 0
    else:
        return lists[size-1] + sum_recursion_list(lists, size-1)





lists = [1,3,5]
print("Sum use for =", sum_for_loop(lists))
print("Sum use while = ",sum_while_loop(lists))
print("Sum use recursion = ", sum_recursion_list(lists, len(lists)))

