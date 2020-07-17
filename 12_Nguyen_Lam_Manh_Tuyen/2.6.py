#Write a function that tests whether a string is a palindrome.

#get string from user input
input_string=input("Please input your string \n")

def reverselist(lst):
    lst.reverse()
    return (lst)

def check_palindrome(string):
    lst=list(string)
    print(lst)
    reverse_lst=reverselist(lst)
    print(reverse_lst)
    if lst==reverse_lst:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

check_palindrome(input_string)