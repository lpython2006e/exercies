"""Create a program to enter student information,
store it as list of student and allow to search students by their name (partial)"""


class student:
    def __init__(self, name: str = None, nickname: str = None, birthday: str = None, class_number: int = None):
        self.name = name,
        self.nickname = nickname,
        self.birthday = birthday,
        self.class_number = class_number

    def get_list(self, a):
        for i in range(0, len(a)):
            list = [x.strip() for x in a.split(',')]
        return list

    def enter_student_info(self):
        student_info = input("Please enter name,nickname,birthday,class of student: ")
        list_info = self.get_list(student_info)
        return list_info

    def store(self, student_info):
        self.list_student.append(student_info)
        return self.list_student

    def search(self, a, b):
        count = 0
        for item in a:
            if b in item[0]:
                print("the student is {}".format(item[0]))
                count +=1
        if count == 0:
            print ("This student is not in our class")



my_student = student()
info_of_student_1 = my_student.enter_student_info()
info_of_student_2 = my_student.enter_student_info()
myclass = my_student.store(info_of_student_1)
myclass = my_student.store(info_of_student_2)
print(myclass)
my_student.search(myclass, "Huo")
