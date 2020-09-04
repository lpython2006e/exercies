"""Create a program to enter student information,
store it as list of student and allow to search students by their name (partial)"""


class Student:
    def __init__(self, name: str = None, nickname: str = None, birthday: str = None, class_number: int = None):
        self.name = name,
        self.nickname = nickname,
        self.birthday = birthday,
        self.class_number = class_number

    def enter_student_info(self):
        list_info = []
        student_info = input("Please enter name,nickname,birthday,class of student: ")
        for i in range(0, len(student_info)):
            list_info = [x.strip() for x in student_info.split(',')]
        return list_info

class StudentManagement:
    def enter_student_info(self):
        list_info = []
        student_info = input("Please enter name,nickname,birthday,class of student: ")
        for i in range(0, len(student_info)):
            list_info = [x.strip() for x in student_info.split(',')]
        return list_info

    #def show_menu(self):


class myClass:
    def __init__(self):
        self.list_student = []

    def add_student(self, student):
        self.list_student.append(student)

    def print_class(self):
        for item in self.list_student:
            print(item)

    def search_student(self, a, b):
        count = 0
        for item in a:
            if b in item[0]:
                print("{} in class {}".format(item[0],item[3]))
                count += 1
        if count == 0:
            print("This student is not in our class")


my_student_1 = Student()
my_student_2 = Student()
my_class = myClass()
student_1 = my_student_1.enter_student_info()
student_2 = my_student_2.enter_student_info()
my_class.add_student(student_1)
my_class.add_student(student_2)
my_class.print_class()
my_class.search_student(my_class.list_student,"Huo")

#entry point to start program
main()
 # create student management instance: studenmanagement()
 # student management: show_menu -> action [1 -> Add Student, 2 -> Add Class...]
 # student_management: Add student /add class..
 # save_to_csv(list_student, list_class)
