"""Create Student class with attributes like (Name, Nickname, birthday, class)"""


class Student:
    def __init__(self, name, nickname, birthday, class_num):
        self.name = name
        self.nickname = nickname
        self.birthday = birthday
        self.class_num = class_num

    def show_info(self):
        print("Name is {}, nickname is {}, birthday is {},class is {}.".format(self.name, self.nickname, self.birthday, self.class_num))


first_student = Student("Name", "Boy", "03/12/99", "1")
first_student.show_info()
