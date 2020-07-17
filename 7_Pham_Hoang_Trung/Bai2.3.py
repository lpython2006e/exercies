#Write a function that checks whether an element occurs in a list.

def Checks(element, lists):
    for i in lists:
        if element == i:
            return True

lists = ['thanh', 'hieu', 'hanh', 'hai']
element = input("Nhap phan tu: ")
if(Checks(element,lists)):
    print("Nam trong List")
else:
    print("Khong nam trong List")




