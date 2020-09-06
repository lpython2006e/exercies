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
# Lặp lại qua các item.
# Tạo một Person thể hiện và truyền item.
# Cuối cùng nối ví dụ person này vào personlist_list.

# csv, paratext, pandas
# Delimiter

import csv


class Person:
    def __init__(self, stt_class, ten_class, tuoi_class):
        self.stt = stt_class
        self.ten = ten_class
        self.tuoi = tuoi_class


person = Person('', '', '')
person_list = []
with open('dulieu.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for item in reader:
        person = item
        person_list.append(item)
        print(person)

    print(person_list)
