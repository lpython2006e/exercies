#Write a function that computes the running total of a list.

def getinput():
    while True:
        element=input("Please input your element \n")
        if element!='':
            lst.append(element)
        else:
            print(lst)
            break
    return lst
def oddlist(lst):
    lst=lst[1::2]
    return (lst)


lst=[]
getinput()
result = oddlist(lst)
print("Element on odd position is {}".format(result))