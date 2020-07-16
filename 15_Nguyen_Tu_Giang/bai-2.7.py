# Write a function that tests whether a string is a palindrome.
def check_palindrome(value):
    for i in range(int(len(value)/2)):
        # print(value[i], value[len(value) - 1 - int(i)])
        if value[i] != value[len(value) - 1 - int(i)]:
            return False
        else:
            return True


print(check_palindrome('1212'))
