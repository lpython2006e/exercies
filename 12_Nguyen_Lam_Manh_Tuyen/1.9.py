#Write a program that prints the next 20 leap years (enter year or if not, get current year as default)
import datetime
now=datetime.datetime.now()
def leapyear(year):
    count=0
    listofyear=[]
    while count<20:
        if ((year%4==0)&(year%100!=0))|(year%400==0):
            listofyear.append(year)
            count = count + 1
        year=year+1
    return listofyear
print("Which year you want to start?")
input=input() or now.year
listofyear=leapyear(int(input))
print(listofyear)