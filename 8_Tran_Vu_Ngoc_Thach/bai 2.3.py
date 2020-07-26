"""Write a function that checks whether an element occurs in a list."""


def check_existence_of_element(a,b):
    if a in b:
        print ("the item in list")
    else:
        print ("the item is not in the list")
item = 1
mylist = [1, 4, 5, 100, 2, 1, -1, -7]
check_existence_of_element(item,mylist)
