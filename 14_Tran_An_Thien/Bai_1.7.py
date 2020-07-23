# Order the input string by ASC (a -> z, 0 -> 9) with any string
k = input("Nhập chuỗi bất kỳ: ")
# li = []
# x = len(k)
# for i in range (0,x):
#     li.append(k[i])
#
# print("List is : ",li)
#
#
# for i in range(0,x):
#     for j in range(0,x):
#         if li[i]<li[j]:
#             temp = li[i]
#             li[i]=li[j]
#             li[j]=temp
# j=""
#
# for i in range(0,x):
#     j = j+li[i]
#
# print("chuỗi sau khi sắp xếp : ",j)

number = ''
character = ''
for x in k:
    if (x.isnumeric()):
        number += x
    else:
        character += x
b = ' '.join(sorted(str(number)))
c = ' '.join(sorted(str(character)))

chuoi = c + ' ' + b

print('chuoi sau sap xep: ' + chuoi)
