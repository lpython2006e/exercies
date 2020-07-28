#Generate the output like: A(5), B(3), C(1) with input like ABBAAACB
# nhap_chuoi = input("Nhap vao chuoi so in hoa ")
# chuoi = sorted(nhap_chuoi)
# print(nhap_chuoi)
# print('A', '(',chuoi.count('A'),')')
# print('B', '(',chuoi.count('B'),')')
# print('C', '(',nhap_chuoi.count('C'),')')

# cach2
a= input("Nhap vao chuoi cua ban")
n= set(a)
print(n)
for char in n:
    dem = str(char) + "(" + str(a.count(char)) +")"
    print(dem)