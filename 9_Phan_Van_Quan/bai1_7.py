# nhap vao 1 chuoi gom ca ky tu chu va so
string = 'abdwndjwd123434'
# in chuoi ban vua nhap
print(string[1])
i=0
j=0
string1 = '                '
string2 = '                   '
#sap xep chuoi
for num in range(len(string)):
    if ord(string[num]) <=122 and ord(string[num]) >= 97 :
        string1[i] = string[num]
        i = i+1
    if ord(string[num]) >= 48 and ord(string[num]) <= 57 :
        string2[j] =  string[num]
print(string1)
print(string2)
# sap xep theo thu tu trong tung chuoi