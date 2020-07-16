#Write function that reverses a list, preferably in place.

#get list from user input until none input
def getinput():
    while True:
        element=input("Please input your element \n")
        if element!='':
            lst.append(element)
        else:
            print(lst)
            break
    return lst

#solution1
def reverselist(lst):
    lst.reverse()
    return (lst)
#solution2
def reverse_list(lst):
    length = len(lst)
    for i in range(0, length//2):
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]
    return lst

lst=[]
getinput()
result = reverse_list(lst)
print("List after reversed is {}".format(result))
