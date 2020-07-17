# Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion.
# (Subject to availability of these constructs in your language of choice.)

def inputList(n,myList):
    for i in range(n):
        x = int(input("nhap phan tu thu " + str(i+1) + ": " ))
        myList.append(x)

def sum_by_for(myList):
    tong=0
    for item in myList:
       tong+=item
    return tong

def sum_by_while(myList):
    tong=i=0
    while(i<len(myList)):
        tong += myList[i]
        i+=1
    return tong

def sum_by_recursion(n, myList):
    if (n == 0):
        return 0
    else:
        return myList[n-1]+sum_by_recursion(n-1,myList)

myList = []
n = int(input("nhap so phan tu: "))
inputList(n,myList)
print("sum(for): ", sum_by_for(myList))
print("sum(while): ", sum_by_while(myList))
print("sum(recursion)", sum_by_recursion(n,myList))