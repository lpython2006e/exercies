# Order the input string by ASC (a -> z, 0 -> 9) with any string

a = input("nhap vao chuoi: ")
number = ""
chu = ""
for x in a:
    if (x.isnumeric()): # kiem tra la so hay khong
        number += x
    else:
        chu += x
b = ''.join(sorted(str(number)))
c = ''.join(sorted(str(chu)))
chuoi = c+b
print("chuoi sau khi sap xep: " + chuoi)