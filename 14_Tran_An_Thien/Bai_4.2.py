"""
    Create a program to enter student information,
    store it as list of student and allow to search students by their name (partial)

"""


# Definig a class student, which contain
# name and Roll number and marks of the student

class Student(object):
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def getmarks(self):
        return self.marks

    def getroll(self):
        return self.roll

    def __str__(self):
        return self.name + ' : ' + str(self.getroll()) + '  : ' + str(self.getmarks())


# Defining a function for building a Record
# which generates list of all the students
def Markss(rec, name, roll, marks):
    rec.append(Student(name, roll, marks))
    return rec


# Main Code
Record = []
x = 'y'
while x == 'y':
    name = input('Enter the name of the student: ')
    height = input('Enter the roll number: ')
    roll = input('Marks: ')
    Record = Markss(Record, name, roll, height)
    x = input('another student? y/n: ')

# Printing the list of student
n = 1
for el in Record:
    print(n, '. ', el)
    n = n + 1
# đối tượng thực sự tồn tại thì người ta mới quan tâm đên thuộc tính
#
# Create class "Student"
# class Student:
#     # Constructor
#     def __init__(self, name, sex, address, birthday):
#         self.name = name
#         self.sex = sex
#         self.address = address
#         self.birthday = birthday

# Function to create and append new student
# while 1:
# def accept(self, name, sex, address, birthday):
#     # use  ' int(input()) ' method to take input from user
#     # ob = input('nhhap thong tin sinh vien: %, %, %, %', name, sex, address, birthday)
#     ob = Student(name, sex, address, birthday)
#     ls.append(ob)

# Function to display student details

# def display(self, ob):
#     print("Name   : ", ob.name)
#     print("Sex : ", ob.sex)
#     print("Address : ", ob.address)
#     print("Birthday : ", ob.birthday)
#     print("\n")

# Search Function

# def search(self, rn):
#     for i in range(ls.__len__()):
#         if (ls[i].rollno == rn):
#             return i

# Delete Function

# def delete(self, rn):
#     i = obj.search(rn)
#     del ls[i]

# Update Function

# def update(self, rn, No):
#     i = obj.search(rn)
#     roll = No
#     ls[i].rollno = roll;

# Create a list to add Students


# ls = []
# an object of Student class
# obj = Student('', '', '', '')

# print("\nOperations used, ")
# print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
# obj.accept("A", 1, 100, 100)
# obj.accept("B", 2, 90, 90)
# obj.accept("C", 3, 80, 80)

# elif(ch == 2):
# print("\n")
# print("\nList of Students\n")
# for i in range(ls.__len__()):
#     obj.display(ls[i])

# # elif(ch == 3):
# print("\n Student Found, ")
# s = obj.search(2)
# obj.display(ls[s])
#
# # elif(ch == 4):
# obj.delete(2)
# print(ls.__len__())
# print("List after deletion")
# for i in range(ls.__len__()):
#     obj.display(ls[i])
#
# # elif(ch == 5):
# obj.update(3, 2)
# print(ls.__len__())
# print("List after updation")
# for i in range(ls.__len__()):
#     obj.display(ls[i])

# else:
# print("Thank You !")
