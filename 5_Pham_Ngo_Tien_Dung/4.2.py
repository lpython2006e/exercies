#  Create a program to enter student information,
#  store it as list of student and allow to search students by their name (partial)

'''
Tạo một chương trình để nhập thông tin sinh viên,
 lưu trữ dưới dạng danh sách sinh viên và cho phép tìm kiếm sinh viên theo tên của họ (một phần)
'''


class Student:

    # Constructor
    def __init__(self, _name, _birthday, _class):
        self._name = _name
        self._birthday = _birthday
        self._class = _class

    def nhap(self, _name, _birthday, _class):
        ob = Student(_name, _birthday, _class)
        student_list.append(ob)

    def hien_thi(self, ob):
        print("Name   : ", ob._name)
        print("Birthday : ", ob._birthday)
        print("Class : ", ob._class)
        print("___________________________________________________")


student_list = []
student = Student('', '', '')

n = int(input("nhap so luong sinh vien: "))
print("___________________________________________________")

for i in range(n):
    _name = input("nhap ten sv " + str(i + 1) + ": ")
    _birthday = input("nhap ngay thang nam sinh: ")
    _class = input("nhap lop: ")
    student.nhap(_name, _birthday, _class)
    print("___________________________________________________")

print("\n\n__________________ Danh sách sv____________________")
for i in range(len(student_list)):
    student.hien_thi(student_list[i])
