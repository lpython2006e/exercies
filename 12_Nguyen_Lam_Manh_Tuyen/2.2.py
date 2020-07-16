#Write function that reverses a list, preferably in place.
def getinput():
    while True:
        element=input("Please input your element \n")
        if element!='':
            lst.append(element)
        else:
            print(lst)
            break
    return lst
def reverselist(lst):
    lst.reverse()
    return (lst)


lst=[]
getinput()
result = reverselist(lst)
print("List after reversed is {}".format(result))
