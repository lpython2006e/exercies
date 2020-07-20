"""Write a program that allow user to enter classmate (name, Birthday, Email),
validate if enter values are valid format (limit length apply), else ask user to enter again per field"""
from datetime import datetime
import re


def _check_valid_name(a):
    list = ["Huong", " Thach", "Dung", "Thien"]
    if a not in list:
        return False
    else:
        return True


def _check_valid_birthday(b):
    try:
        datetime.strptime(b, '%m/%d/%y')
    except:
        return False
    return True


def _check_valid_email(c):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", c))


name = input("Please input your classmate name: ")
while _check_valid_name(name) is False:
    name = input("Please input your classmate name again: ")
else:
    birth = input("Please input your classmate birthday with format DD/MM/YY")

while _check_valid_birthday(birth) is False:
    birth = input("Please input your classmate birthday with format DD/MM/YY")
else:
    email = input("please enter your email: ")

while _check_valid_email(email) is False:
    email = input("please enter your email: ")
else:
    print("Welcome to our class")
