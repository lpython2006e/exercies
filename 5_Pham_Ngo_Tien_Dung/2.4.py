# Write a function that returns the elements on odd positions in a list.

myList = ["a", "b", "c", "d", "e", "f", "g", "h"]

def printOppPosition(a):
    print("cac phan tu co vi tri le la: ")
    for i in range(len(a)):
        if(i%2!=0):
            print("a["+str(i)+"]=",a[i])

printOppPosition(myList)