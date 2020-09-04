"""Create a program to enter student information,
store it as list of student and allow to search students by their name (partial)"""

# class Person:
#     def __init__(self, order, name, age):
#         self.order = order,
#         self.name = name,
#         self.age = age
#
#
# person = Person("", "", "")
# f = open("huong.csv", "r",newline='')
# content = f.read()
#
#
# print(content)
import csv


class Person:
    def __init__(self, STT_Class, Ten_Class, Tuoi_Class):
        self.stt = STT_Class
        self.ten = Ten_Class
        self.tuoi = Tuoi_Class


person = Person('', '', '')
person_list = []
reader = []


with open('huong.csv', 'w+') as fw:
    writer = csv.writer(fw,delimiter ='-',quotechar='"')
    x = [['Huong',"3/12/99",'layla@yopmail.com'],
         ['Minh', "1/12/99", 'layla1@yopmail.com'],
         ['Ngoc', "1/12/99", 'layla33@yopmail.com']]
    writer.writerow(["Name","Birth","Email"])
    writer.writerows(x)



with open('huong.csv', 'r') as file:
    reader = csv.reader(file)
    for item in reader:
        person = item
        person_list.append(person)
    print(person_list)

with open('huong.csv', 'r') as f:
    reader_csv = csv.DictReader(f)
    for item in reader_csv:
        print(item)







