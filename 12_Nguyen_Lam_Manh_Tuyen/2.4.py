#Write a function that returns the elements on odd positions in a list.

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

#solution1: replace list with odđ list
def oddlist(lst):
    lst=lst[1::2]
    return (lst)
#solution2
def odd_list(lst):
    temp_lst=[]
    for i in range(0,len(lst)):
        if i%2!=0:
            temp_lst.append(lst[i])
    return temp_lst
lst=[]
getinput()
result = odd_list(lst)
print("Element on odd position is {}".format(result))
