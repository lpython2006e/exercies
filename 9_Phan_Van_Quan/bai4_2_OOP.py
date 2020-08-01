


class Student():
    def __init__(self, name, nick_name, birthday, cLass):
        self.name = name
        self.nick_name = nick_name
        self.birthday = birthday
        self.cLass = cLass

#student la list
class Class():
    def __init__(self, CLass, student):
        self.CLass = CLass
        self.student = student

class Student_Management():
    list_student = []
    list_class = []