# "Tìm các thư viện hỗ trợ đọc file CSV theo cấu trúc cột bất kỳ và map vào list object mình định nghĩa
# (so sánh, lựa chọn thư viện tốt nhất)
# Ví dụ: Có CSV
# STT, Tên, Tuổi
# 1, Trung, 30
# 2, Phượng, 35
# -> tạo ra 1 class Person có 3 fields, stt, ten, tuổi và List<Person> từ file CSV. "

# Xác định danh sách ( person_list ).
# Mở tệp csv.
# Tạo một csv.reader.
# Lặp lại qua các hàng.
# Chuyển đổi int thành float.
# Tạo một Person thể hiện và truyền tên và số.
# Cuối cùng nối ví dụ person này vào personlist_list.


import csv


# class Person:
#
#     def __init__(self, stt, ten, tuoi):
#         self.stt = stt
#         self.ten = ten
#         self.tuoi = tuoi
#
#
# person_list = []
#
# with open('dulieu.csv', newline='') as csv_file:
#     reader = csv.reader(csv_file)
#     next(reader, None)  # Skip the header.
#     # Unpack the row directly in the head of the for loop.
#     for stt, ten, tuoi in reader:
#
#         # Now create the Person instance and append it to the list.
#         person_list.append(Person(stt, ten, tuoi))
# print(person_list)


class Person:
    def __init__(self, STT_Class, Ten_Class, Tuoi_Class):
        self.stt = STT_Class
        self.ten = Ten_Class
        self.tuoi = Tuoi_Class


person_list = []
with open('dulieu.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for STT, Ten, Tuoi in reader:
        person_list.append(Person(STT, Ten, Tuoi))

        print(STT, Ten, Tuoi)
