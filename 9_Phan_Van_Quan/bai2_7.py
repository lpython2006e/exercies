#Write three functions that compute the sum of the numbers in a list:
# using a for-loop, a while-loop and recursion.
# (Subject to availability of these constructs in your language of choice.)
def sum_for_loop(list_1):
    tong = 0
    for num in list_1:
        tong = tong + num
    print(tong)
def sum_while_loop(list_1):
    tong = 0
    index = 0
    while index < len(list_1):
        tong = tong + list_1[index]
        index += 1
    print(tong)
def sum_recursion(list_1,):
