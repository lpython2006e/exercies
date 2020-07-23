# Write a program that prints the next 20 leap years (enter year or if not, get current year as default)
# dem = 0
# def leapyr(n):
#     if n%4==0 and n%100!=0:
#         if n%400==0:
#             print (n, " is a leap year.")
#     elif n%4!=0:
#         print (n, " is not a leap year.")
# print(leapyr(1900))

# a=[]
# i=2020
# while 1:
#     if i%4==0 and i%100!=0:
#         a.append(i)
#     if len(a)==20:
#         break
#     i+=1
# print(a)

import datetime

now = datetime.datetime.now()
string = input("nhập vào năm: ")
if string:
    actual_year = int(string)
else:
    actual_year = now.year

i = 0
print("danh sách 20 năm nhuận liên tiếp: ")
while i <= 20:
    if actual_year % 4 == 0 and actual_year % 100 != 0:
        i += 1
        print(actual_year)
        actual_year += 1
    else:
        actual_year += 1
