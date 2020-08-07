#Create a program to enter student information, store it as list of student and allow to search students by their name (partial)
import re

class Student():
    def __init__(self, Name, Nickname, Birthday, Class):
        self.Name = Name
        self.Nickname = Nickname
        self.Birthday = Birthday
        self.Class = Class


def search_student_by_name():
    name_student = input("Nhap vao ten student ban muon search ")
    for stt in range(len(inf_student[0])):
        if inf_student[0][stt] == name_student:
            print("ton tai sinh vien ban nhap")
            print("Thong tin ve sinh vien la")
            information = []
            for i in range(4):
                information.append(inf_student[i][stt])
            print(information)
            break
        else:
            print("sorry chung toi khong co ten sinh vien nay vui long nhap lai")
            search_student_by_name()

def Nhap_sinh_vien():
    name = []
    nickname = []
    birthday = []
    cLass = []
    so_luong_student = eval(input("Nhap vao so luong sinh vien "))
    for i in range(so_luong_student):
        input_student = input("Name nickname birthday class ")
        list = re.split("\s", input_student)
        Student_1 = Student(list[0], list[1], str(list[2]), str(list[3]))
        name.append(Student_1.Name)
        nickname.append(Student_1.Nickname)
        birthday.append(Student_1.Birthday)
        cLass.append(Student_1.Class)
    return name, nickname, birthday, cLass

inf_student = list(Nhap_sinh_vien())

search_student_by_name()

