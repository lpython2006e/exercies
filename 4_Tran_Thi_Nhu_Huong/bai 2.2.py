"""Write function that reverses a list, preferably in place."""


def reversved_list(a):
    a.reverse()
    return a    #if return a.reverse() => None ???

mylist = [1, 4, 5, 100, 2, 1, -1, -7]
new = reversved_list(mylist)
print("The reverse list is ", new)
