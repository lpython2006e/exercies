"""Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]"""


def convert_to_list(a):
    mylist = []
    for i in range(0, len(a)):
        mylist.append(a[i])
    return mylist


def concanate_list(a, b):
    a.extend(b)
    return a


string_1 = input("please input first string")
string_2 = input("please input second string")
new_string = concanate_list(convert_to_list(string_1), convert_to_list((string_2)))
print(new_string)
