# Write a function that computes the running total of a list.


def totalList(number, myList):
    tong = 0

    for i in range(number):
        x = int(input("myList[" + str(i) + "]= "))
        myList.append(x)
    print("myList = ", myList)

    for item in myList:
        tong += item
    print("tong cac phan tu trong list la: ", tong)


number = int(input("nhap vao so luong phan tu: "))
myList = []
totalList(number, myList)
