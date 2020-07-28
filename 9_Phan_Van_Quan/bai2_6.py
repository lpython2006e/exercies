#Write a function that tests whether a string is a palindrome

def check_palindrome(string_1):
    center = int(len(string_1)/2) -1
    dem = 0
    for num in range(center):
        if string_1[num] != string_1[len(string_1)-1-num]:
            dem += 1
    if dem == 0:
        print("string is a palindrone")
    else:
        print("string is not a palindtone")


string_2 = input("Nhap vao string ")
check_palindrome(string_2)