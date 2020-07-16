# Write a function that checks whether an element occurs in a list.

#get list from user input until none input
def getinput():
    while True:
        element = input("Please input your element \n")
        if element != '':
            lst.append(element)
        else:
            print(lst)
            break
    return lst

#count element in a list
def checkelement():
    check = input("Please input your element to check \n")
    if lst.count(check) != 0:
        print("The element occurs {} times in the list".format(lst.count(check)))
    else:
        print("The element does not occur in the list")
lst=[]
getinput()
checkelement()