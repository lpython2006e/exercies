# Write function that reverses a list, preferably in place.

def reverselist(a):
    a.reverse()
    return a

mylist = [1,5,3,7,8]
print(reverselist(mylist))