#sap xep chuoi
#cach 1:

nhap_chuoi = input("Nhap vao chuoi bat ky ")
#su dung ham sort thi gia tri tra ve 0-9,a-z

# chuoi_sap_xep = sorted(nhap_chuoi)
# print(chuoi_sap_xep)

# nhan xet ord chuyen kiêu string thanh gia tri cua bang ma ASCII
string1 = []
stringa = []
stringA = []
for num in range(len(nhap_chuoi)):
     if ord(nhap_chuoi[num]) <=122 and ord(nhap_chuoi[num]) >= 97 :
         string1.append(nhap_chuoi[num])
     elif ord(nhap_chuoi[num]) >= 65 and ord(nhap_chuoi[num]) <= 90 :
         stringA.append(nhap_chuoi[num])
     else:
         stringa.append(nhap_chuoi[num])
string1.sort()
stringA.sort()
stringa.sort()

chuoi = stringa + stringA + string1
print(nhap_chuoi)
print(chuoi)