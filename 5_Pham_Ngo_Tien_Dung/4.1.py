# Create Student class with attributes like (Name, Nickname, birthday, class)
'''
Tạo lớp Sinh viên với các thuộc tính như (Tên, Biệt hiệu, sinh nhật, lớp)
'''


class Studen:

    # Constructor
    def __init__(self, _name, _nickname, _birthday, _class):
        self._name = _name
        self._nickname = _nickname
        self._birthday = _birthday
        self._class = _class


student = Studen("Pham Dung", "Kenshin", "10/09/1998", "DHTin13A1")

print("name: ", student._name)
print("nickname: ", student._nickname)
print("birthday: ", student._birthday)
print("class: ", student._class)
