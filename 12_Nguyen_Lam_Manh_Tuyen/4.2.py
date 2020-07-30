# Create a program to enter student information, store it as list of student and allow to search students by their name (partial)

class Student:
    def __init__(self, name, nickname, birthday, classname):
        self.name = name
        self.nickname = nickname
        self.birthday = birthday
        self.classname = classname


class classlist:
    def __init__(self):
        self.list_student = []

    def add_student(selt, student):
        self.list_student.append(student)


class management:
    def getinput():
        while True:
            name = input("Please input student name\n")
            if len(name) <= 12:
                break
            else:
                print("Name can only contain a maximum of 12 characters")
                continue
        while True:
            birth = input("Please input student birthday mm/dd/yy \n")
            if len(birth) <= 8:
                break
            else:
                print("Birthday can only contain a maximum of 8 characters")
                continue
        while True:
            email = input("Please input student email\n")
            if len(email) <= 50:
                break
            else:
                print("Name can only contain a maximum of 50 characters")
                continue

        return name, birth, email

    def multiple_input():
        name, birthday, email = [], [], []
        num = int(input("How many students do you want to add?\n"))
        for i in range(0, num):
            temp = list(getinput())
            name.append(temp[0])
            birthday.append(temp[1])
            email.append(temp[2])
        return name, birthday, email

class ultil:
    def validate_