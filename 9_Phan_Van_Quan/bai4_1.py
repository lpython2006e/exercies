#Create Student class with attributes like (Name, Nickname, birthday, class)
class Student():
    def __init__(self, Name, Nickname,birthday, clas):
        self.Name = Name
        self.Nickname = Nickname
        self.birthday = birthday
        self.clas = clas
Student_1 = Student('hoang', 'long', '12/12/12', '12A1')
print(Student_1.Name)
print(Student_1.Nickname)
print(Student_1.birthday)
print(Student_1.clas)