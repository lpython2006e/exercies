# Write a function that returns the elements on odd positions in a list.


def input_list(n, my_list):
    for i in range(n):
        x = input("nhap phan tu thu " + str(i+1) + ": ")
        myList.append(x)

def printOppPosition(a):
    print("cac phan tu co vi tri le la: ")
    for i in range(len(a)):
        if(i%2!=0):
            print("a["+str(i)+"]=",a[i])

myList = []
input_list(myList)
printOppPosition(myList)