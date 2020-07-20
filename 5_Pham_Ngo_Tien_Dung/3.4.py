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
    for i in range(0, len(mylist)):
        name = _check_valid_name(mylist[0])
        if name is False:
            new_name = input("please input new name,birthday and email for Student: ")
            birth = _check_valid_birthday(mylist[1])
        elif birth is False:
            new_birth = input("please input new birth")
            birth = _check_valid_birthday(new_birth)


def _input_student_info(num):
    for i in range(num):
        student = input("Please input name, birthday and email for Student: ")
        student_details = _get_list(student)
        _validate_student_info(student_details)
        outputFile = open("huong.csv", "a", newline='')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(student_details)


f = open("huong.csv", "a+")
_input_student_info(5)
