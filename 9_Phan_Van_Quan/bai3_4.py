#Update previous one, allow to enter multiple classmate, at end, allow to save to file as CSV format

import re
import clevercsv

limit_name = 7
limit_birthday = 8
limit_emall = 30

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

def input_classmate():
    user = input("Enter classmate first_nam last_name birthday Email ")
    list_user = re.split("\s",user)
    if check_input_name(list_user) and check_input_birday(list_user) and check_input_email(list_user):
        new_input = input("Ban co muon nhap tiep ko Yes or No ")
        if new_input == 'Yes' or new_input == 'yes':
            input_classmate()
        else:
            print(list_user)
    else:
        print("ban nhap sai format roi")
        input_classmate()


input_classmate()