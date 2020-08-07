#Write a guessing game where the user has to guess a secret number.
#After every guess the program tells the user whether their number was too large or too small
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively
secret_num = 100
count = 0
print('Hello your welcome to the guess game')
print('you have 10 input')
gia_tri_da_nhap = [0]
# dang list
while count < 3:
    numinput = eval(input('Nhap vao du doan cua ban '))
    gia_tri_da_nhap.append(numinput)
    count = count + 1
    #print(gia_tri_da_nhap)
    print("Ban da nhap ", count,"lan")
    #print(gia_tri_da_nhap[count])
    if gia_tri_da_nhap[count] == gia_tri_da_nhap[count-1]:
        del gia_tri_da_nhap[count]
        count = count -1

    if (numinput < 100):
        print('too small')
    elif (numinput > 100):
        print('too large')
    else:
        print('you are correct')
        break
del gia_tri_da_nhap[0]
print(gia_tri_da_nhap)




