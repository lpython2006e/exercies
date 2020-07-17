# Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]

def input_list_1(n, list_1):
    for i in range(n):
        x = input("nhap phan tu thu " + str(i + 1) + ": ")
        list_1.append(x)


def input_list_2(n, list_2):
    for i in range(n):
        x = input("nhap phan tu thu " + str(i + 1) + ": ")
        list_2.append(x)


def concatenates_two_list(list_1, list_2):
    list_3 = list_1 + list_2
    return list_3


list_1 = []
list_2 = []
n = int(input("nhap so luong phan tu list 1: "))
input_list_1(n, list_1)
m = int(input("nhap so luong phan tu list 2: "))
input_list_2(m, list_2)
print("concatenates two list: ", concatenates_two_list(list_1, list_2))
