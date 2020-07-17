# Write a function that returns the largest element in a list.

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
def maxele(lst):
    return (max(lst))
#solution2
def max_in_list(lst):
    temp=lst[0]
    for i in range(0,len(lst)-1):
        if temp<lst[i+1]:
            temp=lst[i+1]
    return temp

lst=[]
getinput()
result = max_in_list(lst)
print("Largest element in given list is {}".format(result))
