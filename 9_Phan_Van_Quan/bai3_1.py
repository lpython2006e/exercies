#Write a program that allow user enter a file name (path) then content, allow user to save it
# import os
# os.mkdir("test.txt")
file_name = input("Nhap vao file_name dang .txt ")
file = open(file_name, 'w+')
file.write("Hello is is comment")
file.flush()
file.close()

file_2 = open(file_name,'r')
print(file_2.read())