# tinh tong cua day so co boi so cua 3 ,5

index = eval(input("gia tri nhap vao "))
print("gia tri cuoi cua chuoi ", index)
tong = 0
for num in range(1, index):
    if (num % 3 == 0 ) or (num % 5 == 0 ):
        tong = tong + num
print(tong)