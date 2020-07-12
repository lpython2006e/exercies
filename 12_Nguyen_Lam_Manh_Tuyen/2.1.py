#Write a function that returns the largest element in a list.

def findmax():
    lst=[]
    while True:
        try:
            while True:
                lst.append(int(input("Please input your list, press enter for each element \n")))
        except ValueError:
            print("Your input is not a valid number")
        else:
            break
    maxele = max(lst)
    return maxele
    print("Your input {} element, max elemen is {}".format(len(lst),maxele))

findmax()