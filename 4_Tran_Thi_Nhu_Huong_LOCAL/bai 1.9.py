"""Write a program that prints the next 20 leap years (enter year or if not, get current year as default)"""
import  datetime
now = datetime.datetime.now()
string = input("input the year")
if string:
    actual_year = int(string)
else:
    actual_year= now.year

total = 20
i= 0
print ("List of next 20 leap years:")
while i <=20:
    if (actual_year % 4 == 0 and actual_year % 100!=0) or (actual_year % 400==0):
        i+=1
        print(actual_year)
        actual_year += 1
    else:
        actual_year+=1

