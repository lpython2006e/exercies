#Write a function that checks whether an element occurs in a list.
def check_element(list_1, a):
    if a in list_1:
        print(a, "element occurs in a list")
    else:
        print(a,"element not occurs in a list")
list_2 = [1,2,3,4,4,2,4,2,2]
check_element(list_2, 7)
