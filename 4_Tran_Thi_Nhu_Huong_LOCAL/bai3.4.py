"""Update previous one, allow to enter multiple classmate, at end, allow to save to file as CSV format"""
from datetime import datetime
import re
import csv


def _check_valid_name(a):
    list = ["Huong", "Thach", "Dung", "Thien"]
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


def _get_list(a):
    for i in range(0, len(a)):
        list = [x.strip() for x in a.split(',')]
    return list


def _validate_student_info(mylist: list):
    name = _check_valid_name(mylist[0])
    birth = _check_valid_birthday(mylist[1])
    email = _check_valid_email(mylist[2])
    if name is False:
        _validate_student_info(input_student_detail())
    if birth is False:
        _validate_student_info(input_student_detail())
    if email is False:
        _validate_student_info(input_student_detail())
    return mylist


def input_student_detail():
    student = input("Please input name, birthday and email for Student: ")
    student_details = _get_list(student)
    return student_details


def _input_student_info(num):
    for i in range(num):
        student_details = _validate_student_info(input_student_detail())
        outputFile = open("huong.csv", "a", newline='')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(student_details)


f = open("huong.csv", "a+")
_input_student_info(2)
