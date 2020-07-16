#Write a function that computes the running total of a list.

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
def running_sum(lst):
    temp_lst=[]
    total=0
    for i in range(0,len(lst)):
       total+=int(lst[i])
       temp_lst.append(total)
    return (temp_lst)

lst=[]
getinput()
result = running_sum(lst)
print("Running total is {}".format(result))