#Write a program that read content of a file (path) then show to screen,
# if the file doesn’t exist, announce user
import os
#
# cach1
# for num in file_2:
#     if num == '':
#         print('file not exit')
#     else:
#         print('ok')

#cach 2
def check_exist(filename):
    if os.path.exists(filename):
        return 1
    else:
        return 0

file = input("nhap ten file ")

if check_exist(file):
    f = open(file, 'r')
    f2 = f.read()
    print("file exist")
else:
    print("file not exits")
print(f2)
