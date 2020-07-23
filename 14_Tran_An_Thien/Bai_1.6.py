# Write a guessing game where the user has to guess a secret number.
# After every guess the program tells the user whether their number was too large or too small.
# At the end the number of tries needed should be printed.
# It counts only as one try if they input the same number multiple times consecutively.
sobimat = 3
ccac_so_da_nhap = set()

# while not number>0 or number>17:
#     number = int(input('moi ban nhap vao so nguyen duong: '))
while 1:
    number = int(input('moi ban nhap vao 1 so: '))
    ccac_so_da_nhap.add(number)
    if (number == sobimat):
        print('chuc mung ban da nhap dung')
    else:
        number = int(input('so ban vua nhap k dung, moi ban nhap so khac: '))
        if (number > sobimat):
            print('so ban nhap lon hon')
        else:
            print('so ban nhap nho hon')
