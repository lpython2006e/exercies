# Write a function that returns the largest element in a list.

def getinput():
    while True:
        element=input("Please input your element \n")
        if element!='':
            lst.append(element)
        else:
            print(lst)
            break
    return lst
def maxele(lst):
    return (max(lst))


lst=[]
getinput()
result = maxele(lst)
print("Largest element in given list is {}".format(result))
