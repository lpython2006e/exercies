#Update previous one, allow to enter multiple classmate, at end, allow to save to file as CSV format

import re
import csv

limit_name = 7
limit_birthday = 8
limit_emall = 30
first_name = []
last_name = []
birthday = []
email = []

def check_input_name(list_input):
    if(len(list_input[0]) < limit_name and len(list_input[1]) < limit_name):
        return True
    else:
        return False

def check_input_birday(list_input):
    check_birday = bool(re.search(r"(^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{2}$)", list_input[2]))
    if check_birday and len(list_input[2]) <= limit_birthday :
        return True
    else:
        return False

def check_input_email(list_input):
    check_email = bool(re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", list_input[3]))
    if check_email and len(list_input[3]) < limit_emall:
        return True
    else:
        return False

def check_inf():
    user = input("Enter classmate first_nam last_name birthday Email ")
    list_user = re.split("\s",user)
    if check_input_name(list_user) and check_input_birday(list_user) and check_input_email(list_user):
        first_name.append(list_user[0])
        last_name.append(list_user[1])
        birthday.append(list_user[2])
        email.append(list_user[3])

        return first_name, last_name, email, birthday
    else:
        print("ban nhap sai format roi")
        print("nhap lai di")
        check_inf()


def input_classmate():
    with open('classmate.csv', 'w', newline='') as file:
        fieldnames = ['first_name', 'last_name', 'birthday', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        so_luong_sv = eval(input("Nhap vao so luong sinh vien muon nhap "))
        for i in range(so_luong_sv):
            check_inf()
            writer.writerow({'first_name': first_name[i], 'last_name': last_name[i], 'birthday':birthday[i], 'email':email[i]})

input_classmate()
f = open("classmate.csv", "r")
print(f)