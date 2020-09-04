"""Write a function that tests whether a string is a palindrome.
A palindrome is a word, phrase, number or other sequence of units that has the property of reading the same in either direction"""

def reversved_list(x):
    x.reverse()
    return x

def palindrome(a):
    b = a.lower()
    first_list = []
    for i in range(0, len(b)):
        first_list.append(b[i])
    second_list = reversved_list(first_list)
    if first_list == second_list:
        print(" this is a palindrome")
    else:
        print("not a palindrome")


mylist = input("please input a string")
palindrome(mylist)
